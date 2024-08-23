# Импорт модуля psycopg2
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
    conn.autocommit = True
    print("Database connected successfully")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE seeds (
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(100),
                       variety VARCHAR(100),
                       quantity INTEGER,
                       planting_date DATE,
                       notes TEXT
);
''')

except:
    print("Database not connected successfully")

finally:
    if conn:
        cur.close()
        conn.close()
        print(f"[INFO] Соединение с базой данных '{conn}' закрыто.")
