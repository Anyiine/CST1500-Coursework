
"""
RECORD CHECK - my version

Name: Gideon
Lane: Cyber
Date: 22/10/2026
"""

# INPUT
source_ip = input("Enter source IP: ")
failed_logins = float(input("Enter failed logins: "))
total_attempts = float(input("Enter total attempts: "))


# PROCESS
difference = total_attempts - failed_logins
percent = (failed_logins / total_attempts) * 100

# This shows how many attempts did not fail, which helps
# us understand how many attempts were not failed logins.
successful_attempts = total_attempts - failed_logins


# OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK - {source_ip}")
print("=" * 34)

print(f"  Failed logins : {failed_logins:>10.2f}")
print(f"  Total attempts: {total_attempts:>10.2f}")
print(f"  Difference    : {difference:>+10.2f}")
print(f"  Failed percent: {percent:>9.2f} %")
print(f"  Other attempts: {successful_attempts:>10.2f}")

print("=" * 34)
