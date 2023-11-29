import sqlite3
import pandas as pd

# Connect to the original SQLite database
original_conn = sqlite3.connect('feedback_data.db')  # Replace 'feedback_data.db' with your actual original database file

# Query the data from the original SQLite database
query = "SELECT * FROM feedback_data"  # Replace 'feedback_data' with your actual table name in the original database
df = pd.read_sql_query(query, original_conn)

# Close the connection to the original database
original_conn.close()

# Pivot the table
pivot_df = pd.pivot_table(df, values=['score', 'comments'], index=['image_name'], columns=['username'], aggfunc='first')

# Flatten the multi-level columns and reset the index
pivot_df.columns = [f'{username}_{metric}' for username, metric in pivot_df.columns]
pivot_df.reset_index(inplace=True)

# Create a new DataFrame with the desired structure
new_df = pivot_df.copy()

# Connect to the new SQLite database
new_conn = sqlite3.connect('new_database.db')

# Save the new table to a new SQLite table in the new database
new_df.to_sql('new_table', new_conn, index=False, if_exists='replace')

# Close the connection to the new database
new_conn.close()