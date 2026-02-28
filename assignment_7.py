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
    day_map_full = {
        "M": "Monday",
        "T": "Tuesday",
        "W": "Wednesday",
        "R": "Thursday",
        "F": "Friday"
    }
    day_map_abbrev = {
        "M": "Mon",
        "T": "Tue",
        "W": "Wed",
        "R": "Thu",
        "F": "Fri"
    }

    days_upper = days_raw.upper()  # Makes "mw" and "MW" behave the same
    day_letters = []
    full_days_list = []
    abbrev_days_list = []

    for ch in days_upper:
        if ch in day_map_full:
            day_letters.append(ch)
            full_days_list.append(day_map_full[ch])
            abbrev_days_list.append(day_map_abbrev[ch])

    days_full = "/".join(full_days_list)
    days_abbrev = "/".join(abbrev_days_list)

# ============================================================
# Step 4: Time Standardization
# ============================================================
    t = time_raw.replace(" ", "")          # remove unwanted spaces
    t_lower = t.lower()                   # normalize for consistent am/pm checking
    ampm = t_lower[-2:].upper()           # "am"/"pm" -> "AM"/"PM"
    clock = t[:-2]                        # keep "9:00" or "11:30"
    time_clean = clock + " " + ampm

    courses.append({
        "code": code_clean,
        "title": title_clean,
        "days_full": days_full,
        "days_abbrev": days_abbrev,
        "time": time_clean,
        "room": room_clean,
        "day_letters": day_letters
    })

    course_num += 1
    line = input("Enter course data:")
   
# Print the detailed schedule blocks
print("=== AGGIE COURSE SCHEDULE ===\n")

for i in range(len(courses)):
    c = courses[i]
    print(f"COURSE {i+1}:\n")
    print(f"  Code:  {c['code']}\n")
    print(f"  Title: {c['title']}\n")
    print(f"  Days:  {c['days_full']}\n")
    print(f"  Time:  {c['time']}\n")
    print(f"  Room:  {c['room']}\n")

print("=== SCHEDULE SUMMARY ===")
print(f"Total courses: {len(courses)}\n")

# ============================================================
# Step 5: Conflict Detection
# ============================================================
print("=== CONFLICT REPORT ===")

order = ["M", "T", "W", "R", "F"]
conflicts_found = False

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        # Same meeting time is required for a conflict
        if c1["time"] == c2["time"]:
            s1 = set(c1["day_letters"])
            s2 = set(c2["day_letters"])

            shared_letters = []
            for d in order:
                if d in s1 and d in s2:
                    shared_letters.append(d)

            if len(shared_letters) > 0:
                # Convert shared day letters to full names in correct order
                shared_full_names = []
                for d in shared_letters:
                    shared_full_names.append(day_map_full[d])

                day_text = ", ".join(shared_full_names)
                print(f"{c1['code']} and {c2['code']} conflict on {day_text} at {c1['time']}")
                conflicts_found = True

if not conflicts_found:
    print("No conflicts detected.")

print("\n=== FORMATTED FOR PRINTING ===")


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
for c in courses:
    line_out = f"{c['code']:<10}{c['title']:<26}{c['days_abbrev']:<13}{c['time']:<11}{c['room']}"
    print(line_out)
