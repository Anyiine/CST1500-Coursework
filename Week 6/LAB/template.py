
"""
RECORD CHECK - my version
===========================

Name  : Gideon
Lane  : Cyber
Date  : 29/10/2026
"""

import pandas as pd
import matplotlib.pyplot as plt

# LOAD
df = pd.read_csv(
    r"C:\Users\HomePC\Downloads\CST1500-Coursework\Week 6\LAB\security_records.csv"
)
# PROCESS
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# OUTPUT
print(df)

# Show only records that are not OK
print("\nRecords that need attention:")
print(df[df["status"] != "OK"])

# Count records for each status
print("\nStatus counts:")
print(df["status"].value_counts())

# Save the full DataFrame
df.to_csv("security_report.csv", index=False)

# Create and save a bar chart
df["status"].value_counts().plot(kind="bar")
plt.title("Security Record Status Counts")
plt.savefig("security_status.png")
plt.show()
