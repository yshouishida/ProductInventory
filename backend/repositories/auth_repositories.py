from backend.database.connection import get_connection

def login_repo(username):
    conn  = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    id,
                    username,
                    password
                WHERE username = %s
                LIMIT 1
                """,
                (username,)
            )
            return cursor.fetchone()
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn: conn.close()