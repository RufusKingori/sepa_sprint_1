# Pre-existing customer and product lists
customer_list = [{'id': '2709', 'name': 'rufus', 'address': '40'},
                 {'id': '1439', 'name': 'faith', 'address': '24'},
                 {'id': '3520', 'name': 'amon', 'address': '56'}]
product_list = [{'id': '4056', 'name': 'fries', 'Quantity': '10', 'price': '200'},
                {'id': '2589', 'name': 'buns', 'Quantity': '20', 'price': '120'},
                {'id': '7860', 'name': 'smokies', 'Quantity': '32', 'price': '50'},
                {'id': '7410', 'name': 'soda', 'Quantity': '55', 'price': '60'}]

def customer_operation():
    print("****Welcome to customer service***")
    print("----------------------------------")
    #Customer operations menu
    customer_ops = int(input("Choose your operation:\n"       
                             "[1] Load customer data to array\n"
                             "[2] Insert new customer\n"
                             "[3] Delete a customer\n"
                             "[4] Update a customer\n"
                             "[5] Write Customer Data into a File\n"
                             "[6] Exit\n"))
    if customer_ops == 1:
        customer_list.append(customer_data())
        print(customer_list)
        another_c = input("Would you like to add another customer details?(y/n)".lower())
        if another_c == 'y':
            customer_list.append(customer_data())
            print(customer_list)
        else:
            print("Thank you")
    elif customer_ops == 2:
        customer_list.append(customer_data())
        print(customer_list)
        another_c = input("Would you like to add another customer's details?(y/n)".lower())
        if another_c == 'y':
            customer_list.append(customer_data())
            print(customer_list)
        else:
            print("Thank you")
    elif customer_ops == 3:
        del_customer(customer_list)
        print(customer_list)
        another_c = input("Would you like to delete another customer details?(y/n)".lower())
        if another_c == 'y':
            del_customer(customer_list)
            print(customer_list)
        else:
            print("Thank you")
    elif customer_ops == 4:
        update_customer(customer_list)
        print(customer_list)
        another_c = input("Would you like to update another customer details?(y/n)".lower())
        if another_c == 'y':
            update_customer(customer_list)
            print(customer_list)
        else:
            print("Thank you")
    elif customer_ops == 5:
        customer_file()
    elif customer_ops == 6:
        exit()
    else:
        print("Operation not available, try again")
        customer_operation()

def customer_data():
    #This function adds a customer into the customer list
    customer_id = input("Input a customer id")
    customer_name = input("Enter the customer name:\n")
    customer_address = int(input("Enter the customer address:\n"))
    dict = {"id": customer_id, "name": customer_name, "address": customer_address}
    return dict


def del_customer(customer_list):
    #This function deletes a customer from the list
    customer_id = input("Enter customer id:\n")
    for i in range(len(customer_list)-1):
        c_id = customer_list[i]["id"]
        if customer_id in c_id:
            customer_list.remove(customer_list[i])
    return customer_list


def update_customer(customer_list):
    #This function updates customer details by either the name or the address in the customer list.
    customer_id = input("Enter the customer id:")
    update_option = int(input("Enter option\n [1] for name change\n [2] for address change\n"))
    for i in range(len(customer_list)):
        c_id = customer_list[i]["id"]
        if customer_id in c_id:
            if update_option == 1:
                name = input("Enter the new name:")
                customer_list[i]['name'] = name
            elif update_option == 2:
                address = input("Enter the new address:")
                customer_list[i]['address'] = address
    return customer_list


def customer_file():
    #This function writes the customer list into a file
    cfile = open("customer_data.txt", "w")
    print(customer_list, file=cfile)
    print(customer_data(), file=cfile)
    cfile.close()

customer_operation()
