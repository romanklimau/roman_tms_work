import mysql.connector as mysql


class Sql_DB:

    def connect(self):
        db_conn = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database='db_litecart'
        )
        return db_conn

    def return_len_orders(self, connect):
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM lc_orders_items")
        a = cursor.fetchall()
        return len(a)

    def comarison_id_order(self, param_before, param_later):
        x = param_before + 1
        assert x == param_later, f'Quntity orders {param_before} eq {param_later}'
