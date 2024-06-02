import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Import the required modules from Pillow
import json
from cryptography.fernet import Fernet

class GuiContactBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Book")
        self.geometry("700x700")
        self.resizable(False, False)

        # Load or generate encryption key
        self.key = self.load_key()
        self.fernet = Fernet(self.key)

        # Load contacts from file
        self.contacts = self.load_contacts()

        self.create_widgets()

    def load_key(self):
        try:
            with open("secret.key", "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
        return key

    def save_contacts(self):
        with open("contacts.dat", "wb") as file:
            encrypted_data = self.fernet.encrypt(json.dumps(self.contacts).encode())
            file.write(encrypted_data)

    def load_contacts(self):
        try:
            with open("contacts.dat", "rb") as file:
                encrypted_data = file.read()
                data = self.fernet.decrypt(encrypted_data).decode()
                return json.loads(data)
        except FileNotFoundError:
            return []

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = ttk.Label(main_frame, text="Contact Book", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Information about the app
        self.info_label = ttk.Label(main_frame, text="Manage your contacts easily. Add, view, and search contacts.", font=("Arial", 12), wraplength=650, justify="center")
        self.info_label.pack(pady=10)

        # Form Frame
        self.form_frame = ttk.Frame(main_frame)
        self.form_frame.pack(pady=10)

        # Form fields
        ttk.Label(self.form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = ttk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.bind("<Return>", lambda event: self.phone_entry.focus())

        ttk.Label(self.form_frame, text="Phone:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.phone_entry.bind("<Return>", lambda event: self.email_entry.focus())

        ttk.Label(self.form_frame, text="Email:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.email_entry = ttk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.email_entry.bind("<Return>", lambda event: self.address_entry.focus())

        ttk.Label(self.form_frame, text="Address:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.address_entry = ttk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        self.address_entry.bind("<Return>", lambda event: self.add_contact())

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        self.add_button = ttk.Button(button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        self.view_button = ttk.Button(button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=10)

        self.delete_button = ttk.Button(button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=2, padx=10)

        self.clear_button = ttk.Button(button_frame, text="Clear History", command=self.clear_history)
        self.clear_button.grid(row=0, column=3, padx=10)

        # Search Frame
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(pady=10)

        ttk.Label(search_frame, text="Search:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5)
        self.search_entry = ttk.Entry(search_frame, font=("Arial", 12), width=30)
        self.search_entry.grid(row=0, column=1, padx=5)
        self.search_entry.bind("<Return>", lambda event: self.search_contact())

        self.search_button = ttk.Button(search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5)

        # Notification Box
        self.notification_label = ttk.Label(main_frame, text="", font=("Arial", 12), foreground="red")
        self.notification_label.pack(pady=10)

        # Table Frame
        self.table_frame = ttk.Frame(main_frame)
        self.table_frame.pack(pady=10)

        self.table = ttk.Treeview(self.table_frame, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.table.heading("Name", text="Name")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Email", text="Email")
        self.table.heading("Address", text="Address")
        self.table.column("Name", width=150)
        self.table.column("Phone", width=100)
        self.table.column("Email", width=200)
        self.table.column("Address", width=200)
        self.table.pack()

        # Style Configuration
        style = ttk.Style()
        style.configure("TLabel", padding=5)
        style.configure("TButton", padding=5)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        # Load initial data into table
        self.update_table()

    def add_contact(self, event=None):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone or not email or not address:
            self.show_notification("All fields are required", "red")
            return

        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        self.save_contacts()
        self.show_notification("Contact added successfully", "green")
        self.clear_form()
        self.update_table()

    def view_contacts(self):
        self.update_table()

    def search_contact(self):
        query = self.search_entry.get()
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]

        self.table.delete(*self.table.get_children())
        for contact in results:
            self.table.insert("", "end", values=(contact['name'], contact['phone'], contact['email'], contact['address']))

        if not results:
            self.show_notification("No contacts found", "red")
        else:
            self.notification_label.config(text="")

    def delete_contact(self):
        selected_item = self.table.selection()
        if not selected_item:
            self.show_notification("Please select a contact to delete", "red")
            return

        contact_info = self.table.item(selected_item)["values"]
        self.contacts = [contact for contact in self.contacts if not (contact["name"] == contact_info[0] and contact["phone"] == contact_info[1])]

        self.save_contacts()
        self.update_table()
        self.show_notification("Contact deleted successfully", "green")

    def clear_history(self):
        self.contacts = []
        self.save_contacts()
        self.update_table()
        self.show_notification("Contact list cleared", "green")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

    def update_table(self):
        self.table.delete(*self.table.get_children())
        for contact in self.contacts:
            self.table.insert("", "end", values=(contact['name'], contact['phone'], contact['email'], contact['address']))

    def show_notification(self, message, color):
        self.notification_label.config(text=message, foreground=color)

if __name__ == "__main__":
    app = GuiContactBook()
    
    # Window Icon
    window_icon = ImageTk.PhotoImage(file="images/contacts.png")
    app.iconphoto(False, window_icon)
    
    app.mainloop()
