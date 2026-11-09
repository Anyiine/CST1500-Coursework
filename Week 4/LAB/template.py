"""
RECORD CHECK - my version
===========================

Name  : Gideon
Lane  : Cyber
Date  : 28/10/2026
"""

# This section contains the functions

# This function calculates the difference, percentage and status
def check_record(value, limit):
    """Return the difference, percentage and status for a record."""
    difference = limit - value

    # This checks if the limit is zero
    if limit == 0:
        percent = 0
    else:
        percent = (value / limit) * 100

    # This checks if the value is over the limit
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    # This returns the calculated results
    return difference, percent, status


# This function displays the record details
def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print("\nSource IP:", label)
    print("Failed logins:", value)
    print("Total attempts:", limit)
    print("Difference:", difference)
    print("Percent:", round(percent, 2), "%")
    print("Status:", status)


# This function loads records from a file
def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []

    # This opens the file and reads each line
    with open(path, "r") as input_file:
        for line in input_file:
            label, value, limit = line.strip().split(",")

            # This stores the record details in a dictionary
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            # This adds the record to the list
            records.append(record)

    # This returns all the records
    return records


# This section stores the records

# This list contains three records with IP addresses
records = [
    {"label": "10.0.0.5", "value": 12, "limit": 10},
    {"label": "10.0.0.8", "value": 120, "limit": 100},
    {"label": "10.0.0.10", "value": 5, "limit": 20}
]


# This section processes and saves the results

# This starts counting records over the limit
over_count = 0

# This opens a file to save the results
with open("results.txt", "w") as output_file:

    # This checks each record in the list
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        # This prints the report for each record
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        # This saves the IP address and status to the file
        output_file.write(record["label"] + "," + status + "\n")

        # This counts records that are over the limit
        if status == "OVER LIMIT":
            over_count = over_count + 1


# This section shows the final summary

# This prints the total number of records over the limit
print("\nTotal records OVER LIMIT:", over_count)

# This confirms that the results were saved
print("Results saved to results.txt")