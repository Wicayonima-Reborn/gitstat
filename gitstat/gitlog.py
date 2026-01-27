import subprocess
import sys

def fetch_commits(args):
    cmd = [
        "git", "log",
        "--pretty=format:%an|%ad|%s",
        "--date=short"
    ]

    if args.since:
        cmd.append(f"--since={args.since}")
    if args.author:
        cmd.append(f"--author={args.author}")
    if args.no_merge:
        cmd.append("--no-merges")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        sys.exit("Error: not a git repository")

    return result.stdout.splitlines()