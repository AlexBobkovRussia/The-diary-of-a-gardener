from psycopg2 import *
 
DB_NAME = "Users"
DB_USER = "postgres"
DB_PASS = "asdfvcxz16022011"
DB_HOST = "localhost"
DB_PORT = "5432"
 
try:
    conn = connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")
    