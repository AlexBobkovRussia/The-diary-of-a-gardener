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
# id BIGINT NOT NULL PRIMARY KEY,
    cur.execute('''ALTER TABLE users
                ADD login VARCHAR() NOT NULL;
                ADD password VARCHAR() NOT NULL''')

except:
    print("Database not connected successfully")

finally:
    if conn:
        cur.close()
        conn.close()
        print(f"[INFO] Соединение с базой данных '{conn}' закрыто.")
