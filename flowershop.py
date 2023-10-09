class Flower:
    def __init__(self, flower_id, name, quantity, price, stock):
        self.flower_id = flower_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock

class Bouquet:
    def __init__(self, bouquet_id, name, flowers, price):
        self.bouquet_id = bouquet_id
        self.name = name
        self.flowers = flowers
        self.price = price

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Admin:
    def __init__(self):
        self.flowers = [Flower(1, "Roses", "10 stems", 20.0, 100),
                        Flower(2, "Lilies", "5 stems", 15.0, 50),
                        Flower(3, "Tulips", "15 stems", 25.0, 75)]

        self.bouquets = [Bouquet(1, "Rose Bouquet", [self.flowers[0]], 25.0),
                         Bouquet(2, "Mixed Bouquet", [self.flowers[0], self.flowers[1]], 30.0)]

def display_flower_menu(flowers):
    print("Flower Menu:")
    for i, flower in enumerate(flowers):
        print(f"{i+1}. {flower.name} ({flower.quantity}) [INR {flower.price}]")

def display_bouquet_menu(bouquets):
    print("Bouquet Menu:")
    for i, bouquet in enumerate(bouquets):
        print(f"{i+1}. {bouquet.name} [INR {bouquet.price}]")

def admin_add_flower(admin, name, quantity, price, stock):
    flower_id = len(admin.flowers) + 1
    flower = Flower(flower_id, name, quantity, price, stock)
    admin.flowers.append(flower)
    print(f"Flower ID: {flower_id} - {name} added to the menu.")

def admin_edit_flower(admin, flower_id, name, quantity, price, stock):
    for flower in admin.flowers:
        if flower.flower_id == flower_id:
            flower.name = name
            flower.quantity = quantity
            flower.price = price
            flower.stock = stock
            print(f"Flower with ID {flower_id} edited successfully.")
            return
    print(f"Flower with ID {flower_id} not found.")

def admin_remove_flower(admin, flower_id):
    for flower in admin.flowers:
        if flower.flower_id == flower_id:
            admin.flowers.remove(flower)
            print(f"Flower with ID {flower_id} removed from the menu.")
            return
    print(f"Flower with ID {flower_id} not found.")

def admin_add_bouquet(admin, name, flower_ids, price):
    bouquet_id = len(admin.bouquets) + 1
    flowers = [admin.flowers[flower_id - 1] for flower_id in flower_ids]
    bouquet = Bouquet(bouquet_id, name, flowers, price)
    admin.bouquets.append(bouquet)
    print(f"Bouquet ID: {bouquet_id} - {name} added to the menu.")

def admin_edit_bouquet(admin, bouquet_id, name, flower_ids, price):
    for bouquet in admin.bouquets:
        if bouquet.bouquet_id == bouquet_id:
            bouquet.name = name
            bouquet.flowers = [admin.flowers[flower_id - 1] for flower_id in flower_ids]
            bouquet.price = price
            print(f"Bouquet with ID {bouquet_id} edited successfully.")
            return
    print(f"Bouquet with ID {bouquet_id} not found.")

def admin_remove_bouquet(admin, bouquet_id):
    for bouquet in admin.bouquets:
        if bouquet.bouquet_id == bouquet_id:
            admin.bouquets.remove(bouquet)
            print(f"Bouquet with ID {bouquet_id} removed from the menu.")
            return
    print(f"Bouquet with ID {bouquet_id} not found.")

def user_register(users, full_name, phone_number, email, address, password):
    user = User(full_name, phone_number, email, address, password)
    users.append(user)
    print(f"User {full_name} registered successfully.")

def user_login(users, email, password):
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def user_place_order(user, flowers, bouquets, selected_items):
    total_cost = 0
    order_details = []
    for index in selected_items:
        if 0 < index <= len(flowers):
            flower = flowers[index - 1]
            total_cost += flower.price
            order_details.append(f"{flower.name} ({flower.quantity}) [INR {flower.price}]")
        elif 0 < index <= len(bouquets):
            bouquet = bouquets[index - 1]
            total_cost += bouquet.price
            order_details.append(f"{bouquet.name} [INR {bouquet.price}]")

    if total_cost == 0:
        print("No items selected for the order.")
        return

    print("Selected items for the order:")
    for item in order_details:
        print(item)
    print(f"Total Cost: INR {total_cost}")
    confirm_order = input("Confirm the order: yes/no")
    if confirm_order == 'yes':
        user.orders.append(order_details)
        print("Order placed successfully.")
    elif confirm_order == 'no':
        print("Order canceled.")
    else:
        print("Invalid choice.")

