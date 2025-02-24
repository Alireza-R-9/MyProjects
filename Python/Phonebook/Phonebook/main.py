import json

FILE_NAME = 'contacts.json'


def load_contacts():
    try:
        with open(FILE_NAME, 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")
    contact_id = f"{first_name.lower()}_{last_name.lower()}"
    contacts[contact_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number
    }
    save_contacts(contacts)
    print("Contact added.")


def find_contact_id(contacts, first_name, last_name):
    contact_id = f"{first_name.lower()}_{last_name.lower()}"
    if contact_id in contacts:
        return contact_id
    return None


def edit_contact(contacts):
    first_name = input("First name of contact to edit: ")
    last_name = input("Last name of contact to edit: ")
    contact_id = find_contact_id(contacts, first_name, last_name)

    if contact_id:
        new_first_name = input(f"New first name [{contacts[contact_id]['first_name']}]: ") or contacts[contact_id][
            'first_name']
        new_last_name = input(f"New last name [{contacts[contact_id]['last_name']}]: ") or contacts[contact_id][
            'last_name']
        new_phone_number = input(f"New phone number [{contacts[contact_id]['phone_number']}]: ") or \
                           contacts[contact_id]['phone_number']
        new_contact_id = f"{new_first_name.lower()}_{new_last_name.lower()}"

        if new_contact_id != contact_id:
            contacts[new_contact_id] = contacts.pop(contact_id)

        contacts[new_contact_id] = {
            'first_name': new_first_name,
            'last_name': new_last_name,
            'phone_number': new_phone_number
        }

        save_contacts(contacts)
        print("The contact was edited.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    first_name = input("First name of contact to delete: ")
    last_name = input("Last name of contact to delete: ")
    contact_id = find_contact_id(contacts, first_name, last_name)

    if contact_id:
        del contacts[contact_id]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    query = input("Search (first or last name): ").lower()
    results = [contact for contact in contacts.values() if
               query in contact['first_name'].lower() or query in contact['last_name'].lower()]
    if results:
        for result in results:
            print(
                f"First name: {result['first_name']}, Last name: {result['last_name']}, Phone number: {result['phone_number']}")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()
    while True:
        print("\nPhonebook")
        print("1. Add contact")
        print("2. Edit contact")
        print("3. Delete contact")
        print("4. Search contacts")
        print("5. Exit")
        choice = input("Select: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            break
        else:
            print("Invalid selection!")


if __name__ == "__main__":
    main()
