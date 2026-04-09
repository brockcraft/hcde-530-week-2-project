# A script to process and count words in a CSV file.
# Section-by-section walkthrough: see CONTEXT.md
import csv

# Load the CSV file
filename = "demo_responses.csv"
responses = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        responses.append(row)

# Count words in each response and print a row-by-row summary for readable output
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

# Loop through each row in the responses and count the words
for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    # Split on whitespace to count words
    count = len(response.split())
# append the count to the word_counts list
    word_counts.append(count)

    # Truncate the response for display
    preview = response[:60] + "..." if len(response) > 60 else response
    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

# Print summary statistics
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
