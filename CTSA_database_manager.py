import pandas as pd
import sqlite3

df = pd.read_csv('CTSA_cleaned_sample.csv')

# connecting to SQLite database
connection = sqlite3.connect('cyber_security_logs.db')
cursor = connection.cursor()

print("Database connection established.")

# loading DataFrame into SQL table
# call table 'network_traffic'
print("Migrating data to SQL")
df.to_sql('network_traffic', connection, if_exists='replace', index=False)

# verification query (table exists and has data)
cursor.execute("SELECT COUNT(*) FROM network_traffic")
count = cursor.fetchone()[0]

print(f"Successfully Created SQL table 'network_traffic' with {count:,} records.")

connection.close()
