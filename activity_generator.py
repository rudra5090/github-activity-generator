import subprocess
import argparse
from datetime import datetime
from config import FILE_TO_MODIFY


def make_change():
    """Append a timestamp to the activity file."""
    with open(FILE_TO_MODIFY, "a") as file:
        file.write(f"Commit created at {datetime.now()}\n")


def create_commit(commit_date):
    """Create a git commit using a custom date."""

    make_change()

    subprocess.run("git add .", shell=True, check=True)

    command = (
        f'git commit --date="{commit_date}" '
        f'-m "Contribution on {commit_date}"'
    )

    subprocess.run(command, shell=True, check=True)


def main():
    parser = argparse.ArgumentParser(
        description="GitHub Activity Generator"
    )

    parser.add_argument(
        "--date",
        required=True,
        help="Commit date (YYYY-MM-DD)"
    )

    args = parser.parse_args()

    commit_datetime = args.date + "T12:00:00"

    create_commit(commit_datetime)

    print("Commit created successfully!")


if __name__ == "__main__":
    main()