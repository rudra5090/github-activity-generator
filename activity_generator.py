from datetime import datetime
import subprocess
from config import FILE_TO_MODIFY, COMMIT_MESSAGE


def make_change():
    """
    Appends the current date and time to the activity file.
    """
    with open(FILE_TO_MODIFY, "a") as file:
        file.write(f"Commit created at {datetime.now()}\n")


def git_commit():
    """
    Adds and commits the changes.
    """
    subprocess.run("git add .", shell=True)
    subprocess.run(
        f'git commit -m "{COMMIT_MESSAGE}"',
        shell=True
    )


def main():
    print("Generating activity...")

    make_change()

    git_commit()

    print("Done!")


if __name__ == "__main__":
    main()