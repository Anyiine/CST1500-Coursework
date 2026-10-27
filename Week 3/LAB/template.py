
"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 2026-10-22
"""


# FUNCTIONS
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"{'Failed logins:':<20} {value:>10.2f}")
    print(f"{'Total attempts:':<20} {limit:>10.2f}")
    print(f"{'Difference:':<20} {difference:>10.2f}")
    print(f"{'Percentage:':<20} {percent:>9.2f} %")
    print(f"{'Status:':<20} {status:>10}")
    print("=" * 34)


# MAIN PROGRAM
over_limit_count = 0

while True:
    label = input("Enter source IP or type 'quit' to stop: ")

    if label.lower() == "quit":
        break

    value = float(input("Enter failed logins: "))
    limit = float(input("Enter total attempts: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1


# FINAL SUMMARY
print()
print(f"Total records OVER LIMIT: {over_limit_count}")
