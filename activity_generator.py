import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from config import FILE_TO_MODIFY, COMMIT_MESSAGE


def _validated_activity_path():
    """Return the configured activity path, rejecting invalid configuration."""
    if not isinstance(FILE_TO_MODIFY, str) or not FILE_TO_MODIFY.strip():
        raise ValueError("FILE_TO_MODIFY must be a non-empty path string.")
    return Path(FILE_TO_MODIFY)


def make_change():
    """Append a real current-time UTC activity record."""
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path = _validated_activity_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        file.write(f"Activity recorded at {timestamp}\n")

    return path


def create_commit():
    """Commit only the activity file using the current Git timestamp."""
    if not isinstance(COMMIT_MESSAGE, str) or not COMMIT_MESSAGE.strip():
        raise ValueError("COMMIT_MESSAGE must be a non-empty string.")

    activity_file = make_change()
    subprocess.run(["git", "add", "--", str(activity_file)], check=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    message = f"{COMMIT_MESSAGE.strip()} ({timestamp})"
    subprocess.run(["git", "commit", "-m", message], check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Record and commit genuine GitHub activity using the current date."
    )
    parser.parse_args()

    create_commit()
    print("Current activity recorded and committed successfully.")


if __name__ == "__main__":
    main()
