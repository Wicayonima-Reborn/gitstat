import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Git commit statistics tool"
    )

    parser.add_argument("--since", help="Filter commits since date or duration")
    parser.add_argument("--author", help="Filter by author name")
    parser.add_argument("--no-merge", action="store_true", help="Exclude merge commits")

    parser.add_argument("--limit", type=int, default=5, help="Limit top results")
    parser.add_argument("--type-only", action="store_true", help="Show commit types only")
    parser.add_argument("--top-messages", action="store_true", help="Show most common commit messages")

    parser.add_argument("--json", action="store_true", help="Output JSON")

    return parser.parse_args()