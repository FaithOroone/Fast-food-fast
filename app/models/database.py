import psycopg2
import os


class DatabaseConnection:
    def __init__(self):
        try:

            postgresdb = 'fast_food_fast'
            if os.getenv('APP_VAR') == 'testing':
                postgresdb = 'fast-food-fast-testing'
            print(os.getenv('APP_VAR'))
            print(postgresdb)

            self.connection = psycopg2.connect(
                dbname='df9dd94m13r0sd', user='opdceyzerkijjs', password='d0f6de1a81591f70b184e446e3f97d130f981af08d94cb12c760c604bc048968',
                host='ec2-54-243-147-162.compute-1.amazonaws.com', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("connected!!")

        except:
            print("Failed to connect to the database")

    def create_tables(self):
        create_user_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id serial primary key, user_name TEXT NOT NULL, email VARCHAR NOT NULL, user_password VARCHAR(99) NOT NULL, is_admin Boolean NOT NULL);"
        self.cursor.execute(create_user_table)

        create_menu = " CREATE TABLE IF NOT EXISTS menu\
        (menu_id serial primary key, menu_item text NOT NULL, price integer);"
        self.cursor.execute(create_menu)

        create_order = "CREATE TABLE IF NOT EXISTS orders\
        (order_id serial primary key, user_id integer references users(user_id), menu_id integer references menu(menu_id), contact integer NOT NULL, quantity int NOT NULL, order_status text NOT NULL);"
        self.cursor.execute(create_order)

    def create_user(self, user_name, email, user_password):
        self.cursor.execute(
            "SELECT *FROM users WHERE user_name =%s", [user_name])
        check_user = self.cursor.fetchone()
        if check_user:
            return "username exists"
        query = "INSERT INTO users(user_name, email, user_password, is_admin)\
        VALUES('{}','{}','{}', False);".format(user_name, email, user_password)
        self.cursor.execute(query)

    def auto_admin(self):
        query = "UPDATE users SET is_admin = True WHERE user_id = 1;"
        self.cursor.execute(query)

    def create_menu(self, menu_item, price):
        query = "INSERT INTO menu(menu_item, price)\
        VALUES('{}','{}');".format(menu_item, price)
        self.cursor.execute(query)

    def create_order(self, user_id, menu_id, contact, quantity, order_status):
        query = "INSERT INTO orders(user_id, menu_id, contact, quantity, order_status)\
        VALUES('{}','{}','{}','{}', '{}');".format(user_id, menu_id, contact,
                                                   quantity, order_status)
        self.cursor.execute(query)

    # get a user
    def get_a_user(self, column, value):
        query = "SELECT * FROM users WHERE {} = '{}';".format(column, value)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    # get all orders
    def get_all_orders(self):
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        order = []
        for row in rows:
            row = {'user_id': row[0], 'menu_id': row[1], 'contact': row[2],
                   'quantity': row[3], 'order_status': row[4]}
            order.append(row)
        return order

    # get a signle order
    def get_an_order(self, column, value):
        query = " SELECT * FROM orders WHERE {} = '{}';".format(column=value)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    # update order status
    def update_order_status(self, order_status, order_id):
        query = "UPDATE orders SET order_status='{}' WHERE order_id='{}';".format(
            order_status, order_id)
        self.cursor.execute(query)
        return order_status

    # get order history.
    def get_order_history(self, user_id):
        query = "SELECT * FROM orders WHERE user_id = '{}';".format(user_id)
        self.cursor.execute(query)
        history = self.cursor.fetchall()
        return history

    # Get available menu
    def get_menu(self):
        query = "SELECT * FROM menu"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        menu = []
        for row in rows:
            row = {'menu_id': row[0], 'menu_item': row[1], 'price': row[2]}
            menu.append(row)
        return menu
# "DROP TABLE orders; DROP TABLE menu

    def drop_table(self):
        query = "DROP TABLE users CASCADE;"
        self.cursor.execute(query)
        return "Droped"

    # make an admin
    def make_admin(self):
        query = "UPDATE users SET is_admin = {} WHERE user_id = '{}';\
        ".format(True, 1)
        self.cursor.execute(query)


DatabaseConnection().create_tables()
DatabaseConnection().auto_admin()
DatabaseConnection().make_admin()
