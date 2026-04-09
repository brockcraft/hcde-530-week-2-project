"""Read app reviews from CSV and summarize word counts per review."""

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent / "reviews.csv"


def word_count(text: str) -> int:
    return len(text.split()) if text.strip() else 0


def main() -> None:
    reviews: list[tuple[str, str, int]] = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rid = row["review_id"]
            text = row["text"]
            reviews.append((rid, text, word_count(text)))

    if not reviews:
        print("No reviews found.")
        return

    counts = [c for _, _, c in reviews]
    shortest = min(reviews, key=lambda x: x[2])
    longest = max(reviews, key=lambda x: x[2])
    avg = sum(counts) / len(counts)

    print(f"Loaded {len(reviews)} reviews from {CSV_PATH.name}\n")
    print("── Word count summary ──")
    print(f"  Shortest : {shortest[2]} words  ({shortest[0]})")
    print(f"  Longest  : {longest[2]} words  ({longest[0]})")
    print(f"  Average  : {avg:.1f} words")
    print()
    print("Shortest review text:")
    print(f"  {shortest[1][:200]}{'…' if len(shortest[1]) > 200 else ''}")
    print()
    print("Longest review text:")
    print(f"  {longest[1][:200]}{'…' if len(longest[1]) > 200 else ''}")


if __name__ == "__main__":
    main()
