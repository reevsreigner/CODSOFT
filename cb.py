import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="e")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=1, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=1, pady=5)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, sticky="e")
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=2)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=1, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=1, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        if self.contacts:
            contacts_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contacts_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        query = self.search_entry.get().lower()
        found_contacts = []
        for contact in self.contacts:
            if query in contact['Name'].lower() or query in contact['Phone']:
                found_contacts.append(f"{contact['Name']}: {contact['Phone']}")
        if found_contacts:
            contacts_list = "\n".join(found_contacts)
            messagebox.showinfo("Search Results", contacts_list)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        for contact in self.contacts:
            if contact['Name'] == name:
                contact.update({"Phone": phone, "Email": email, "Address": address})
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return
        messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()

        for contact in self.contacts:
            if contact['Name'] == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return
        messagebox.showerror("Error", "Contact not found!")


def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()
