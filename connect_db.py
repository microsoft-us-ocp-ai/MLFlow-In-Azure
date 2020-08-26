import psycopg2, os, json
from settings import (PG_DB_URI, PG_DBNAME, PG_SERVER_HOST, 
                      PG_USER_PASSWORD, PG_USER)


# Update connection string information 
host = PG_SERVER_HOST
dbname = PG_DBNAME
user = PG_USER
password = PG_USER_PASSWORD
sslmode = "require"

# Construct connection string
conn_string = f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}"
conn = psycopg2.connect(conn_string) 
print("Connection established")

#use cursor to wrap the connection and send commands
cursor = conn.cursor()

# Check the list of databases within the PG server
cursor.execute("SELECT datname from pg_database;")
rows=cursor.fetchall()
print("Here are the databases:\n",rows)

# This will auto check if "mlflow" exists
if [True for x in rows if "mlflow" in x[0] ][0]:
    print("mlflow database exists")
    pass
else:
    # If mlflow database does not exist, create it
    print("mlflow database does not exist")
    cursor.execute("create database mlflow")

# Clean up
conn.commit()
cursor.close()
conn.close()