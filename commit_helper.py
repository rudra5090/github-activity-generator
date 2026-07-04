import subprocess


def run_command(command):
    """
    Runs a terminal command and prints the result.
    """
    print(f"Running: {command}")

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error:")
        print(result.stderr)