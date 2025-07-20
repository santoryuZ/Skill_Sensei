import psycopg2
from utils.db_utils import connect_to_db

from utils.db_utils import connect_to_db

def add_skill(skill_name,  proficiency_level, target_level, start_date, target_date):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = (
                "INSERT INTO skills (skill_name, proficiency_level, target_level, start_date, target_date) "
                "VALUES (%s, %s, %s, %s, %s);"
            )
            cursor.execute(query, (skill_name,  proficiency_level, target_level, start_date, target_date))
            connection.commit()
            print("Skill added successfully.")
        except Exception as e:
            print("Failed To Add Skill:", e)
        finally:
            cursor.close()
            connection.close()


def list_skills():
    connection, cursor = connect_to_db()
    if connection:
        try:
            cursor.execute("SELECT * FROM skills;")
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print("Failed To List Skills", e)
        finally:
            cursor.close()
            connection.close()

def update_skill(skill_name, field_to_update, new_value):
    connection, cursor = connect_to_db()
    query = (f"UPDATE skills "
             f"SET {field_to_update} = %s "
             f"WHERE skill_id = %s;")

    if connection:
        try:
            cursor.execute(query, (new_value, skill_name))
            connection.commit()
        except Exception as e:
            print("Failed To Update Skills", e)
        finally:
            cursor.close()
            connection.close()


def delete_skill(skill_name):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = "DELETE FROM skills WHERE skill_name = %s"
            cursor.execute(query, (skill_name,))
            connection.commit()
            print("Skill Deleted successfully.")
        except Exception as e:
            print("Failed To Delete Skill:", e)
        finally:
            cursor.close()
            connection.close()

def search_skill(skill_name):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = ("SELECT * FROM skills "
                     "WHERE skill_name ILIKE %s;")
            cursor.execute(query, (f"%{skill_name}%",))
            result = cursor.fetchall()
            print(result)
        except Exception as e:
            print("Failed To Search Skills", e)
        finally:
            cursor.close()
            connection.close()

def get_skill_id_by_name(skill_name):
    connection, cursor = connect_to_db()
    if connection:
        try:
            cursor.execute("SELECT skill_id FROM skills WHERE skill_name = %s;", (skill_name,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print("Error getting skill ID:", e)
        finally:
            cursor.close()
            connection.close()
    return None