def user_view_order_history(user):
    if not user.orders:
        print("No order history available.")
        return

    print("Order History:")
    for i, order in enumerate(user.orders, start=1):
        print(f"Order {i}:")
        for item in order:
            print(item)

def user_update_profile(user, full_name, phone_number, address, password):
    user.full_name = full_name
    user.phone_number = phone_number
    user.address = address
    user.password = password
    print("User profile updated successfully.")

if __name__ == "__main__":
    admin = Admin()
    users = []

    while True:
        print("\nWelcome to the Flower Shop App!")
        print("1. Admin Login")
        print("2. User Register")
        print("3. User Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Admin Login
            admin_password = input("Enter admin password: ")
            if admin_password == "adminpass":
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add New Flower")
                    print("2. Edit Flower")
                    print("3. Remove Flower")
                    print("4. Add New Bouquet")
                    print("5. Edit Bouquet")
                    print("6. Remove Bouquet")
                    print("7. View Flower Menu")
                    print("8. View Bouquet Menu")
                    print("9. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        # Add New Flower
                        name = input("Enter flower name: ")
                        quantity = input("Enter quantity: ")
                        price = float(input("Enter price: "))
                        stock = int(input("Enter stock: "))
                        admin_add_flower(admin, name, quantity, price, stock)

                    elif admin_choice == "2":
                        # Edit Flower
                        flower_id = int(input("Enter Flower ID to edit: "))
                        name = input("Enter new flower name: ")
                        quantity = input("Enter new quantity: ")
                        price = float(input("Enter new price: "))
                        stock = int(input("Enter new stock: "))
                        admin_edit_flower(admin, flower_id, name, quantity, price, stock)

                    elif admin_choice == "3":
                        # Remove Flower
                        flower_id = int(input("Enter Flower ID to remove: "))
                        admin_remove_flower(admin, flower_id)

                    elif admin_choice == "4":
                        # Add New Bouquet
                        name = input("Enter bouquet name: ")
                        flower_ids = [int(x) for x in input("Enter flower IDs in the bouquet (e.g., 1 2): ").split()]
                        price = float(input("Enter bouquet price: "))
                        admin_add_bouquet(admin, name, flower_ids, price)

                    elif admin_choice == "5":
                        # Edit Bouquet
                        bouquet_id = int(input("Enter Bouquet ID to edit: "))
                        name = input("Enter new bouquet name: ")
                        flower_ids = [int(x) for x in input("Enter new flower IDs in the bouquet (e.g., 1 2): ").split()]
                        price = float(input("Enter new bouquet price: "))
                        admin_edit_bouquet(admin, bouquet_id, name, flower_ids, price)

                    elif admin_choice == "6":
                        # Remove Bouquet
                        bouquet_id = int(input("Enter Bouquet ID to remove: "))
                        admin_remove_bouquet(admin, bouquet_id)

                    elif admin_choice == "7":
                        # View Flower Menu
                        display_flower_menu(admin.flowers)

                    elif admin_choice == "8":
                        # View Bouquet Menu
                        display_bouquet_menu(admin.bouquets)

                    elif admin_choice == "9":
                        # Logout
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Admin login failed. Incorrect password.")

        elif choice == "2":
            # User Register
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            user_register(users, full_name, phone_number, email, address, password)

        elif choice == "3":
            # User Login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            logged_user = user_login(users, email, password)
            if logged_user:
                while True:
                    print("\nUser Menu:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        # Place New Order
                        display_flower_menu(admin.flowers)
                        display_bouquet_menu(admin.bouquets)
                        selected_items = [int(x) for x in input("Enter item numbers (e.g., 1 2): ").split()]
                        user_place_order(logged_user, admin.flowers, admin.bouquets, selected_items)

                    elif user_choice == "2":
                        # Order History
                        user_view_order_history(logged_user)

                    elif user_choice == "3":
                        # Update Profile
                        full_name = input("Enter new full name: ")
                        phone_number = input("Enter new phone number: ")
                        address = input("Enter new address: ")
                        password = input("Enter new password: ")
                        user_update_profile(logged_user, full_name, phone_number, address, password)

                    elif user_choice == "4":
                        # Logout
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("User login failed. Incorrect email or password.")

        elif choice == "4":
            # Exit
            print("Thank you for using the Flower Shop App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
