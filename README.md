# GitHub Activity Generator

[![CI](https://github.com/rudra5090/github-activity-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/rudra5090/github-activity-generator/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A small Python CLI for learning Git, GitHub workflows, automation, and commit tooling.

> **Responsible use:** this project is for learning Git/GitHub automation. Do not use it to misrepresent professional activity, employment, or contributions.

## Features

- Simple command-line interface
- Strict `YYYY-MM-DD` date validation
- Configurable activity file
- Git workflow automation using Python's standard library
- Automated tests with pytest
- GitHub Actions CI on pushes and pull requests

## Requirements

- Python 3.10+
- Git

## Setup

```bash
git clone https://github.com/rudra5090/github-activity-generator.git
cd github-activity-generator
python -m pip install -r requirements.txt
```

## Usage

```bash
python activity_generator.py --date 2026-08-25
```

Invalid dates are rejected before any commit operation begins.

## Tests

```bash
python -m pytest -q
```

## Project Structure

```text
.
├── activity_generator.py
├── config.py
├── activity.txt
├── tests/
│   └── test_activity_generator.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/ci.yml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Development Workflow

1. Open an issue describing a focused change.
2. Create a feature or fix branch.
3. Make the smallest useful change.
4. Run the test suite locally.
5. Open a pull request using the PR template.
6. Let CI verify the change.
7. Review the PR before merging.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development and contribution guidelines.

## License

Released under the [MIT License](LICENSE).
