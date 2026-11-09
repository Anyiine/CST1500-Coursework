"""
RECORD CHECK - my version
===========================

Name  : Gideon
Lane  : Cyber
Date  : 29/10/2026
"""

# This section contains the functions

# This function cleans a messy security record
def parse_line(raw_line):
    """Clean a security record and return a dictionary."""

    # This removes spaces and changes the text to lowercase
    raw_line = raw_line.strip().lower()

    # This splits the record into separate parts
    parts = raw_line.split(",")

    # This creates an empty dictionary
    record = {}

    # This checks each part of the record
    for part in parts:

        # This separates the key and value
        key, value = part.split("=")

        # This removes extra spaces
        key = key.strip()
        value = value.strip()

        # This changes attempts into a number
        if key == "attempts":
            value = int(value)

        # This adds the cleaned details to the dictionary
        record[key] = value

    # This returns the cleaned record
    return record


# This function checks the login result
def status_of(record):
    """Return the status of a security record."""

    # This checks if the login failed
    if record["result"] == "failed":
        return "FLAGGED"
    else:
        return "OK"


# This section loads the security records

# This creates an empty list
raw_records = []

# This opens the security records file from Week 7
with open("Week 7/LAB/security_records.txt", "r") as file:

    # This reads each line from the file
    for line in file:
        raw_records.append(line)


# This section processes and displays the results

# This starts counting all records
total_records = 0

# This starts counting flagged records
flagged_count = 0

# This checks every security record
for raw_record in raw_records:

    # This cleans the record
    record = parse_line(raw_record)

    # This checks the record status
    status = status_of(record)

    # This prints the cleaned record and status
    print("\nRecord:", record)
    print("Status:", status)

    # This counts the records
    total_records += 1

    # This counts failed login records
    if status == "FLAGGED":
        flagged_count += 1


# This section displays the final summary

# This prints the total records and flagged records
print("\nTotal records:", total_records)
print("Flagged records:", flagged_count)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
