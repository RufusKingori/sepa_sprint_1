# This program is used by kings foods and beverages staff to order foods and drinks for it's customers.

# Pre-existing customer and product lists
customer_list = [{'id': '2709', 'name': 'rufus', 'address': '40'},
                 {'id': '1439', 'name': 'faith', 'address': '24'},
                 {'id': '3520', 'name': 'amon', 'address': '56'}]
product_list = [{'id': '4056', 'name': 'fries', 'Quantity': '10', 'price': '200'},
                {'id': '2589', 'name': 'buns', 'Quantity': '20', 'price': '120'},
                {'id': '7860', 'name': 'smokies', 'Quantity': '32', 'price': '50'},
                {'id': '7410', 'name': 'soda', 'Quantity': '55', 'price': '60'}]


def main():
    print("*****Welcome to Kings foods and beverages*****")
    print("----------------------------------------------")
    operation = int(input("Choose your operation\n"     #main menu
                          "[1] Customer operations\n"
                          "[2] Product operations\n"
                          "[3] Queries\n"
                          "[4] Exit\n"))
    if operation == 1:
        customer_operation()
    elif operation == 2:
        product_operation()
    elif operation == 3:
        queries()
    elif operation == 4:
        exit()
        print("Thank you")
    else:
        print("Please enter one of the options 1, 2, 3 or 4")


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
    elif customer_ops == 2:
        customer_list.append(customer_data())
        print(customer_list)
    elif customer_ops == 3:
        del_customer(customer_list)
        print(customer_list)
    elif customer_ops == 4:
        update_customer(customer_list)
        print(customer_list)
    elif customer_ops == 5:
        customer_file()
    elif customer_ops == 6:
        exit()
    else:
        print("Operation not available, try again")


def product_operation():
    product_data = []
    print("****Welcome to Product operations****")
    print("-------------------------------------")
    #Product operations menu
    product_ops = int(input("Choose your operation:\n"
                            "[1] Load product data to array\n"
                            "[2] Insert a new product\n"
                            "[3] Delete a product\n"
                            "[4] Update product data\n"
                            "[5] Write product data into a file\n"
                            "[6] Purchase product\n"
                            "[7} Exit\n"))
    if product_ops == 1:
        product_list.append(product_data())
        print(product_list)
    elif product_ops == 2:
        product_list.append(product_data())
        print(product_list)
    elif product_ops == 3:
        product_list.append(del_product())
        print(product_list)
    elif product_ops == 4:
        product_list.append(update_product())
        print(product_list)
    elif product_ops == 5:
        product_file()
    elif product_ops == 6:
        product_purchase()
        print(product_list)
    elif product_ops == 7:
        exit()
    else:
        print("Operation not available, try again")


def queries():
    print("*****Welcome to the queries section*****")
    print("----------------------------------------")
    #Queries menu
    queries_op = int(input("Choose your operation:\n"
                           "[1] Search a product\n"
                           "[2] List all customers\n"
                           "[3] List all products\n"
                           "[4] List a customer's name, products bought and total spent\n"
                           "[5] Quit\n"))
    if queries_op == 1:
        search_product()
    elif queries_op == 2:
        print(customer_list)
    elif queries_op == 3:
        print(product_list)
    elif queries_op == 4:
        purchase_data()
    elif queries_op == 5:
        quit()
    else:
        print("Operation not available, Try again")


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


def update_customer():
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

def product_data():
    #This function adds a product into the list of products.
    p_id = input("Enter the product id:")
    p_name = input("Enter the product name:")
    p_amount = int(input("Enter the product quantity amount:"))
    p_price = float(input("Enter the product price:"))
    dict = {"product id": p_id, "product name": p_name, "Quantity": p_amount, "price": p_price}
    return dict


def del_product():
    #This function deletes a product from the list of products
    product_id = input("Enter the product id:\n")
    for i in range(len(product_list)):
        id_p = product_list[i]["id"]
        if product_id in id_p:
            product_list.remove(product_list[i])
    return product_list


def update_product():
    #This function deletes a product from the list of products
    product_id = input("Enter the customer id:")
    update_option = int(input("Enter option\n [1] for quantity change\n [2] for price change\n"))
    for i in range(len(product_list)):
        id_p = (product_list[i]["id"])
        if product_id in id_p:
            if update_option == 1:
                quantity = input("Enter the new quantity:")
                product_list[i]['Quantity'] = quantity
            elif update_option == 2:
                price = input("Enter the new price:")
                product_list[i]['price'] = price
    return product_list


def product_file():
    #This function writes the list of products into a file product_data.txt
    pfile = open("product_data.txt", "w")
    print(product_list, file=pfile)
    print(product_data(),file=pfile)
    pfile.close()


def product_purchase():
    #This functions reads a customer's id from the list of customers.
    #It reads a product's id from the list of products.
    #The program asks the user to imput the quantity of the product to purchase.
    #The program deducts the quantity in the list to quantity input.

    c_id = input("Enter the customer id:\n")
    for i in range(len(customer_list)):
        if c_id in customer_list[i]['id']:
            print("proceed with the purchase")
            p_id = input("Enter the product id:\n")
            for i in range(len(product_list)):
                if p_id in product_list[i]['id']:
                    p_amount = int(input("Enter the quantity purchased:\n"))
                    if p_amount <= int(product_list[i]['Quantity']):
                        product_list[i]['Quantity'] = int(product_list[i]['Quantity']) - p_amount
                        print("Product Purchased")
                        print(product_list[i])
                    else:
                        print("Product is out of stock")
                        break
                else:
                    print("product unavailable")
                    exit()

            return product_list



def search_product():
    #This function loops through the product list for the product id
    p_id = input("Enter the product ID:\n")
    for i in range(len(product_list)):
        product_id = product_list[i]['id']
        if p_id in product_id:
            print(product_list[i])
        else:
            print("Product not available")

def list_customer():
    #This function loops through the list of customers searching for the customer with the id input
    c_id = input("Enter the customer ID:\n")
    for i in range(len(customer_list)):
        customer_id = customer_list[i]['id']
        if c_id == customer_id:
            print(customer_list[i])
            break
        else:
            print("customer not available")


def purchase_data():
    #This program writes to file the customer's name, products purchased, quantity purchased
    #and the total amout to be paid.
    product_details = []
    total = 0
    id_customer = input("Enter the customer id:")
    for i in range(len(purchase_list)):
        c_id = purchase_list[i]["c_id"]
        if id_customer in c_id:
            c_name = purchase_list[i]['c_name']
            p_name = purchase_list[i]['p_name']
            quantity = purchase_list[i]['quantity']
            price = purchase_list[i]['price']
            total_price = int(price) * int(quantity)
            product_d = {"p_name":p_name,"quantity":quantity}
            product_details.append(product_d)
            total += total_price
    print(c_name,"has bought",product_details,"for",total)


#Pre-existing purchase list with details of customer and product purchased.
purchase_list = [{"c_id":"2709","c_name":"rufus","p_name":"buns","quantity":"3","price":"120"},
                 {"c_id":"1439","c_name":"faith","p_name":"soda","quantity":"2","price":"60"},
                 {"c_id":"3520","c_name":"amon","p_name":"fries","quantity":"2","price":"200"},
                 {"c_id":"1439","c_name":"faith","p_name":"smokies","quantity":"5","price":"50"}]
main()







