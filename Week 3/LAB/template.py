"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 2026-10-22
"""


# FUNCTIONS

# This function checks the percentage and gives a status
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# This function works out the difference and percentage
def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


# This function prints all the record details neatly
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

# I start counting records that are over the limit
over_limit_count = 0

# This loop lets me check more than one record
while True:

    # I ask the user to enter an IP address
    label = input("Enter source IP or type 'quit' to stop: ")

    # This stops the program when the user types quit
    if label.lower() == "quit":
        break

    # I ask the user to enter the login details
    value = float(input("Enter failed logins: "))
    limit = float(input("Enter total attempts: "))

    # I calculate the results and check the status
    difference, percent = check(value, limit)
    status = status_of(percent)

    # This displays the record report
    print_report(label, value, limit, difference, percent, status)

    # I add one if the record is over the limit
    if status == "OVER LIMIT":
        over_limit_count += 1


# FINAL SUMMARY

# This shows how many records were over the limit
print()
print(f"Total records OVER LIMIT: {over_limit_count}")