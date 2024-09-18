from db_config import get_db_connection

if __name__ == '__main__':
    try:
        conn = get_db_connection()

        print("Connection to SQL Server established!")

        conn.close()

    except Exception as e:
        print(f"Error: {e}")
