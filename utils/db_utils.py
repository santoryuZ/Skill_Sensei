import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def connect_to_db():
    try:
        connection = psycopg2.connect(dbname=DB_NAME,
                                      user=DB_USER,
                                      password=DB_PASSWORD,
                                      host=DB_HOST,
                                      port=DB_PORT)
        cursor = connection.cursor()
        return connection, cursor
    except ConnectionError as e:
        print("Database Connection Failed:", e)
        return None, None

def execute_query(query, values = None):
    connection, cursor = connect_to_db()
    if not connection:
        return
    try:
        cursor.execute(query, values)
        connection.commit()

    except Exception as e:
        print("Query Execution Failed:", e)
    finally:
        close_connection(connection, cursor)


def fetch_query(query, values):
    connection, cursor = connect_to_db()

    if not connection:
        return []
    try:
        cursor.execute(query, values)
        return cursor.fetchall()

    except Exception as e:
        print("Fetch Query Failed", e)
        return []
    finally:
        close_connection(connection, cursor)



def close_connection(connection, cursor):
    connection.close()
    cursor.close()
    