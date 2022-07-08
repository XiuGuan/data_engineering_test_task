import os
import psycopg2
from flask import Flask, jsonify, request, render_template
from flask_table import Table, Col

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user='postgres',
                            password='password')
    return conn


# Declare your table
class ItemTable(Table):
    month = Col('Month')
    profit = Col('Profit')
    growth_rate = Col('Growth from last month')

# Get some objects
class Item(object):
    def __init__(self, month, profit, growth_rate):
        self.month = month
        self.profit = profit
        self.growth_rate = growth_rate

@app.route('/')
def index():
    created_from = request.args.get("created_from", None)
    created_to = request.args.get("created_to", None)
    conn = get_db_connection()
    cur = conn.cursor()
    execute_sql = f"""
        WITH filtered_tbl AS (
            SELECT 
                invoice_id,
                created_date,
                due_date,
                payment_date,
                amount_to_pay_to_builder,
                amount_total,
                (amount_total - amount_to_pay_to_builder) AS profit,
                client_id,
                to_char(payment_date, 'YYYY-MM') AS payment_month
            FROM client_invoices 
            WHERE 
                created_date >= '{created_from}'
                    AND 
                created_date <= '{created_to}'
        )
        SELECT 
            payment_month,
            profit,
            COALESCE(((profit - previous_year_sales) / previous_year_sales), 0) AS growth_rate
        FROM (
            SELECT 
                payment_month,
                profit,
                LAG(profit, 1) OVER (
                    ORDER BY payment_month ASC
                ) AS previous_year_sales
            FROM (
                SELECT
                    payment_month,
                    SUM(profit) AS profit
                FROM filtered_tbl
                GROUP BY 1
            ) a
        ) b
        ;
    """
    cur.execute(execute_sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    items = [Item(x[0], "${:,.0f}".format(x[1]), "{:.1%}".format(x[2])) for x in results]


    # Populate the table
    table = ItemTable(items)

    # Print the html
    return table.__html__()

if __name__ == "__main__":
    app.run(debug=True)