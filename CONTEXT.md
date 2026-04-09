# Project context — HCDE 530 Week 2

Human-facing notes for anyone opening this folder (instructor, classmates, or future you). The author is an **HCD practitioner** (UX research / UX design), not a software engineer; the code is intentionally small and readable.

## What this project is trying to show

- **Process a data file end-to-end:** load structured text from a CSV, compute a simple quantitative summary, and present results in the terminal and optionally in a browser.
- **Make the “important bits” easy to find** without cluttering the script: this file maps **each section of `demo_word_count.py` to its purpose**. Prefer reading here first, then skim the code.

## What readers should be able to do

1. **Run the Python script** from a terminal and read the printed table and summary.
2. **Open `dashboard.html` in a browser** to explore the same dataset visually (filters, search, charts).
3. **Run `count_words.py`** on the separate **app-reviews** exercise (`reviews.csv`): summary only (shortest, longest, average word count).

No servers or extra packages are required for that path.

## Dataset — how to talk about it

- **`reviews.csv`** holds **made-up app store–style reviews** (50 rows) for practicing the same word-count pattern on different content. Not real user feedback.
- **`demo_responses.csv` is fully fictional** demo material created for class.
- Text is **paraphrased from real professional themes** (research handoffs, synthesis fatigue, org dynamics, etc.) but **does not quote real participants** and should not be treated as empirical findings.
- Treat it as a **teaching stub** for pipeline practice, not publishable research data.

## How to interpret “word count” here

Word count is a coarse **effort / verbosity signal**: how much each person wrote before you read closely. It does **not** measure insight, quality, or theme density. In real research you would pair this kind of metric with qualitative coding and context.

**Definition used in code:** split the response string on whitespace and count the pieces (`len(response.split())` in Python). The dashboard uses the same idea so numbers stay aligned.

## Run the script

From this project folder:

```bash
cd "/path/to/HCDE 530 Week 2 Project"
python3 demo_word_count.py
python3 count_words.py
```

Each script expects its CSV in the **current working directory** (same folder you run the command from): `demo_responses.csv` for `demo_word_count.py`, `reviews.csv` for `count_words.py`.

## View the dashboard

Double-click `dashboard.html` or open it from the browser’s File menu. The page embeds a copy of the survey rows as JSON so it works as a local file without a web server.

**If you edit the CSV:** update the embedded data in `dashboard.html` (or regenerate that page) so charts and tables stay in sync with `demo_responses.csv`.

## `demo_word_count.py` — section-by-section map

| Lines (approx.) | What it does | Why it matters |
|-----------------|--------------|----------------|
| 1–2 | Shebang-style comment + `import csv` | States intent; uses only the standard library. |
| 4–6 | `filename` + empty `responses` list | Separates **configuration** (which file) from logic; list will hold one dict per row. |
| 8–11 | `open` + `csv.DictReader` + loop | **Core ingestion:** `newline=""` avoids subtle CSV bugs on some OSes; `encoding="utf-8"` handles smart quotes and apostrophes; `DictReader` uses the header row as keys (`participant_id`, `role`, `response`). |
| 14–15 | Print header row + separator | Human-readable table layout in the terminal. |
| 17–30 | Loop: extract fields, word count, preview, print | **Core transform + output:** `split()` defines “word”; `word_counts` stores counts for the summary; preview truncates long text for the terminal. |
| 32–38 | Summary block | Aggregates the per-row counts: count of responses, min, max, mean. |

## Design choices (constraints)

There are **no hard course constraints** on tooling; this repo stays **stdlib-only** and **static HTML** on purpose so installation and grading stay simple.

## Related files

| File | Role |
|------|------|
| `demo_responses.csv` | Source table (survey) |
| `demo_word_count.py` | CLI processing and summary for survey CSV |
| `reviews.csv` | Fictional app reviews for `count_words.py` |
| `count_words.py` | Word-count summary (min / max / average) for `reviews.csv` |
| `dashboard.html` | Visual exploration of survey data |
| `week2.md` | Week 2 written reflection on Competency 2 (code literacy & documentation) |
| `.cursorrules` | Hints for AI assistants working in this folder (optional for human readers) |

---

*Update this document if the assignment brief, data story, or file layout changes.*
