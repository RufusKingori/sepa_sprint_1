#This program is used by kings foods and beverages staff to order foods and drinks for it's customers.

#This is the main menu

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
    print("****Welcome to Product operations****" )
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
    if queries_op == 2:
        pass
    if queries_op == 3:
        pass
    elif queries_op == 4:
        pass
    elif queries_op == 5:
        quit()
    else:
        print("Operation not available, Try again")

main()


