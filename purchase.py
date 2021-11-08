# Pre-existing customer and product lists
customer_list = [{'id': '2709', 'name': 'rufus', 'address': '40'},
                 {'id': '1439', 'name': 'faith', 'address': '24'},
                 {'id': '3520', 'name': 'amon', 'address': '56'}]
product_list = [{'id': '4056', 'name': 'fries', 'Quantity': '10', 'price': '200'},
                {'id': '2589', 'name': 'buns', 'Quantity': '20', 'price': '120'},
                {'id': '7860', 'name': 'smokies', 'Quantity': '32', 'price': '50'},
                {'id': '7410', 'name': 'soda', 'Quantity': '55', 'price': '60'}]

class product:
    def __init__(self,p_id,p_name,p_quantity,p_price):
        self.id = p_id
        self.name = p_name
        self.quantity = p_quantity
        self.price = p_price


def product_operation():
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
        another_p = input("Would you like to add another product's details?(y/n)".lower())
        if another_p == 'y':
            customer_list.append(product_data())
            print(product_list)
        else:
            print("Thank you")
    elif product_ops == 2:
        product_list.append(product_data())
        print(product_list)
        another_p = input("Would you like to add another product's details?(y/n)".lower())
        if another_p == 'y':
            product_list.append(product_data())
            print(product_list)
        else:
            print("Thank you")
    elif product_ops == 3:
        product_list.append(del_product())
        print(product_list)
        another_p = input("Would you like to delete another product's details?(y/n)".lower())
        if another_p == 'y':
            product_list.append(del_product())
            print(product_list)
        else:
            print("Thank you")
    elif product_ops == 4:
        product_list.append(update_product())
        print(product_list)
        another_p = input("Would you like to update another product's details?(y/n)".lower())
        if another_p == 'y':
            product_list.append(update_product())
            print(product_list)
        else:
            print("Thank you")
    elif product_ops == 5:
        product_file()
    elif product_ops == 6:
        product_purchase()
        another_p = input("Would you like to purchase another product?(y/n)".lower())
        if another_p == 'y':
            product_purchase()
        else:
            print("Thank you")
    elif product_ops == 7:
        exit()
    else:
        print("Operation not available, try again")
        product_operation()

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
                        print("Product has been Purchased")
                        print("Product remaining in stock\n",product_list[i])
                        break
                    else:
                        print("Product is out of stock")
                else:
                    print("product unavailable")
        """""
        if c_status == False:
            print("customer unavailable. Please enter the customer details.")
            customer_data()
            product_purchase()
        """

        return product_list

