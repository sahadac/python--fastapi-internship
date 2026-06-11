contacts = {}

while True:

    print("\n1 Add")
    print("2 Search")
    print("3 Update")
    print("4 Delete")
    print("5 Show All")
    print("6 Exit")

    choice = input("Enter choice: ")

    # Add
    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contacts[name] = phone

        print(f"{name} added")

    # Search
    elif choice == "2":

        name = input("Enter name: ")

        print(contacts.get(name, "Contact not found"))

    # Update
    elif choice == "3":

        name = input("Enter name: ")

        if name in contacts:

            phone = input("Enter new phone: ")

            contacts[name] = phone

            print("Updated")

        else:
            print("Contact not found")

    # Delete
    elif choice == "4":

        name = input("Enter name: ")

        if name in contacts:

            del contacts[name]

            print("Deleted")

        else:
            print("Contact not found")

    # Show All
    elif choice == "5":

        for name in sorted(contacts):

            print(f"{name} : {contacts[name]}")

    # Exit
    elif choice == "6":

        print("Exit")
        break

    else:
        print("Invalid choice")