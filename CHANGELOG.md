# Changelog

All notable changes to this project are documented in this file.

This project follows a pragmatic versioning approach during early development (0.x.y), where minor versions may still include feature additions and UX improvements.

---

## [0.1.3] – Upcoming

### Added

* Author matching modes via `--author-mode` with support for `contains` (default), `exact`, and `regex`.
* Friendly CLI typo suggestions for mistyped flags (e.g. `--hep` → `--help`).

### Improved

* Overall CLI usability and error feedback.
* Reduced ambiguity when filtering commits by author name.

---

## [0.1.2]

### Added

* Colored human-readable output for better terminal readability.
* `--busiest-hour` option to identify the most active commit hour.

### Improved

* Output formatting and visual hierarchy.
* CLI user experience without affecting JSON or quiet modes.

---

## [0.1.1]

### Added

* `--version` flag to display the current tool version.
* `--quiet` mode for scripting and CI usage.

### Improved

* Deterministic sorting of commit type statistics.
* Meaningful exit codes for automation workflows.

---

## [0.1.0]

### Initial Release

* Basic Git commit statistics (total commits, per-day activity, top authors).
* Commit message classification (`feat`, `fix`, `chore`, `refactor`, `test`, `other`).
* Filters for author and time range (`--author`, `--since`).
* JSON output support for machine consumption.

---

## Versioning Notes

* Versions prior to `1.0.0` may include backward-compatible feature additions.
* Once the CLI stabilizes, versioning will move toward stricter semantic versioning.
