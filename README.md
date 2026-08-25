# GitHub Activity Generator

A small Python CLI that appends an activity entry and creates a Git commit for a supplied date.

> This project is intended for learning Git, GitHub workflows, automation, and commit tooling. Do not use it to misrepresent professional activity or contributions.

## Features

- Simple command-line interface
- Date-based commit creation
- Configurable activity file
- Git workflow automation with Python

## Requirements

- Python 3.10+
- Git

## Setup

```bash
git clone https://github.com/rudra5090/github-activity-generator.git
cd github-activity-generator
python -m pip install -r requirements.txt
```

If you do not need the optional development dependencies, the script itself uses only Python's standard library.

## Usage

```bash
python activity_generator.py --date 2026-08-25
```

The command validates the date and then appends a timestamp to the configured activity file before creating a commit.

## Project Structure

```text
.
├── activity_generator.py
├── config.py
├── activity.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Configuration

`config.py` contains the activity file path, default branch, and commit-related settings.

## Development Workflow

1. Create an issue describing the change.
2. Create a focused feature or fix branch.
3. Make the smallest useful change.
4. Run tests or validation locally.
5. Open a pull request and describe the change.
6. Review the PR before merging.

## Contributing

Keep changes focused, use clear commit messages, and update documentation when behavior changes.

## License

This project is provided for educational and portfolio purposes.
