class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            print("Error!, Not enough stock")
            return False
        else:
            self.stock -= quantity
            return True

class User:

    def __init__(self, username, wallet=0):
        self.username = username
        self.wallet = wallet

    def deduct_funds(self, amount):
        if amount > self.wallet:
            print("Error!, You don't have enough balance")
            return False
        else:
            self.wallet -= amount
            return True

class Order:
    total_orders = 0
    def __init__(self, buyer, product, quantity, status = "Pending"):
        self.buyer = buyer
        self.product = product
        self.quantity = quantity
        self.status = status
        Order.total_orders += 1

    def process_order(self):
        total_cost = self.product.price * self.quantity
        if self.product.reduce_stock(self.quantity):
            if self.buyer.deduct_funds(total_cost):
                self.status = "Completed"
                self.status = "Completed"
                print("\nPurchase Successful")
                print(f"You purchased {self.quantity} {self.product.name} at total Rs. {total_cost:.2f} successfully.")
                return True
            else:
                self.product.stock += self.quantiy
                print("Order cancelled: Transaction rolled back due to insufficient funds.")
                return False
        else:
            return False

if __name__ == "__main__":
    # 1. Create a User with Rs. 5000 in their wallet
    buyer = User("Ravi", 5000.0)

    # 2. Create a Product with Rs. 1500 price and 3 items in stock
    headphone = Product("Wireless Headphones", 1500.0, 3)

    # 3. Print initial States
    print(f"Initial Stock: {headphone.stock}")
    print(f"Initial Wallet: {buyer.wallet}")

    # 4. Attempt to create and process Order #1 (Buy 2 headphones -> Total Rs. 3000)
    order1 = Order(buyer, headphone, 2)
    order1.process_order()

    # 5. Check remaining stock and wallet balance (Should be 1 headphone left, Rs. 2000 in wallet)
    print(f"Remaining Stock: {headphone.stock}")
    print(f"Remaining Wallet: {buyer.wallet}")

    # 6. Attempt Order #2 (Overdraft & Out of stock check: Try to buy 2 more headphones)
    # This should fail because only 1 headphone is left, and the total cost (Rs. 3000) exceeds Rs. 2000!
    order2 = Order(buyer, headphone, 2)
    order2.process_order()

    # 7. Print the class attribute to prove we tracked the total orders created in our database
    print(f"Total Orders Created globally {Order.total_orders}")