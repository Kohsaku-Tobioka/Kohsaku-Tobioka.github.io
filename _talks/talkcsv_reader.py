import csv
import os

# Mapping of month names to numbers
month_to_number = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

# Function to generate the filename based on the date
def generate_filename(year, month, day):
    month_number = month_to_number[month]
    return f"{year}-{month_number.zfill(2)}{day.zfill(2)}-talk.md"

# Function to create the content of the markdown file
def create_markdown_content(data):
    title, venue, location, day, month, year, text1, text2 = data[1:]
    month_number = month_to_number[month]
    date = f"{year}-{month_number.zfill(2)}-{day.zfill(2)}"
    location_formatted = ", ".join(location.split(" | "))
    content = f"""---
title: "{title}"
collection: talks
category: "workshop-conference"
permalink: /talks/{year}-{month_number.zfill(2)}{day.zfill(2)}-talk
venue: "{venue}"
date: {date}
location: "{location_formatted}"
---
**Workshop/conference**: *{venue}*, {location_formatted}. *{text1}*

{text2}
"""
    return content

# Function to read the CSV and process a specific line
def process_csv(input_file, talk_number):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == str(talk_number):
                # Extract the required fields
                day, month, year = row[4], row[5], row[6]
                # Generate filename and content
                filename = generate_filename(year, month, day)
                content = create_markdown_content(row)
                
                # Write to the markdown file in the same directory as the script
                output_path = os.path.join(script_dir, filename)
                with open(output_path, 'w', encoding='utf-8') as mdfile:
                    mdfile.write(content)
                print(f"Markdown file '{filename}' has been created.")
                return

    print(f"Talk number {talk_number} not found in the CSV file.")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Input CSV file in the same directory as the script
input_csv = os.path.join(script_dir, 'Conf_Talk_list.csv')

# Process the CSV file for talk numbers 1 to 41
for talk_number in range(1, 42):
    process_csv(input_csv, str(talk_number))
