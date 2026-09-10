from backend.database.connection import get_connection


def get_products_repo():
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

def get_by_id_repo(id):
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
                WHERE id = %s
                """,
                (id,)
            )
            return cursor.fetchone()
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn: conn.close()

def add_product_repo(code, name, description, qty, price):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tblProducts
                    (code, name, description, qty, price)
                VALUES
                    (%s, %s, %s, %s, %s)
                """,
                (
                    code, name, description, qty, price
                )
            )
            conn.commit()
            return True
        
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")

    finally:
        if conn: conn.close()