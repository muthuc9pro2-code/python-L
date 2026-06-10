class order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount

    def final_cal(self):
        return self.__total_amount - self.__discount
    
    def adminView(self):
        return {
            "customer" : self.customer_name,
            "items" : self.items,
            "amount" : self.__total_amount,
            "discount" : self.__discount,
            "final amount" : self.final_cal()
        }
    
    def customerView(self):
        return {
            "customer" : self.customer_name,
            "items" : self.items,
            "final amount" : self.final_cal()
        }
    
class adminPortal:
    def admin(self, order):
        return order.adminView()
    
class customerPortal:
    def customer(self, order):
        return order.customerView()
    
Order = order("muthu", ["pizza", "burger", "nimathi"], 600, 120)

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
    


        