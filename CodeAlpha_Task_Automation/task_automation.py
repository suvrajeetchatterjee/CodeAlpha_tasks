"""
Task Automation with Python Scripts
CodeAlpha Python Programming Internship - Task 3

This script offers three small real-life automation tasks (pick any one,
or use all three via the menu):

1. Move all .jpg files from a folder to a new folder.
2. Extract all email addresses from a .txt file and save them to another file.
3. Scrape the title of a fixed webpage and save it.

Key Concepts Used: os, shutil, re, requests, file handling.
"""

import os
import re
import shutil

try:
    import requests
except ImportError:
    requests = None  # requests is only needed for option 3


# ---------------------------------------------------------------------------
# Task 3a: Move all .jpg files from a folder to a new folder
# ---------------------------------------------------------------------------
def move_jpg_files():
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid folder.")
        return

    # Create the destination folder if it doesn't already exist
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\nDone! Moved {moved_count} .jpg file(s) to '{destination_folder}'.")


# ---------------------------------------------------------------------------
# Task 3b: Extract all email addresses from a .txt file
# ---------------------------------------------------------------------------
def extract_emails():
    input_file = input("Enter the path of the .txt file to scan: ").strip()
    output_file = input("Enter the path to save extracted emails (e.g. emails.txt): ").strip()

    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    found_emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(found_emails))  # remove duplicates, sort alphabetically

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    if unique_emails:
        print(f"\nFound {len(unique_emails)} unique email address(es).")
        print(f"Saved to '{output_file}'.")
    else:
        print("No email addresses were found in the file.")


# ---------------------------------------------------------------------------
# Task 3c: Scrape the title of a fixed webpage and save it
# ---------------------------------------------------------------------------
def scrape_webpage_title():
    if requests is None:
        print("The 'requests' library is not installed.")
        print("Install it with: pip install requests")
        return

    url = input("Enter the webpage URL (e.g. https://www.example.com): ").strip()
    output_file = "webpage_title.txt"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    # Extract the <title>...</title> content using a regular expression
    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)

    if match:
        title = match.group(1).strip()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")
        print(f"\nPage title: {title}")
        print(f"Saved to '{output_file}'.")
    else:
        print("Could not find a <title> tag on that page.")


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------
def main():
    while True:
        print("\n===== Task Automation Menu =====")
        print("1. Move all .jpg files from a folder to a new folder")
        print("2. Extract email addresses from a .txt file")
        print("3. Scrape the title of a webpage")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
