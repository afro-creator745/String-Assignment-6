"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: Hakeem Cole
GitHub Username: afro-creator745
Date: 2/27/2025
Description: [What your program does]
AI Usage: [Describe any AI assistance OR write "None"]
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting
# ============================================================
courses = []
course_num = 1

line = input('Enter course data:')
while line != "DONE":
    # Split the raw input into 5 fields, then strip spaces so messy input is cleaned
    parts = line.split("|")
    code_raw = parts[0].strip()
    title_raw = parts[1].strip()
    days_raw = parts[2].strip()
    time_raw = parts[3].strip()
    room_raw = parts[4].strip()


    code_parts = code_raw.split()
    dept = code_parts[0].upper()
    num = code_parts[1]
    code_clean = dept + " " + num
# ============================================================
# Step 2: Title and Room Formatting
# ============================================================
    title_clean = title_raw.title()
    room_clean = room_raw.title()


# ============================================================
# Step 3: Day Code Expansion
# ============================================================


# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
