# GitHub Activity Generator

A small Python utility that records a genuine activity entry with the current UTC time and commits only the configured activity file. It does not backdate commits.

## Requirements

- Python 3.8+
- Git installed and available on PATH
- Run the script from inside a Git working tree
- Git user name and email configured

## Usage

1. Clone this repository and open its folder.
2. Configure Git if you have not already:
   ```bash
   git config user.name "Your Name"
   git config user.email "you@example.com"
   ```
3. Preview the operation without changing anything:
   ```bash
   python activity_generator.py --dry-run
   ```
4. If the preview is correct, run it:
   ```bash
   python activity_generator.py
   ```

Before appending an activity record, the script checks that it is running inside a Git working tree. If Git is missing or the current directory is not a repository, it stops without modifying the activity file. It then stages only the configured file and creates a commit using the current date/time.

The dry-run mode displays the target file, proposed record, and Git commands without creating files or executing Git.

If validation or a Git command fails, the command now prints a concise error with a non-zero exit status instead of an unhandled Python traceback. For a failed Git commit, inspect `git status` before retrying.

## Run tests

The project uses Python's built-in `unittest` framework, so no extra test dependency is required:

```bash
python -m unittest discover -s tests -v
```

Tests use temporary files and mocked Git commands. They do not create commits in your repository.

## Configuration

Edit `config.py` to set `FILE_TO_MODIFY` and `COMMIT_MESSAGE`. The activity path must be a non-empty file path, not an existing directory.

Use this tool only for real, transparent project activity; do not use it to fabricate or backdate contributions.
