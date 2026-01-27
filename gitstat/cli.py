import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple git commit statistics tool"
    )
    parser.add_argument("--since", help="Filter commits since date or duration")
    parser.add_argument("--author", help="Filter by author name")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--limit", type=int, default=5, help="Limit top results")
    parser.add_argument("--type-only", action="store_true", help="Show commit type stats only")
    parser.add_argument("--no-merge", action="store_true", help="Exclude merge commits")
    return parser.parse_args()