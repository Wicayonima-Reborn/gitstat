import subprocess

class NotGitRepoError(Exception):
    pass


def fetch_commits(args):
    cmd = [
        "git", "log",
        "--pretty=format:%an|%ad|%H|%s",
        "--date=format:%Y-%m-%d"
    ]

    if args.since:
        cmd.append(f"--since={args.since}")

    if args.author:
        cmd.append(f"--author={args.author}")

    if args.no_merge:
        cmd.append("--no-merges")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise NotGitRepoError("Not a git repository")

    output = result.stdout.strip()
    if not output:
        return []

    return output.splitlines()