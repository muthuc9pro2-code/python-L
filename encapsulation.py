class order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def final_cal(self):
        return self.__total_amount - self.__discount
    
    def get_adminView(self):
        return {
            "customer" : self.customer_name,
            "items" : self.items,
            "total" : self.__total_amount,
            "discount" : self.__discount,
            "final_total" : self.final_cal()
        }
    
    def get_customerView(self):
        return {
            "customer" : self.customer_name,
            "items" : self.items,
            "final_total" : self.final_cal()
        }
    
class adminPortal:
    def admin(self, order):
        print(order.get_adminView())

class customerPortal:
    def customer(self, order):
        print(order.get_customerView())

Order = order("muthu", "nimathi", 1000, 232)

admin = adminPortal()
customer = customerPortal()

def printAdmin():
    print("adminView")
    print(admin.admin(Order))

def printCustomer():
    print("customerView")
    print(customer.customer(Order))

printAdmin()
printCustomer()
        