import json

def print_human(result, args):
    print(f"\nTotal commits: {result['total']}\n")

    if not args.type_only:
        print("Top days:")
        for k, v in result["per_day"].most_common(args.limit):
            print(f"  {k}: {v}")

        print("\nTop authors:")
        for k, v in result["per_author"].most_common(args.limit):
            print(f"  {k}: {v}")

    print("\nCommit types:")
    for k, v in result["per_type"].items():
        print(f"  {k}: {v}")

def print_json(result):
    print(json.dumps(result, indent=2, default=int))