print("WELCOME TO THE AMANDO SHOPPING SITE")
shoppingCart = {}

while True:
    print("1. Add your product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number of items to be added to the cart: "))
        if len(shoppingCart) + n > 5:
            print("Cart is full.")
        else:
            for i in range(n):
                item = input("Enter an item: ")
                brand = input("Enter the brand name: ")
                shoppingCart[item] = brand

            print("You added the following items to the cart:")
            for item, brand in shoppingCart.items():
                print(item + ": " + brand)

    elif choice == 2:
        item = input("Enter the item to be searched: ")
        if item in shoppingCart:
            print(item + ": " + shoppingCart[item])
        else:
            print("No product exists with this name.")

    elif choice == 3:
        if len(shoppingCart) == 0:
            print("Cart is empty, no item is found.")
        else:
            item = input("Enter the item to be deleted: ")
            if item in shoppingCart:
                del shoppingCart[item]
                print("Item deleted successfully.")
            else:
                print("No product exists with this name.")

    elif choice == 4:
        print("Thank you for shopping with us!")
        break

    else:
        print("Wrong option entered.")
