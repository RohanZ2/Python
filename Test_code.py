import sys
import unittest 

class ShoppingCart:
    def __init__(self, cart):
        if cart is None:
            cart = {}
        self.cart = cart

    def add_item(self, item,quantity, price):
        if item in self.cart:
            self.cart[item]["quantity" ] += quantity
        else:
            self.cart[item] = {"quantity" : quantity, "price" : price}
    
    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]

    def calc_price(self):
        total = 0
        
        for v in self.cart.values():
            total += v['price'] *v["quantity"]
        
        return total

    def print_cart(self):
        
        for k,v in self.cart.items():
            print(k, v)
        
        print(self.calc_price())

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart({})

    def test_add_item(self):
            self.cart.add_item("apple", 2, 3.0)
            self.assertIn("apple", self.cart.cart)
            self.assertEqual(self.cart.cart["apple"]["quantity"], 2)
            self.assertEqual(self.cart.cart["apple"]["price"], 3.0)



if __name__ == '__main__':
    cart = ShoppingCart({})
    while True:
       
        item = input("What item do you need to buy: ")
        if item == "done":
            break   

        quantity = float(input("How much of this item do you need?: "))
        price = float(input("What is the price of this item?: "))
        cart.add_item(item, quantity, price)

        remove = input("do you want to  remove any items? y or n: ")
        if remove == "y":
            item_to_remove = input("What Item do you want to remvoe?: ")
            cart.remove_item(item_to_remove)
    
    cart.print_cart()

    if len(sys.argv) > 1:
        TestShoppingCart.item = sys.argv.pop()
    unittest.main()