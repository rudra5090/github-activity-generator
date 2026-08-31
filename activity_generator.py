import argparse
import subprocess
from datetime import datetime

from config import FILE_TO_MODIFY


def make_change():
    """Append a timestamp to the activity file."""
    with open(FILE_TO_MODIFY, "a", encoding="utf-8") as file:
        file.write(f"Commit created at {datetime.now()}\n")


def validate_date(date_text):
    """Validate an ISO calendar date and return it in YYYY-MM-DD form."""
    try:
        return datetime.strptime(date_text, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "date must be a valid calendar date in YYYY-MM-DD format"
        ) from exc


def create_commit(commit_date):
    """Create a git commit using the supplied date."""
    make_change()
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(
        ["git", "commit", "--date", commit_date, "-m", f"Contribution on {commit_date}"],
        check=True,
    )


def main():
    parser = argparse.ArgumentParser(description="GitHub Activity Generator")
    parser.add_argument(
        "--date",
        required=True,
        type=validate_date,
        help="Commit date (YYYY-MM-DD)",
    )
    args = parser.parse_args()

    commit_datetime = f"{args.date}T12:00:00"
    create_commit(commit_datetime)
    print("Commit created successfully!")


if __name__ == "__main__":
    main()
