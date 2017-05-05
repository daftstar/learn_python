class ShoppingCart(object):
    """
    Creates shopping cart objects 
    for users of our fine website
    """

    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name


    def add_item(self, product, price):
        """ Add product to cart """
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added. Price: " + str(price))

        else:
            print (product + " is already in your cart")


    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in your cart")

my_cart = ShoppingCart("Nik")
my_cart.add_item("Garbage", 33)
my_cart.add_item("Litter", 19)

print (my_cart.items_in_cart)
