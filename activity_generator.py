import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from config import FILE_TO_MODIFY, COMMIT_MESSAGE


def make_change():
    """Append a real current-time UTC activity record."""
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path = Path(FILE_TO_MODIFY)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        file.write(f"Activity recorded at {timestamp}\\n")

    return path


def create_commit():
    """Commit only the activity file using the current Git timestamp."""
    activity_file = make_change()

    subprocess.run(["git", "add", "--", str(activity_file)], check=True)
    message = f"{COMMIT_MESSAGE} ({datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')})"
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
