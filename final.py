import sqlite3
import pandas as pd
import csv

original_conn = sqlite3.connect('feedback_data.db')

# Query the data from the original SQLite database
query = "SELECT * FROM feedback_data"
df = pd.read_sql_query(query, original_conn)
original_conn.close()

# Pivot the table
pivot_df = pd.pivot_table(df, values=['score', 'comments', 'hard'], index=['image_name'], columns=['username'], aggfunc='first')

# Flatten the multi-level columns and reset the index
pivot_df.columns = [f'{username}_{metric}' for username, metric in pivot_df.columns]
pivot_df.reset_index(inplace=True)

# Create a new DataFrame with the desired structure
new_df = pivot_df.copy()

new_conn = sqlite3.connect('new_database.db')

new_df.to_sql('new_table', new_conn, index=False, if_exists='replace')

new_conn.close()

database_file = 'new_database.db'
table_name = 'new_table'
output_file = 'output_file.csv'

# Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Execute a query to select all data from the table
cursor.execute(f"SELECT * FROM {table_name} ORDER BY image_name ASC")

# Fetch all rows
rows = cursor.fetchall()

# Get column names
columns = [description[0] for description in cursor.description]

# Write to CSV file
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)
    csv_writer.writerows(rows)

conn.close()