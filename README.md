# GitHub Activity Generator

A small Python utility that records a genuine activity entry with the current UTC time and commits only the configured activity file. It does not backdate commits.

## Requirements

- Python 3.8+
- Git installed and configured with your name and email
- Run this script inside a Git repository

## Usage

1. Clone this repository and open its folder.
2. Configure Git if you have not already:
   ```bash
   git config user.name "Your Name"
   git config user.email "you@example.com"
   ```
3. Run the script:
   ```bash
   python activity_generator.py
   ```

The script appends a UTC timestamp to the file configured in `config.py`, stages that file only, and creates a commit using the current date/time. Review the change before pushing.

## Run tests

The project uses Python's built-in `unittest` framework, so no extra test dependency is required:

```bash
python -m unittest discover -s tests -v
```

Tests use temporary files and mocked Git commands. They do not create commits in your repository.

## Configuration

Edit `config.py` to set `FILE_TO_MODIFY` and `COMMIT_MESSAGE`.

Use this tool only for real, transparent project activity; do not use it to fabricate or backdate contributions.
