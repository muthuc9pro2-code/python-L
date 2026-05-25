delivery_partner = "swiggy"


def hotel():
    item = "prizza"

    def order_now():
        quantity = 2
        print(f"order placed for {quantity} {item} from {delivery_partner}")
        order_now()


hotel()

# this code is to show the variable scope example in python 