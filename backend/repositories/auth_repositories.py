from backend.database.connection import get_connection

def login_repo(email):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    u.id,
                    u.email,
                    u.password,
                    r.name as role
                FROM tblUser u
                INNER JOIN tblRole r
                    ON u.role_id = r.id
                WHERE email = %s
                LIMIT 1
                """,
                (email,)
            )
            return cursor.fetchone()
        
    finally:
        if conn:
            conn.close()
