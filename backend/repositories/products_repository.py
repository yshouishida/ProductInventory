from backend.database.connection import get_connection


def get_products():
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    id,
                    code,
                    name,
                    description,
                    qty,
                    price
                FROM tblProducts
                """
            )
            return cursor.fetchall()
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn: conn.close()