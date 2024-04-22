import pyodbc


# Define the connection string
conn_str = "DRIVER={postgresql};SERVER=localhost;PORT=5432;DATABASE=postgres-test;USER=postgres;PASSWORD=postpassword"

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM information_schema.tables")

# Fetch the results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()