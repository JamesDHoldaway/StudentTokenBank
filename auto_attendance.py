"""Credit +1 'attendance' token for lessons Noto marks as Occurred.

Used by the /attendance-check routine. Reads a JSON list of sessions on stdin:
  [{"date": "2026-11-13", "time": "3:45 - 4:15pm", "name": "Alex Rivera - Voice", "status": "Occurred"}, ...]
Each session is credited at most once (tracked in attendance_log.json), so re-runs and
catch-up after missed days never double-count. Students not already in students.json are
reported, never added. Use --dry-run to preview without saving.
"""
import json
import re
import sys
import unicodedata

from bank import students, apply_rule, save_students

LOG_FILE = "attendance_log.json"
START_DATE = "2026-11-13"  # first lesson date handled automatically; earlier lessons were credited by hand


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def student_name(session_name):
    """'DUO - Sam Lee - Piano' -> 'Sam Lee'. Returns None for group classes."""
    name = session_name.strip()
    if name.lower().startswith("group"):
        return None
    name = re.sub(r"^(DUO|STAFF CHANGE|Makeup|MAKEUP)\s*[-:]\s*", "", name, flags=re.I)
    name = re.split(r"\s+-\s+", name)[0]
    return name.strip() or None


def bank_key(full_name):
    """'Chloë Park' -> matching key in students.json like 'Chloe P.', or None."""
    parts = strip_accents(full_name).split()
    if len(parts) < 2:
        return None
    # Try the first name with the initial of each later name ("Maria Jose Garcia" -> "Maria J." or "Maria G.").
    candidates = {f"{parts[0]} {p[0]}.".lower() for p in parts[1:]}
    matches = [key for key in students if strip_accents(key).lower() in candidates]
    return matches[0] if len(matches) == 1 else None


def main():
    dry_run = "--dry-run" in sys.argv
    sessions = json.load(sys.stdin)
    try:
        with open(LOG_FILE) as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []
    done = {(e["date"], e["time"], e["name"]) for e in log}

    credited, skipped, unmatched = [], [], []
    for s in sessions:
        sid = (s["date"], s["time"], s["name"])
        if s["date"] < START_DATE or s["status"] != "Occurred" or sid in done:
            continue
        full = student_name(s["name"])
        if full is None:
            skipped.append(s["name"])
            continue
        key = bank_key(full)
        if key is None:
            unmatched.append(f'{s["date"]} {s["name"]}')
            continue
        before = students[key]
        if not dry_run:
            apply_rule(key, "attendance")
        after = before + 1
        credited.append({"date": s["date"], "time": s["time"], "name": s["name"], "student": key,
                         "before": before, "after": after})
        log.append({"date": s["date"], "time": s["time"], "name": s["name"], "student": key})
        done.add(sid)

    if credited and not dry_run:
        save_students()
        with open(LOG_FILE, "w") as f:
            json.dump(log, f, indent=1)

    print(json.dumps({"dry_run": dry_run, "credited": credited, "group_skipped": skipped,
                      "not_in_bank": unmatched}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
