
"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 2026-10-22
"""

over_limit_count = 0

while True:
    # INPUT
    label = input("Enter source IP or type 'quit': ").strip()

    if label.lower() == "quit":
        break

    failed_logins = float(input("Enter failed logins: "))
    total_attempts = float(input("Enter total attempts: "))

    # PROCESS
    difference = total_attempts - failed_logins
    percent = (failed_logins / total_attempts) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        over_limit_count += 1

    # OUTPUT
    print()
    print("=" * 40)
    print(f"  RECORD CHECK - {label}")
    print("=" * 40)
    print(f"Failed logins : {failed_logins:10.2f}")
    print(f"Total attempts: {total_attempts:10.2f}")
    print(f"Difference    : {difference:10.2f}")
    print(f"Failed percent: {percent:9.2f} %")
    print(f"Status        : {status:>10}")
    print("=" * 40)

print()
print(f"Total records marked OVER LIMIT: {over_limit_count}")
