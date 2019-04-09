import pandas as pd

# Read the csv file in
df = pd.read_csv('cities.csv')

# Save to file
df.to_html('myTable.htm')

# Assign to string
htmTable = df.to_html()