# git-statistics

`git-statistics` is a lightweight command-line tool for analyzing Git commit history. It provides quick insights into commit activity without requiring any external dependencies or configuration files.

The tool is designed to be simple, script-friendly, and easy to install, making it suitable for daily developer workflows, code reviews, and basic repository analytics.

## Features

* Total commit count summary
* Commit activity grouped by day
* Top contributors by commit count
* Commit message type classification (`feat`, `fix`, `chore`, `refactor`, `test`, `other`)
* Detection of very short or empty commit messages
* Most frequent commit messages
* Busiest commit hour analysis
* Filters by time range and author
* Optional JSON output for automation
* Quiet mode for scripting and CI usage

## Requirements

* Python 3.9 or newer
* Git installed and available in PATH
* Must be executed inside a Git repository

## Installation

Install from PyPI:

```bash
pip install git-statistics
```

After installation, the `git-stat` command will be available globally.

---

## Basic Usage

Run inside a Git repository:

```bash
git-stat
```

This will print a human-readable summary including total commits, top days, top authors, and commit types.

## Command Line Options

### Show help

```bash
git-stat --help
```

### Filter commits by time

```bash
git-stat --since 7d
git-stat --since 2024-01-01
```

### Filter commits by author

```bash
git-stat --author "Your Name"
```

### Exclude merge commits

```bash
git-stat --no-merge
```

### Limit output size

```bash
git-stat --limit 3
```

Limits the number of results shown for top days, authors, and messages.

### Show only commit type statistics

```bash
git-stat --type-only
```

### Show most frequent commit messages

```bash
git-stat --top-messages
```

### Show busiest commit hour

```bash
git-stat --busiest-hour
```

Outputs the hour of the day with the highest number of commits.

### JSON output

```bash
git-stat --json
```

Useful for piping into other tools or scripts.

### Quiet mode

```bash
git-stat --quiet
```

Outputs minimal key-value pairs suitable for CI and shell scripts.

### Show version

```bash
git-stat --version
```

## Exit Codes

The command exits with the following status codes:

* `0` — Successful execution
* `1` — Not a Git repository
* `2` — No commits matched the given filters

These exit codes are intended to make the tool easy to integrate into automation pipelines.

## Example Output

```text
Total commits: 124

Top days:
  2024-06-12: 15
  2024-06-10: 12

Top authors:
  Alice: 70
  Bob: 54

Commit types:
  feature: 40
  fix: 32
  chore: 18
  other: 34
```

## Design Philosophy

* No configuration files
* No external Python dependencies
* Single-purpose, focused analytics
* Predictable and script-friendly output

The tool intentionally avoids complex visualization and long-running background processes.

## License

MIT [LICENSE](LICENSE)

## Contributing

Issues and pull requests are welcome. Keep changes small, focused, and consistent with the existing CLI behavior.

