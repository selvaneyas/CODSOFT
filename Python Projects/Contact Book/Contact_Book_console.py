class ConsoleContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, query):
        print("Search Results:")
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone'] = new_phone
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def run(self):
        while True:
            print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email address: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == '4':
                name = input("Enter name of contact to update: ")
                new_phone = input("Enter new phone number: ")
                self.update_contact(name, new_phone)
            elif choice == '5':
                name = input("Enter name of contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_book = ConsoleContactBook()
    contact_book.run()