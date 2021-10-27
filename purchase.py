customer_id = [114,277,290,154,139]
customer_name = ["amon","faith","albert","alfred","brenda"]
customer_address =[224,187,666,144,987]

product_id = [45,20,64,98,41,20]
product_name = ["burger","chips","buns","soda","cheese"]
product_amount = [15,20,8,12,14]
product_price = [150,200,80,120,40]



def main():
    print("*****Welcome to Kings foods and beverages*****")
    print("----------------------------------------------")
    operation = int(input("Choose your operation\n"
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
    customer_ops = int(input("Choose your operation:\n"
                             "[1] Load customer data to array\n"
                             "[2] Insert new customer\n"
                             "[3] Delete a customer\n"
                             "[4] Update a customer\n"
                             "[5] Write Customer Data into a File\n"
                             "[6] Exit\n"))
    if customer_ops == 1:
        pass
    elif customer_ops == 2:
        pass
    elif customer_ops == 3:
        pass
    elif customer_ops == 4:
        pass
    elif customer_ops == 5:
        pass
    elif customer_ops == 6:
        exit()
    else:
        print("Operation not available, try again")


def product_operation():
    product_data = []
    print("****Welcome to Product operations****")
    print("-------------------------------------")
    product_ops = int(input("Choose your operation:\n"
                            "[1] Load product data to array\n"
                            "[2] Insert a new product\n"
                            "[3] Delete a product\n"
                            "[4] Update product data\n"
                            "[5] Write product data into a file\n"
                            "[6] Purchase product\n"
                            "[7} Exit\n"))
    if product_ops == 1:
        pass
    elif product_ops == 2:
        pass
    elif product_ops == 3:
        pass
    elif product_ops == 4:
        pass
    elif product_ops == 5:
        pass
    elif product_ops == 6:
        pass
    elif product_ops == 7:
        exit()
    else:
        print("Operation not available, try again")


def queries():
    print("*****Welcome to the queries section*****")
    print("----------------------------------------")
    queries_op = int(input("Choose your operation:\n"
                           "[1] Search a product\n"
                           "[2] List all customers\n"
                           "[3] List all products\n"
                           "[4] List a customer\n"
                           "[5] Quit\n"))
    if queries_op == 1:
        pass
    elif queries_op == 2:
        pass
    elif queries_op == 3:
        pass
    elif queries_op == 4:
        pass
    elif queries_op == 5:
        quit()
    else:
        print("Operation not available, Try again")

def customer_data():
    infile = open("customer_data.txt", "w")
    c_id = int(input("Enter the customer ID"))
    customer_id.append(c_id)
    c_name = input("Enter the customer name")
    customer_name.append(c_name)
    c_address = input("Enter the customer address")
    customer_address.append(c_address)
    print(customer_id,customer_name,customer_address,file=infile)
    infile.close()




def purchase():
    my_order = []
    my_cost = []
    counter = 0
    total = 0
    customer = input("Enter the customer name:")
    if customer in customer_name:
        next_order = True
        while next_order == True:
            food_order = input("Enter your order:")
            if food_order =="burger":
                my_order.append(product_name[0])
                my_cost.append(product_price[0])
                counter = counter + 1
                total = total + (product_price[0])
            elif food_order == "chips":
                my_order.append(product_name[1])
                my_cost.append(product_price[1])
                counter = counter + 1
                total = total + (product_price[1])
            elif food_order == "buns":
                my_order.append(product_name[2])
                my_cost.append(product_price[2])
                counter = counter + 1
                total = total + (product_price[2])
            elif food_order == "soda":
                my_order.append(product_name[3])
                my_cost.append(product_price[3])
                counter = counter + 1
                total = total + (product_price[3])
            elif food_order == "cheese":
                my_order.append(product_name[4])
                my_cost.append(product_price[4])
                counter = counter + 1
                total = total + (product_price[4])
            else:
                print("Order not in the menu")
            finished = input("Have you finished ordering?(yes/no):\n")
            if finished == "no":
                next_order = True
            else:
                next_order = False
        print("Here is your order",(customer))
        y = 0
        while y < counter:
            print("Item: ", (my_order[y]))
            print("Cost: $", (my_cost[y]))
            y = y + 1
        print("The total cost of your order is $", (total))
        exit()
    else:
        print("Customer not available in the database: enter customer details")
        customer_data()
        exit()
purchase()
