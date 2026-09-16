from backend.database.connection import get_connection

def login_repo(username):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    id,
                    username,
                    password,
                    role
                FROM tblUsers
                WHERE username = %s
                LIMIT 1
                """,
                (username,)
            )
            return cursor.fetchone()
        
    finally:
        if conn:
            conn.close()
