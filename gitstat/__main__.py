import sys

from gitstat import __version__
from gitstat.cli import parse_args
from gitstat.gitlog import fetch_commits, NotGitRepoError
from gitstat.analyze import analyze_commits
from gitstat.output import print_human, print_json, print_quiet


def main():
    args = parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    try:
        lines = fetch_commits(args)
    except NotGitRepoError as e:
        print(str(e))
        sys.exit(1)

    if not lines:
        print("No commits found for the given filters")
        sys.exit(2)

    result = analyze_commits(lines)

    if args.quiet:
        print_quiet(result)
    elif args.json:
        print_json(result)
    else:
        print_human(result, args)


if __name__ == "__main__":
    main()