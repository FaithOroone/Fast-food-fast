class Order():

    def __init__(self,orderId, location, contact, quantity, payment_mode, status):
        self.orderId = orderId
        self.location = location
        self.contact = contact
        self.quantity = quantity
        self.payment_mode = payment_mode
        self.status = status

    def create_order(self):
        order = {"orderId": 1, "quantity": self.quantity, "contact": self.contact, "payment_mode":self.payment_mode, "status":self.status}
        return order

class OrderList():
    # {'orderId': 1, 'quantity': 5, 'contact': 'faith@gmail.com','payment_mode':'C.O.D'},{'orderId': 2, 'quantity': 5, 'contact': 'faith1@gmail.com','payment_mode':'C.O.D'}
    def __init__(self):
        self.orderlist = []

    def get_orders(self):
        return self.orderlist

    def add_order(self, orderId, location, contact, quantity, payment_mode, status):
        order = Order(orderId, location, contact, quantity, payment_mode, status).create_order()
        self.orderlist.append(order)
        return order


    def get_an_order(self, orderId):
        for order in self.orderlist:
            if order['orderId']==orderId:
                return order