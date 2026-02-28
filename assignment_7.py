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
day_full = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "F": "Friday"}
day_abbr = {"M": "Mon", "T": "Tue", "W": "Wed", "R": "Thu", "F": "Fri"}
day_order = ["M", "T", "W", "R", "F"]

course_info = input("Enter course data: ").strip()
index = 1
course_dictionary = {}

while course_info.upper() != "DONE":
    course_list = course_info.split("|")

    # Ensure 5 fields
    while len(course_list) < 5:
        course_list.append("")

    # Strip each field
    for i in range(5):
        course_list[i] = course_list[i].strip()

    course_dictionary[index] = course_list
    index += 1
    course_info = input("Enter course data: ").strip()

print()
print("=== AGGIE COURSE SCHEDULE ===")
print()

# We'll store cleaned courses here for conflicts + formatted output
clean_courses = []

for idx in course_dictionary:
    current_course = course_dictionary[idx]

    print("COURSE", f"{idx}:")
    print()

    # ---------------------------
    # Code formatting
    # ---------------------------
    class_code = current_course[0]
    class_code_clean = " ".join(class_code.replace("-", " ").upper().split())
    print("  Code:", class_code_clean)
    print()


# ============================================================
# Step 2: Title and Room Formatting
# ============================================================
course_title = current_course[1]
    course_title_clean = course_title.lower().title()
    print("  Title:", course_title_clean)
    print()

    room = current_course[4]
    room_clean = room.lower().title()
    print("  Room:", room_clean)
    print()

    # ============================================================
    # Step 3: Day Code Expansion
    # ============================================================
    days_raw = current_course[2].upper().replace(" ", "")
    full_days = []
    abbr_days = []
    day_codes = set()

    for ch in days_raw:
        if ch in day_full:
            full_days.append(day_full[ch])
            abbr_days.append(day_abbr[ch])
            day_codes.add(ch)

    days_full_text = "/".join(full_days)
    days_abbr_text = "/".join(abbr_days)

    print("  Days:", days_full_text)
    print()


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
