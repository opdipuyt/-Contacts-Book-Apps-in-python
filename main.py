# # #Contacts apps in python program


contacts = {}

is_running = True
while is_running:
    print("*****************")
    print("Contact Apps")
    print("******************")
    print("1.Create Contact ")
    print("2.View Contact ")
    print("3.Update Contact ")
    print("4.Delete Contact ")
    print("5.Search Contact")
    print("6.Count Contact")
    print("7.Exit")
    print("")

    choice = input("Enter your choice (1-7) : ")
    if choice =="1":
        name = input("Enter your name : ")
        if name in contacts:
            print(f"Contact name {name} already exists")

        else:

            age = input("Enter your age    : ")
            mobile = input("Enter your mobile : ")
            email = input("Enter your email      :")
            contacts[name]= {"Age":int(age),"Mobile":int(mobile),"Email":email}
            print(f"Contact name {name} has been created successfully")

    elif choice == "2":
        name = input("Enter your name : ")
        if name in contacts:
            contact = contacts[name]
            print(f"\nName    :{name}\nAge      :{age}\nMobile :{mobile}\nemail    :{email}")
        else:
            print("Contact not found")

    elif choice =="3":
        name = input("Enter your updateed  name : ")
        if name in contacts:
            age = input("Enter your updated age         : ")
            mobile = input("Enter your updated mobile : ")
            email = input("Enter your updated email      : ")
            contacts[name] = {"Age": int(age), "Mobile": int(mobile), "Email": email}
            print(f"Contact name {name} has been updated successfully")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter your name : ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print(f"Contact not found")


    elif choice =="5":
        search_name = input('Enter Contact name to search : ')
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found Name {name}\nAge {age}\nMobile:{mobile}")
                found = True
                if not found:
                    print("no contact found with that name : ")

    elif choice == "6":
        print(f"total contact in your book :{len(contacts)}")
    elif choice == "7":
        print("Thank you have a nice day ")
        break
    else:
        print("invalid choice ")



