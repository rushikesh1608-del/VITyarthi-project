#CONTACT BOOK

contacts={}

# Adds a new contact to the contacts dictionary after checking it doesn't already exist
def add():
    
    name=input("Enter name: ").strip()

    if name in contacts:
        print(f"Contact '{name}' already exists. Use update instead.\n")
        return

    phone=input("Enter phone number: ").strip()
    email=input("Enter email (optional): ").strip()

    contacts[name]={"phone": phone, "email": email}
    print(f"Contact '{name}' added succesfully.\n")


# Displays all saved contacts sorted alphabetically by name
def view():

    if not contacts:
        print("No contacts saved yet.\n")
        return

    print("\n=== All Contacts ===")
    for name, details in sorted(contacts.items()):
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email'] if details['email'] else 'N/A'} ")
        print("="*20)
    print()


# Searches for a single contact by exact name and prints its details
def search():

    name=input("Enter name to search: ").strip()

    if name in contacts:
        details = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone:{details['phone']}")
        print(f"Email: {details['email'] if details['email']else 'N/A'}\n")
    else:
        print(f"No contact found with the name '{name}'.\n")


# Updates an existing contact's phone or email, keeping old values if left blank
def update():

    name=input("Enter name to update: ").strip()

    if name not in contacts:
        print(f"No contact found with the name '{name}'.\n")
        return

    print("Leave a field blank to keep it unchanged.")
    phone=input(f"New phone (current: {contacts[name]['phone']}): ").strip()
    email=input(f"New email (current: {contacts[name]['email']}): ").strip()

    if phone:
        contacts[name]["phone"]=phone

    if email:
        contacts[name]["email"]=email

    print(f"Contact '{name}' updated successfully.\n")


# Deletes a contact after asking the user to confirm
def delete():

    name=input("Enter name to delete: ").strip()

    if name in contacts:
        confirm=input(f"Are you sure you want to delete '{name}'? (y/n): ").strip()
        if confirm=="y":
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.\n")
        else:
            print("Delete Cancelled.\n")
    else:
        print(f"No Contact found with this name '{name}'.\n")


# Prints the main menu options for the user to choose from
def menu():
    print("===== CONTACT BOOK =====")

    print("1. Add Contact")
    
    print("2. View All Contacts")
    
    print("3. Search Contact")
    
    print("4. Update Contact")
    
    print("5. Delete Contact")
    
    print("6. Exit")


# Runs the main program loop, reading user choice and calling the matching function
def main():


    while True:

        menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add()

        elif choice == "2":
            view()

        elif choice == "3":
            search()

        elif choice == "4":
            update()

        elif choice == "5":
            delete()

        elif choice == "6":
            print("Exiting Contact Book. BYE!!!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
main()

