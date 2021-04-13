class Sql_DB:

    def __init__(self, connect):
        self.connect = connect


    def return_len_orders(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT id FROM lc_orders_items")
        a = cursor.fetchall()
        return len(a)

    def comarison_id_order(self, param_before, param_later):
        x = param_before + 1
        assert x == param_later, f'Quntity orders {param_before} eq {param_later}'
