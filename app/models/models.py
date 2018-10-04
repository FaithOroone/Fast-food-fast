class Users():
    def __init__(self, user_id, user_name, email, password, is_admin):
        self.user_id = 0
        self.user_name = user_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

class Menu():
    def __init__(self, menu_id, menu_item, price):
        self.menu_id = 0
        self.menu_item = menu_item
        self.price = price

class Order():
    def __init__(self, user_id,menu_id, contact, quantity, order_status):
        self.user_id = user_id
        self.menu_id = menu_id
        self.contact = contact
        self.quantity = quantity
        self.order_status = order_status
