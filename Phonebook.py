
phonebook = {}

def add_contact(name, email, number):
    phonebook[name] = {"email": email, "number": number}
    print("{name} has been added to the phonebook.")
    
def search_contact(name):
    if name in phonebook:
        contact = phonebook[name]
        print("Name: {name}")
        print("Email: {contact['email']}")
        print("Number: {contact['number']}")
    else:
        print("{name} not found in the phonebook.")

def update_contact(name, email, number):
    if name in phonebook:
        phonebook[name] = {"email": email, "number": number}
        print("{name}'s information has been updated.")
    else:
        print("{name} not found in the phonebook. You can add a new contact.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("{name} has been deleted from the phonebook.")
    else:
        print("{name} not found in the phonebook.")

def display_contacts():
    print("Phonebook Contacts:")
    for name, contact in phonebook.items():
        print("Name: {name}")
        print("Email: {contact['email']}")
        print("Number: {contact['number']}")
        print("--------------------")


while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        name = input("Enter the name: ")
        email = input("Enter the email address: ")
        number = input("Enter the phone number: ")
        add_contact(name, email, number)
    elif choice == "2":
        name = input("Enter the name to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter the name to update: ")
        email = input("Enter the new email address: ")
        number = input("Enter the new phone number: ")
        update_contact(name, email, number)
    elif choice == "4":
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Phonebook.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
