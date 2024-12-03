import csv

input_file = "1.csv"
output_file = "2.csv"


with open(input_file, mode="r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    
    filtered_rows = [row for row in reader if row.get("Popularity") and int(row["Popularity"]) >= 97]
    
    with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

print("done")