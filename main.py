# This program is used by kings foods and beverages staff to order foods and drinks for it's customers.

import customer
import purchase
import Queries
def main():
    print("*****Welcome to Kings foods and beverages*****")
    print("----------------------------------------------")
    operation = int(input("Choose your operation\n"     #main menu
                          "[1] Customer operations\n"
                          "[2] Product operations\n"
                          "[3] Queries\n"
                          "[4] Exit\n"))
    if operation == 1:
        customer.customer_operation()
    elif operation == 2:
        purchase.product_operation()
    elif operation == 3:
        Queries.queries()
    elif operation == 4:
        print("Thank you")
        exit()
    else:
        print("Please enter one of the options 1, 2, 3 or 4 and try again!")
        main()
main()







