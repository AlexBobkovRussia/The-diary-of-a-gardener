# Импорт модуля psycopg2
from psycopg2 import *
# Импорт переменных из файла config_db
from config_db import host, db_name, db_password, db_user, port

# try:
    # Подключение к базе данных
db_conn = connect(
    host = host,
    database= db_name,
    user= db_user,
    password = db_password,
    port = port
)

# except Exception as e:
#     # Обработка ошибок
#     print("[INFO] Ошибка при работе с PostgreSQL:", e)

# finally:
#     # Закрытие соединения с базой данных
#     if db_conn:
#         db_conn.close()
#         print(f"[INFO] Соединение с базой данных '{db_name}' закрыто.")