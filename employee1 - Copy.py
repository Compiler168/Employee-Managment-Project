import psycopg2

# Establish database connection
conn = psycopg2.connect(
    host='localhost',
    user='postgres',  # Default PostgreSQL username
    password='Majid345',  # Replace with your PostgreSQL password
    database='employee'  # Replace with your PostgreSQL database name
)

# Test connection
print("PostgreSQL database connected successfully")

# Don't forget to close the connection after usage
conn.close()
