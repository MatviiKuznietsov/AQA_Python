import csv

file1 = "random-michaels.csv"
file2 = "random.csv"
result_file = "result.csv"

rows = set()

for file in [file1, file2]:
    with open(file, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.add(tuple(row))

with open(result_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)