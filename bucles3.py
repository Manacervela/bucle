
book = {}

while True:
    print("\t.:MENU:.")
    print("1. New Contact")
    print("2. Delete contact")
    print("3. View existing contacts")
    print("4. Exit")
    option = int(input("Type a menu option: "))

    print()

    if option == 1:
        name = input("Name: ")
        phone = input("phone number: ")

        if name not in book:
            book[name] = phone
            print("Contact save!")
        else:
            print("That contact name is already in use")

    elif option==2:
        name = input("Contact Name: ")

        if name in book:
            del(book[name])
            print("contact deleted!")
        else:
            print("That contact does not exist")

    elif option==3:
        print("Notebook:")
        for clave,value in book.items():
            print(f"Name: {clave}, phone: {value}")

    elif option==4:
        print("thanks you, see you soon")
        break

    else:
        print("wrong menu option")

    print()
