
"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 22/10/2026
"""

# CLASS
class Record:
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status of the record."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# LOAD RECORDS
def load_records(path):
    """Read records from a file."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


# RECORDS
records = load_records("c:/Users/HomePC/Downloads/CST1500-Coursework/Week 5/LAB/records.txt")


# OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Source IP: {record.label}")
    print(f"  Failed logins: {record.value}")
    print(f"  Total attempts: {record.limit}")
    print(f"  Status: {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Total records over limit: {over_limit_count}")
