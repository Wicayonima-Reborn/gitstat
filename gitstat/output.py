import json
from gitstat.colors import style, CYAN, GREEN, YELLOW

def print_human(result, args):
    print()
    print(style("Git Commit Statistics", CYAN, bold=True))
    print(style(f"Total commits: {result['total']}", GREEN, bold=True))

    if result.get("empty_messages", 0) > 0:
        print(style(
            f"Warning: {result['empty_messages']} commits have very short messages",
            YELLOW
        ))

    if not args.type_only:
        print()
        print(style("Top days:", CYAN, bold=True))
        for k, v in result["per_day"].most_common(args.limit):
            print(f"  {style(k, bold=True)}: {style(v, GREEN)}")

        print()
        print(style("Top authors:", CYAN, bold=True))
        for k, v in result["per_author"].most_common(args.limit):
            print(f"  {style(k, bold=True)}: {style(v, GREEN)}")

    print()
    print(style("Commit types:", CYAN, bold=True))
    for k, v in result["per_type"].most_common():
        print(f"  {style(k, bold=True)}: {style(v, GREEN)}")

    if args.top_messages:
        print()
        print(style("Top commit messages:", CYAN, bold=True))
        for msg, count in result["top_messages"].most_common(args.limit):
            print(f"  ({style(count, GREEN)}) {msg}")

def print_quiet(result):
    print(f"total={result['total']}")
    for k, v in result["per_type"].most_common():
        print(f"{k}={v}")
    if "per_hour" in result:
        hour, count = result["per_hour"].most_common(1)[0]
        print(f"busiest_hour={hour}")

def print_json(result):
    print(json.dumps(result, indent=2, default=int))