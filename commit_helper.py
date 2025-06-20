import subprocess


def run_command(command):
    """
    Execute a shell command.

    Args:
        command (list): Command to execute.
    """

    result = subprocess.run(
        command,
        text=True,
        capture_output=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)