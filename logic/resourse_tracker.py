from utils.db_utils import connect_to_db

def add_resource(resource_name, resource_type, resource_link, skill_id):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = (
                "INSERT INTO resources (resource_name, resource_type, resource_link, skill_id) "
                "VALUES (%s, %s, %s, %s);"
            )
            cursor.execute(query, (resource_name, resource_type, resource_link, skill_id))
            connection.commit()
            print("Resource added successfully.")
        except Exception as e:
            print("Failed to add resource:", e)
        finally:
            cursor.close()
            connection.close()


def list_resources():
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = (
                "SELECT r.resource_id, r.resource_name, r.resource_type, r.resource_link, "
                "s.skill_name FROM resources r "
                "JOIN skills s ON r.skill_id = s.skill_id;"
            )
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print("Failed to list resources:", e)
        finally:
            cursor.close()
            connection.close()


def update_resource(resource_id, field_to_update, new_value):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = f"UPDATE resources SET {field_to_update} = %s WHERE resource_id = %s;"
            cursor.execute(query, (new_value, resource_id))
            connection.commit()
            print("Resource updated successfully.")
        except Exception as e:
            print("Failed to update resource:", e)
        finally:
            cursor.close()
            connection.close()


def delete_resource(resource_id):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = "DELETE FROM resources WHERE resource_id = %s;"
            cursor.execute(query, (resource_id,))
            connection.commit()
            print("Resource deleted successfully.")
        except Exception as e:
            print("Failed to delete resource:", e)
        finally:
            cursor.close()
            connection.close()


def search_resource(resource_name_partial):
    connection, cursor = connect_to_db()
    if connection:
        try:
            query = (
                "SELECT r.resource_id, r.resource_name, r.resource_type, r.resource_link, "
                "s.skill_name FROM resources r "
                "JOIN skills s ON r.skill_id = s.skill_id "
                "WHERE r.resource_name ILIKE %s;"
            )
            cursor.execute(query, (f"%{resource_name_partial}%",))
            result = cursor.fetchall()
            print(result)
        except Exception as e:
            print("Failed to search resource:", e)
        finally:
            cursor.close()
            connection.close()
