cart = []
if_exit = False

while not if_exit:
    print("=" * 30)
    print("Shopping Cart Menu")
    print("=" * 30)
    print("\n")
    print("Please choose what you like to do.")
    print("\n")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Calculate Total")
    print("5. Exit")
    print("\n")
    print("=" * 30)
    user_choice = int(input("Please make a choice and make input 1-5:"))
    if user_choice == 1:
        purchase_list = {}
        purchase_list["name"] = input("What do you like to purchase?: ").lower()
        purchase_list["price"] = float(input("Please enter price: "))
        purchase_list["quantity"] = float(input("Please enter quantity: "))
        cart.append(purchase_list)
    elif user_choice == 2:
        name = input("Enter item name to remove: ")
        for item in cart:
            if item["name"] == name.lower():
                cart.remove(item)
                print(f"{name}, has been removed.")
                break
        else:
            print(f"{name}, was not in cart.")
    elif user_choice == 3:
        if len(cart) == 0:
            print("Your cart is empty right now please add items.")
        for item in cart:
            print(f"Item: {item['name']}\nQuantity: {item['quantity']}\nTotal: Rs. {item['quantity']*item['price']}")
    elif user_choice == 4:
        total = 0
        for item in cart:
            print(f"Item: {item['name']}\nQuantity: {item['quantity']}\nTotal: Rs. {item['quantity']*item['price']}")
            total += item["quantity"]*item["price"]
        print("-" * 30)
        print(f"Subtotal: Rs. {total:.2f}")
        if total >= 5000:
            print("Yay you are eligible for 10% discount.")
            discount = total * 0.10
            grand_total = total - discount
            print(f"Discount(10%): Rs. {discount:.2f}")
            print(f"Grand Total: Rs. {grand_total:.2f}")
        else:
            print(f"Grand Total: Rs. {total:.2f}")
    else:
        if_exit = True