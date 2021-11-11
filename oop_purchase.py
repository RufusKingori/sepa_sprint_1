
class product:
    #class for all customers
    def __init__(self):
        self.p_list = []


    def add_product(self,p_id,p_name,p_quantity,p_price):
        p_id = input("Enter the product's id")
        p_name = input("Enter the product's name")
        p_quantity = input("Enter the product's quantity")
        p_price = input("Enter the product's price")
        self.p_list.append({"ID":p_id,"name":p_name,"quantity":p_quantity,"price":p_price})
        #This method adds the customer and it's attributes
        print("ID:",self.p_id,"Name:",self.p_name,"quantity:",self.p_quantity,"price:",self.p_price)
        return self.p_list

    def remove_product(self,p_id,p_list):
        p_id = input("Enter the product's id")
        for i in range(len(self.p_list)):
            if p_id in self.p_list:
                del self.p_list[i]
            return self.p_list


object = product
object.add_product()
object.remove_product()