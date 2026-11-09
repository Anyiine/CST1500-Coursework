"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 22/10/2026
"""

# This section contains the Record class
class Record:

    # This stores the record details
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label = label
        self.value = value
        self.limit = limit

    # This checks the percentage and returns the status
    def status(self):
        """Return the status of the record."""
        percent = (self.value / self.limit) * 100

        # This checks if the record is over the limit
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# This section loads records from a file
def load_records(path):
    """Read records from a file."""
    records = []

    # This opens the file and reads each line
    with open(path, "r") as file:
        for line in file:

            # This separates the record details
            label, value, limit = line.strip().split(",")

            # This creates a record object
            record = Record(label, float(value), float(limit))

            # This adds the record to the list
            records.append(record)

    # This returns all the records
    return records


# This loads the records from the text file
records = load_records("c:/Users/HomePC/Downloads/CST1500-Coursework/Week 5/LAB/records.txt")


# This section displays the results

# This starts counting records over the limit
over_limit_count = 0

# This checks each record in the list
for record in records:

    # This gets the status of the record
    status = record.status()

    # This prints the record report
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Source IP: {record.label}")
    print(f"  Failed logins: {record.value}")
    print(f"  Total attempts: {record.limit}")
    print(f"  Status: {status}")
    print("=" * 34)

    # This counts records that are over the limit
    if status == "OVER LIMIT":
        over_limit_count += 1

# This prints the final number of records over the limit
print()
print(f"Total records over limit: {over_limit_count}")