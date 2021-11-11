
class customer:
    #class for all customers
    def __init__(self):
        self.c_list = []


    def add_customer(self,c_id,c_name,c_address):
        c_id = input("Enter the customer's id")
        c_name = input("Enter the customer's name")
        c_address = input("Enter the customer's address")
        self.c_list.append({"ID":c_id,"name":c_name,"address":c_address})
        #This method adds the customer and it's attributes
        print("ID:",self.c_id,"Name:",self.c_name,"Address:",self.c_address)
        return self.c_list

    def remove_customer(self,c_id,c_name,c_address):
        c_id = input("Enter the customer's id:")
        for i in range(len(self.c_list)):
            if c_id in self.c_list:
                del self.c_list[i]
            return self.c_list


object = customer
object.add_customer()
object.remove_customer()