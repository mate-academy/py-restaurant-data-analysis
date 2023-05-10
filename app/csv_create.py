import csv
import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

query = """
    SELECT o.id, o.datetime, p.name, p.price, oi.quantity, (p.price * oi.quantity) AS total
    FROM restaurant_order o
    LEFT JOIN restaurant_orderitem AS oi ON o.id = oi.order_id
    LEFT JOIN restaurant_product AS p ON oi.product_id = p.id
    """
cursor.execute(query)


rows = cursor.fetchall()


output_file = "output.csv"

with open(output_file, "w") as csvfile:
    csv_writer = csv.writer(csvfile)

    header = ["id", "datetime", "name", "price", "quantity", "total"]
    csv_writer.writerow(header)

    csv_writer.writerows(rows)

conn.close()
