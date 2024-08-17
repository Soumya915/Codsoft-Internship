# Contact Book in Python

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts available.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(name):
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == '4':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)

        elif choice == '5':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the contact book function
contact_book()
