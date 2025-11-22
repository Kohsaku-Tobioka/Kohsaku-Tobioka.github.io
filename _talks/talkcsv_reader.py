import csv
import os

MONTHS = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def make_filename(year, month, day):
    return f"{year}-{MONTHS[month]}{day.zfill(2)}-talk.md"

def make_markdown(row):
    title = row["Title"]
    venue = row["Workshop/Conference venue"]
    location = ", ".join(row["Location"].split(" | "))
    day = row["Day"].zfill(2)
    year = row["Year"]
    month_num = MONTHS[row["Month"]]

    return f"""---
title: "{title}"
collection: talks
category: "workshop-conference"
permalink: /talks/{year}-{month_num}{day}-talk
venue: "{venue}"
date: {year}-{month_num}-{day}
location: "{location}"
---
**Workshop/conference**: *{venue}*, {location}. *{row["Para1"]}*

{row["Para2"]}
"""

def process_csv(csv_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # DictReader automatically uses the first row as header → no need for next()
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            filename = make_filename(row["Year"], row["Month"], row["Day"])
            content = make_markdown(row)
            out_path = os.path.join(script_dir, filename)

            with open(out_path, "w", encoding="utf-8") as md:
                md.write(content)

            print(f"Created: {filename}")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Input CSV file in the same directory as the script
input_csv = os.path.join(script_dir, 'Conf_Talk_list.csv')

# Run
process_csv(input_csv)


