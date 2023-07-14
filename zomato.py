import json

MENU_FILE = "menu.json"
ORDERS_FILE = "orders.json"


def load_menu():
    try:
        with open(MENU_FILE) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_menu(menu):
    with open(MENU_FILE, "w") as file:
        json.dump(menu, file)


def load_orders():
    try:
        with open(ORDERS_FILE) as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file)


def display_menu(menu):
    print("Menu:")
    print("ID\tName\tPrice\tAvailability")
    for dish_id, dish in menu.items():
        print(f"{dish_id}\t{dish['name']}\t{dish['price']}\t{dish['availability']}")


def add_dish(menu):
    dish_id = input("Enter Dish ID: ")
    name = input("Enter Dish Name: ")
    price = float(input("Enter Dish Price: "))
    availability = input("Enter Dish Availability (yes/no): ")
    menu[dish_id] = {
        'name': name,
        'price': price,
        'availability': availability
    }
    print("Dish added to the menu.")


def remove_dish(menu):
    dish_id = input("Enter Dish ID to remove: ")
    if dish_id in menu:
        del menu[dish_id]
        print("Dish removed from the menu.")
    else:
        print("Dish not found in the menu.")


def update_dish_availability(menu):
    dish_id = input("Enter Dish ID to update availability: ")
    if dish_id in menu:
        availability = input("Enter Dish Availability (yes/no): ")
        menu[dish_id]['availability'] = availability
        print("Dish availability updated.")
    else:
        print("Dish not found in the menu.")


def take_order(menu, orders):
    customer_name = input("Enter Customer Name: ")
    order_id = generate_order_id(orders)
    order = {'order_id': order_id, 'customer': customer_name, 'dishes': [], 'status': 'received'}
    dish_ids = input("Enter Dish IDs (comma-separated): ").split(',')
    total_bill = 0
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]['availability'] == 'yes':
            order['dishes'].append(dish_id)
            total_bill += menu[dish_id]['price']
        else:
            print(f"Dish {dish_id} is not available. Order not added.")
            return
    order['total_bill'] = total_bill
    orders.append(order)
    print("Order added successfully. Order ID:", order_id)


def update_order_status(orders):
    order_id = input("Enter Order ID to update status: ")
    for order in orders:
        if order.get('order_id') == order_id:
            status = input("Enter New Status: ")
            order['status'] = status
            print("Order status updated.")
            return
    print("Order not found.")


def display_orders(orders):
    print("Orders:")
    print("ID\tCustomer\tDishes\tStatus\tTotal Bill")
    for order in orders:
        dishes = ", ".join(order['dishes'])
        print(f"{order.get('order_id')}\t{order['customer']}\t{dishes}\t{order['status']}\t{order['total_bill']}")


def generate_order_id(orders):
    if orders:
        return str(int(orders[-1].get('order_id', 0)) + 1)
    return "1"


def main():
    menu = load_menu()
    orders = load_orders()

    while True:
        print("\n==== Zomato Chronicles: The Great Food Fiasco ====")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Display Orders")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu(menu)

        elif choice == "2":
            add_dish(menu)
            save_menu(menu)

        elif choice == "3":
            remove_dish(menu)
            save_menu(menu)

        elif choice == "4":
            update_dish_availability(menu)
            save_menu(menu)

        elif choice == "5":
            take_order(menu, orders)
            save_orders(orders)

        elif choice == "6":
            update_order_status(orders)
            save_orders(orders)

        elif choice == "7":
            display_orders(orders)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

    save_menu(menu)
    save_orders(orders)


if __name__ == "__main__":
    main()
