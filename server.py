from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="dbstore",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def index():

    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

    finally:
        conn.close()

    return render_template(
        "index.html",
        products=products,
        edit_product=None
    )


@app.route("/add", methods=["POST"])
def add_product():

    code = request.form["product_code"]
    name = request.form["product_name"]
    description = request.form["description"]
    qty = request.form["qty"]
    price = request.form["price"]

    conn = get_connection()

    try:
        with conn.cursor() as cursor:

            sql = """
                INSERT INTO products
                (product_code, product_name, description, qty, price)
                VALUES (%s,%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (code, name, description, qty, price)
            )

        conn.commit()

    finally:
        conn.close()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit_product(id):

    conn = get_connection()

    try:
        with conn.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM products WHERE product_id=%s",
                (id,)
            )

            product = cursor.fetchone()

            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

    finally:
        conn.close()

    return render_template(
        "index.html",
        products=products,
        edit_product=product
    )


@app.route("/update/<int:id>", methods=["POST"])
def update_product(id):

    code = request.form["product_code"]
    name = request.form["product_name"]
    description = request.form["description"]
    qty = request.form["qty"]
    price = request.form["price"]

    conn = get_connection()

    try:
        with conn.cursor() as cursor:

            sql = """
                UPDATE products
                SET
                    product_code=%s,
                    product_name=%s,
                    description=%s,
                    qty=%s,
                    price=%s
                WHERE product_id=%s
            """

            cursor.execute(
                sql,
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

    finally:
        conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_product(id):

    conn = get_connection()

    try:
        with conn.cursor() as cursor:

            cursor.execute(
                "DELETE FROM products WHERE product_id=%s",
                (id,)
            )

        conn.commit()

    finally:
        conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)