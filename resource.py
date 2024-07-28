import mysql.connector
from mysql.connector import Error

def test_connection(server_name, server_username, server_password):
    try:
        connection = mysql.connector.connect(
            host=server_name,
            user=server_username,
            password=server_password
        )
        if connection.is_connected():
            return f"Connected to {server_name} successfully!"
        else:
            return f"Failed to connect to {server_name}."
    except Error as e:
        return f"Error: {e}"
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
