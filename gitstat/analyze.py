from collections import Counter

EMPTY_MSG_LIMIT = 5

def classify_message(message: str) -> str:
    msg = message.lower()
    if msg.startswith("feat"):
        return "feature"
    if msg.startswith("fix"):
        return "fix"
    if msg.startswith("chore"):
        return "chore"
    if msg.startswith("refactor"):
        return "refactor"
    if msg.startswith("test"):
        return "test"
    return "other"

def analyze_commits(lines):
    per_day = Counter()
    per_author = Counter()
    per_type = Counter()
    messages = Counter()

    empty_messages = 0

    for line in lines:
        author, date, message = line.split("|", 2)

        per_day[date] += 1
        per_author[author] += 1
        per_type[classify_message(message)] += 1

        clean_msg = message.strip()
        if len(clean_msg) < EMPTY_MSG_LIMIT:
            empty_messages += 1
        else:
            messages[clean_msg] += 1

    return {
        "total": len(lines),
        "per_day": per_day,
        "per_author": per_author,
        "per_type": per_type,
        "top_messages": messages,
        "empty_messages": empty_messages,
    }