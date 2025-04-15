import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port,ssl):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            sslmode=ssl
        )
        print("Подключение к PostgreSQL успешно")
    except OperationalError as e:
        print(f"Произошла ошибка '{e}'")
    return connection

# Использование
connection = create_connection(
    "test_db", "admin_db", "RfYbjdienWE", "85.235.205.239", "5432", "require"
)
