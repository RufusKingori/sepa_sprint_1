# Pre-existing customer and product lists
customer_list = [{'id': '2709', 'name': 'rufus', 'address': '40'},
                 {'id': '1439', 'name': 'faith', 'address': '24'},
                 {'id': '3520', 'name': 'amon', 'address': '56'}]
product_list = [{'id': '4056', 'name': 'fries', 'Quantity': '10', 'price': '200'},
                {'id': '2589', 'name': 'buns', 'Quantity': '20', 'price': '120'},
                {'id': '7860', 'name': 'smokies', 'Quantity': '32', 'price': '50'},
                {'id': '7410', 'name': 'soda', 'Quantity': '55', 'price': '60'}]
#Pre-existing purchase list with details of customer and product purchased.
purchase_list = [{"c_id":"2709","c_name":"rufus","p_name":"buns","quantity":"3","price":"120"},
                 {"c_id":"1439","c_name":"faith","p_name":"soda","quantity":"2","price":"60"},
                 {"c_id":"3520","c_name":"amon","p_name":"fries","quantity":"2","price":"200"},
                 {"c_id":"1439","c_name":"faith","p_name":"smokies","quantity":"5","price":"50"}]

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
        another_p = input("Would you like to search another product's details?(y/n)".lower())
        if another_p == 'y':
            search_product()
        else:
            print("Thank you")
    elif queries_op == 2:
        print(customer_list)
    elif queries_op == 3:
        print(product_list)
    elif queries_op == 4:
        purchase_data()
        another_p = input("Would you like to search another customer's product details?(y/n)".lower())
        if another_p == 'y':
            purchase_data()
        else:
            print("Thank you")
    elif queries_op == 5:
        quit()
    else:
        print("Operation not available, Try again")
        queries()

class queries:
    def __init__(self,c_id,c_name,p_id,p_name,p_quantity,p_price):
        self.c_id = c_id
        self.c_name = c_name
        self.p_id = p_id
        self.p_name = p_name
        self.p_quantity = p_quantity
        self.p_price = p_price

def search_product():
    #This function loops through the product list for the product id
    p_id = input("Enter the product ID:\n")
    for i in range(len(product_list)):
        product_id = product_list[i]['id']
        if p_id in product_id:
            print(product_list[i])
        else:
            print("Product not available")


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


