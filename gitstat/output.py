import json

def print_human(result, args):
    print(f"\nTotal commits: {result['total']}")

    if result.get("empty_messages", 0) > 0:
        print(f"Warning: {result['empty_messages']} commits have very short messages")

    if not args.type_only:
        print("\nTop days:")
        for k, v in result["per_day"].most_common(args.limit):
            print(f"  {k}: {v}")

        print("\nTop authors:")
        for k, v in result["per_author"].most_common(args.limit):
            print(f"  {k}: {v}")

    print("\nCommit types:")
    for k, v in result["per_type"].most_common():
        print(f"  {k}: {v}")

    if args.top_messages:
        print("\nTop commit messages:")
        for msg, count in result["top_messages"].most_common(args.limit):
            print(f"  ({count}) {msg}")


def print_quiet(result):
    print(f"total={result['total']}")
    for k, v in result["per_type"].most_common():
        print(f"{k}={v}")


def print_json(result):
    print(json.dumps(result, indent=2, default=int))