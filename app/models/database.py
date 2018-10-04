import psycopg2
import os


class DatabaseConnection:
    def __init__(self):
        try:

            postgresdb='fast_food_fast'
            if os.getenv('APP_VAR')=='testing':
                postgresdb='fast-food-fast-testing'
            print(os.getenv('APP_VAR'))
            print(postgresdb)



            self.connection = psycopg2.connect(
                dbname=postgresdb, user='postgres', password='12345@kerenagemo', \
                host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("connected!!")

        except:
            print("Failed to connect to the database")

    def create_tables(self):
        create_user_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id serial primary key, user_name VARCHAR NOT NULL, email VARCHAR NOT NULL, user_password VARCHAR(99) NOT NULL, is_admin Boolean NOT NULL);"
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
        order = self.cursor.fetchall()
        return order

    # get a signle order
    def get_an_order(self, order_id):
        query = "SELECT * FROM orders WHERE order_id = '{}';".format(order_id)
        self.cursor.execute(query)
        order = self.cursor.fetchone()
        return order

    # update order status

    def update_order_status(self, order_status, order_id):
        query = "UPDATE orders SET order_status='{}' WHERE order_id='{}';".format(
            order_status, order_id)
        self.cursor.execute(query)
        return order_status

    # Get available menu
    def get_menu(self):
        query = "SELECT * FROM menu"
        self.cursor.execute(query)
        menu = self.cursor.fetchall()
        return menu

    # get all users
    def get_all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            print({'user_id': row[0], 'user_name': row[1],
                   'email': row[2], 'user_password': row[3]})
        return users

    # def drop_table(self):
    #     	query = "DROP TABLE users;DROP TABLE menu;DROP TABLE order;"
    #     self.cursor.execute(query)
    #     return "Droped"

DatabaseConnection()
# DatabaseConnection().auto_admin()
