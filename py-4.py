import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to edit: ")) - 1
    if 0 <= idx < len(contacts):
        contact = contacts[idx]
        contact['name'] = input(f"Enter new name [{contact['name']}]: ") or contact['name']
        contact['phone'] = input(f"Enter new phone [{contact['phone']}]: ") or contact['phone']
        contact['email'] = input(f"Enter new email [{contact['email']}]: ") or contact['email']
        save_contacts(contacts)
        print("Contact updated.")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        save_contacts(contacts)
        print(f"Deleted contact: {removed['name']}")
    else:
        print("Invalid contact number.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
