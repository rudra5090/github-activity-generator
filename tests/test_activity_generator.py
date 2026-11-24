import subprocess
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import activity_generator


class ActivityGeneratorTests(unittest.TestCase):
    def test_make_change_appends_utc_record_with_newline(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "nested" / "activity.txt"
            with patch.object(activity_generator, "FILE_TO_MODIFY", str(target)):
                returned_path = activity_generator.make_change()
            self.assertEqual(returned_path, target)
            content = target.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("Activity recorded at "))
            self.assertTrue(content.endswith("\\n"))
            self.assertNotIn("\\\\n", content)
            self.assertRegex(content, r"Activity recorded at \\d{4}-\\d{2}-\\d{2}T.*\\+00:00\\n")

    def test_rejects_empty_activity_path(self):
        with patch.object(activity_generator, "FILE_TO_MODIFY", "  "):
            with self.assertRaisesRegex(ValueError, "FILE_TO_MODIFY"):
                activity_generator.make_change()

    def test_rejects_directory_as_activity_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(activity_generator, "FILE_TO_MODIFY", temp_dir):
                with self.assertRaisesRegex(ValueError, "must point to a file"):
                    activity_generator.make_change()

    def test_create_commit_checks_repository_before_writing_and_commits_only_target(self):
        preflight = subprocess.CompletedProcess(args=["git", "rev-parse"], returncode=0, stdout="true\\n", stderr="")
        with patch.object(activity_generator, "make_change", return_value=Path("activity.txt")), \\
             patch.object(activity_generator.subprocess, "run", side_effect=[preflight, None, None]) as run_mock:
            activity_generator.create_commit()
        self.assertEqual(run_mock.call_count, 3)
        run_mock.assert_any_call(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            text=True,
        )
        run_mock.assert_any_call(["git", "add", "--", "activity.txt"], check=True)
        commit_args = run_mock.call_args_list[2].args[0]
        self.assertEqual(commit_args[:3], ["git", "commit", "-m"])
        self.assertIn("Auto-generated contribution (", commit_args[3])

    def test_create_commit_refuses_non_repository_without_writing(self):
        failure = subprocess.CalledProcessError(128, ["git", "rev-parse"])
        with patch.object(activity_generator.subprocess, "run", side_effect=failure), \\
             patch.object(activity_generator, "make_change") as change_mock:
            with self.assertRaisesRegex(RuntimeError, "inside a Git working tree"):
                activity_generator.create_commit()
        change_mock.assert_not_called()

    def test_rejects_empty_commit_message(self):
        with patch.object(activity_generator, "COMMIT_MESSAGE", ""):
            with patch.object(activity_generator, "_ensure_git_repository") as git_mock:
                with self.assertRaisesRegex(ValueError, "COMMIT_MESSAGE"):
                    activity_generator.create_commit()
                git_mock.assert_not_called()

    def test_dry_run_prints_preview_without_side_effects(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "activity.txt"
            output = StringIO()
            with patch.object(activity_generator, "FILE_TO_MODIFY", str(target)), \\
                 patch.object(activity_generator.subprocess, "run") as run_mock, \\
                 patch("sys.stdout", output):
                activity_generator.dry_run()
            self.assertFalse(target.exists())
            run_mock.assert_not_called()
            text = output.getvalue()
            self.assertIn("DRY RUN", text)
            self.assertIn(str(target), text)
            self.assertIn("Would append: Activity recorded at ", text)
            self.assertIn("git add --", text)
            self.assertIn("git commit -m", text)


if __name__ == "__main__":
    unittest.main()
