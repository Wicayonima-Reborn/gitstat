import sys

def supports_color():
    return sys.stdout.isatty()

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

def style(text, color="", bold=False):
    if not supports_color():
        return text
    prefix = ""
    if bold:
        prefix += BOLD
    if color:
        prefix += color
    return f"{prefix}{text}{RESET}"
