import re


def validate_phone_number(phone_number):
    pattern = re.compile(r"^(09\d{9}|081\d{8})$")
    return pattern.match(phone_number) is not None


def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                first_name, last_name, phone_number = line.strip().split(':')
                contacts.append({
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number
                })
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f"{contact['first_name']}:{contact['last_name']}:{contact['phone_number']}\n")


def add_contact(contacts):
    first_name = input("name: ")
    last_name = input("last name: ")
    phone_number = input("phone number: ")

    if not validate_phone_number(phone_number):
        print("The phone number entered is not valid.")
        return

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    })
    print("Contact added successfully.")


def search_contact(contacts):
    search_term = input("Enter the contact's first or last name: ")
    results = [contact for contact in contacts if
               search_term in contact['first_name'] or search_term in contact['last_name']]

    if results:
        for contact in results:
            print(f"{contact['first_name']} {contact['last_name']}, {contact['phone_number']}")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    first_name = input("name: ")
    last_name = input("last name: ")

    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")


def edit_contact(contacts):
    first_name = input("name: ")
    last_name = input("last name: ")

    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            new_phone_number = input("New phone number: ")

            if not validate_phone_number(new_phone_number):
                print("The phone number entered is not valid.")
                return

            contact['phone_number'] = new_phone_number
            print("Phone number edited successfully.")
            return
    print("Contact not found.")


def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)

    while True:
        print("\nPhonebook:")
        print("1. Add a new contact")
        print("2. Audience search")
        print("3. Delete the contact")
        print("4. Edit audience")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            save_contacts(filename, contacts)
            print("Information saved. Bye!")
            break
        else:
            print("The entered option is not valid. Try again.")


if __name__ == "__main__":
    main()
