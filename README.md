# git-stat

Simple CLI tool to analyze git commit statistics.

## Features

* Commit count summary
* Filter by time and author
* Exclude merge commits
* Commit type classification (feat, fix, chore, etc)
* Optional JSON output

## Installation

```bash
pip install gitstat
```

## Usage

```bash
git-stat
git-stat --since 7d
git-stat --author "Your Name"
git-stat --type-only
git-stat --top-messages
git-stat --json
```

## Notes

* Must be executed inside a git repository
* Requires Git and Python >= 3.9