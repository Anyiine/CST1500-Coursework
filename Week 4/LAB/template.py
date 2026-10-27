
"""
RECORD CHECK - my version
===========================

Name  : Gideon
Lane  : Cyber
Date  : 28/10/2026
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return the difference, percentage and status for a record."""
    difference = limit - value

    if limit == 0:
        percent = 0
    else:
        percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print("\nSource IP:", label)
    print("Failed logins:", value)
    print("Total attempts:", limit)
    print("Difference:", difference)
    print("Percent:", round(percent, 2), "%")
    print("Status:", status)


def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []

    with open(path, "r") as input_file:
        for line in input_file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records


# ====================================================================== STORE

records = [
    {"label": "10.0.0.5", "value": 12, "limit": 10},
    {"label": "10.0.0.8", "value": 120, "limit": 100},
    {"label": "10.0.0.10", "value": 5, "limit": 20}
]

# =============================================================== PROCESS + OUTPUT

over_count = 0

with open("results.txt", "w") as output_file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        output_file.write(record["label"] + "," + status + "\n")

        if status == "OVER LIMIT":
            over_count = over_count + 1


# ====================================================================== SUMMARY

print("\nTotal records OVER LIMIT:", over_count)
print("Results saved to results.txt")
