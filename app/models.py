class Order():

    def __init__(self, orderId, contact, quantity, status):
        self.orderId = orderId
        self.contact = contact
        self.quantity = quantity
        self.status = status

    def create_order(self):
        order = {"orderId": 1, "quantity": self.quantity, "contact": self.contact,
                 "status": self.status}
        return order


class OrderList():
    def __init__(self):
        self.orderlist = []

# get all orders endpoint.
    def get_orders(self):
        return self.orderlist

# add an order endpoint
    def add_order(self, orderId, contact, quantity, status):
        if not orderId == type(int):
            raise ValueError('orderId must be an Integer.')
        if not quantity == type(int):
            raise ValueError('quantity must be an Integer.')
        if not contact == type(int) or len(contact) == 10:
            raise ValueError('contact must be an Integer of 10 digits.')
        if not status == type(str):
            raise ValueError('status must be a string.')
        order = Order(orderId, location, contact, quantity,
                      payment_mode, status).create_order()
        self.orderlist.append(order)
        return order

# get a signal order endpoint
    def get_an_order(self, orderId):
        for order in self.orderlist:
            if order['orderId'] == orderId:
                return order

# update an order.
    def update_an_order(self, orderId, status):
        for order in self.orderlist:
            if order['orderId'] == orderId:
                order['status'] = status
                return order
