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
                FROM tblProduct
                """
            )
            return cursor.fetchall()
        
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
                FROM tblProduct
                WHERE id = %s
                """,
                (id,)
            )
            return cursor.fetchone()
        
    finally:
        if conn: conn.close()

def add_product_repo(code, name, description, qty, price):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tblProduct
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
        
    except Exception:
        if conn: conn.rollback()
        raise

    finally:
        if conn: conn.close()

def update_product_repo(code, name, description, qty, price, id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM tblProduct WHERE id = %s
                """,
                (id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                UPDATE tblProduct
                SET
                    code        = %s, 
                    name        = %s, 
                    description = %s, 
                    qty         = %s, 
                    price       = %s
                WHERE id        = %s
                """,
                (
                    code,
                    name,
                    description,
                    qty,
                    price, 
                    id
                )
            )
            conn.commit()

            return True
    except Exception:
        if conn: conn.rollback()
        raise

    finally:
        if conn: conn.close()


def delete_product_repo(id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM tblProduct WHERE id = %s
                """,
                (id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                DELETE FROM tblProduct WHERE id = %s
                """,
                (id,)
            )
            conn.commit()
            return True
        
    except Exception:
        if conn: conn.rollback()
        raise

    finally:
        if conn: conn.close()
