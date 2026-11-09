"""
RECORD CHECK - my version
===========================

Name  : Gideon
Lane  : Cyber
Date  : 29/10/2026
"""

# This imports pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# This section loads the records

# This reads the security records from the CSV file
df = pd.read_csv(
    r"C:\Users\HomePC\Downloads\CST1500-Coursework\Week 6\LAB\security_records.csv"
)


# This section processes the records

# This calculates the percentage of failed logins
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# This gives each record a status based on its percentage
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)


# This section displays the results

# This prints all the security records
print(df)

# This shows only records that need attention
print("\nRecords that need attention:")
print(df[df["status"] != "OK"])

# This counts the records for each status
print("\nStatus counts:")
print(df["status"].value_counts())

# This saves the full report to a CSV file
df.to_csv("security_report.csv", index=False)

# This creates a bar chart showing the status counts
df["status"].value_counts().plot(kind="bar")

# This adds a title to the chart
plt.title("Security Record Status Counts")

# This saves the chart as an image
plt.savefig("security_status.png")

# This displays the chart
plt.show()