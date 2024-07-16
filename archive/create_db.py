import psycopg2
from config import hostname, database, username, pwd, port_id
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 


try:
  # Connect to the existing database server
  conn = psycopg2.connect(
    host= hostname,
    user = username,
    password= pwd,
    port = port_id
  )

  conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
  cur = conn.cursor()

  # Create the new database (if it doesn't exist)
  try:
    sql = f"""CREATE DATABASE {database};"""
    cur.execute(sql)
    conn.commit()
    print(f"Database '{database}' created successfully")
  except Exception as e:
    print(f"Error creating database: {e}")

except Exception as e:
  print(f"Error connecting to database server: {e}")

finally:
  # Close the connection
    if cur is not None:
        cur.close()
    if conn:
        conn.close()
