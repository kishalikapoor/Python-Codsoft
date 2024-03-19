contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    return results

def update_contact():
    view_contact_list()
    try:
        idx = int(input("\nEnter the index of the contact to update: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid index.")
            return
        contact = contacts[idx]
        print("Update contact details:")
        contact['name'] = input("Enter updated name: ")
        contact['phone'] = input("Enter updated phone number: ")
        contact['email'] = input("Enter updated email address: ")
        contact['address'] = input("Enter updated address: ")
        print("Contact updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact():
    view_contact_list()
    try:
        idx = int(input("\nEnter the index of the contact to delete: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid index.")
            return
        del contacts[idx]
        print("Contact deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = search_contact(query)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
