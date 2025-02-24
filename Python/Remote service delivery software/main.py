import json
import os


class User:
    def __init__(self, user_id, first_name, last_name, username, password, balance, phone, city):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.balance = balance
        self.phone = phone
        self.city = city

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "balance": self.balance,
            "phone": self.phone,
            "city": self.city
        }



class Operator:
    def __init__(self, operator_id, first_name, last_name, username, password, phone, city, balance, rating):
        self.operator_id = operator_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.phone = phone
        self.city = city
        self.balance = balance
        self.rating = rating

    def to_dict(self):
        return {
            "operator_id": self.operator_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "phone": self.phone,
            "city": self.city,
            "balance": self.balance,
            "rating": self.rating
        }



class Admin:
    def __init__(self, admin_id, username, password):
        self.admin_id = admin_id
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "admin_id": self.admin_id,
            "username": self.username,
            "password": self.password
        }


class Order:
    def __init__(self, order_id, user_id, operator_id, cost, start_date, end_date, user_rating):
        self.order_id = order_id
        self.user_id = user_id
        self.operator_id = operator_id
        self.cost = cost
        self.start_date = start_date
        self.end_date = end_date
        self.user_rating = user_rating

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "operator_id": self.operator_id,
            "cost": self.cost,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "user_rating": self.user_rating
        }


def register_user():
    user_id = input("User ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    balance = 0
    phone = input("Phone Number: ")
    city = input("City: ")

    user = User(user_id, first_name, last_name, username, password, balance, phone, city)

    with open("users.json", "r") as file:
        users = json.load(file)
    users.append(user.to_dict())
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("Registration successful!")


def register_operator():
    operator_id = input("Operator ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    phone = input("Phone Number: ")
    city = input("City: ")
    balance = 0
    rating = 0

    operator = Operator(operator_id, first_name, last_name, username, password, phone, city, balance, rating)


    with open("operators.json", "r") as file:
        operators = json.load(file)
    operators.append(operator.to_dict())
    with open("operators.json", "w") as file:
        json.dump(operators, file, indent=4)

    print("Registration successful!")


def login_user():
    username = input("Username: ")
    password = input("Password: ")

    with open("users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return user
    print("Invalid username or password!")
    return None


def login_operator():
    username = input("Username: ")
    password = input("Password: ")

    with open("operators.json", "r") as file:
        operators = json.load(file)

    for operator in operators:
        if operator['username'] == username and operator['password'] == password:
            print("Login successful!")
            return operator
    print("Invalid username or password!")
    return None


def login_admin():
    username = input("Username: ")
    password = input("Password: ")

    with open("admins.json", "r") as file:
        admins = json.load(file)

    for admin in admins:
        if admin['username'] == username and admin['password'] == password:
            print("Login successful!")
            return admin
    print("Invalid username or password!")
    return None


def main_menu():
    while True:
        print("1. Register as User")
        print("2. Register as Operator")
        print("3. Login as User")
        print("4. Login as Operator")
        print("5. Login as Admin")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            register_operator()
        elif choice == "3":
            user = login_user()
            if user:
                user_menu(user)
        elif choice == "4":
            operator = login_operator()
            if operator:
                operator_menu(operator)
        elif choice == "5":
            admin = login_admin()
            if admin:
                admin_menu(admin)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")


def user_menu(user):
    while True:
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Add Balance")
        print("4. Place Order")
        print("5. View Orders")
        print("6. Rate Operator")
        print("7. Report Issue")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(user)
        elif choice == "2":
            edit_profile(user)
        elif choice == "3":
            add_balance(user)
        elif choice == "4":
            place_order(user)
        elif choice == "5":
            view_orders(user)
        elif choice == "6":
            rate_operator(user)
        elif choice == "7":
            report_issue(user)
        elif choice == "8":
            break
        else:
            print("Invalid choice! Please try again.")


def operator_menu(operator):
    while True:
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. View Orders")
        print("4. Accept Order")
        print("5. Report Issue")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(operator)
        elif choice == "2":
            edit_profile(operator)
        elif choice == "3":
            view_orders(operator)
        elif choice == "4":
            accept_order(operator)
        elif choice == "5":
            report_issue(operator)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")


def admin_menu(admin):
    while True:
        print("1. View Users")
        print("2. View Operators")
        print("3. View Orders")
        print("4. Manage Users")
        print("5. Manage Operators")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_users()
        elif choice == "2":
            view_operators()
        elif choice == "3":
            view_orders()
        elif choice == "4":
            manage_users()
        elif choice == "5":
            manage_operators()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")


def initialize_data_files():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            json.dump([], file, indent=4)

    if not os.path.exists("operators.json"):
        with open("operators.json", "w") as file:
            json.dump([], file, indent=4)

    if not os.path.exists("admins.json"):
        with open("admins.json", "w") as file:
            json.dump([], file, indent=4)

    if not os.path.exists("orders.json"):
        with open("orders.json", "w") as file:
            json.dump([], file, indent=4)


def main():
    initialize_data_files()
    main_menu()


if __name__ == "__main__":
    main()
