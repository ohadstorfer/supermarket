from enum import Enum


class Actions(Enum):

    PRINT_ALL_PRODUCTS=0
    ADD_TO_CART =1
    SHOW_CART =2
    PAY=3
    EXIT=4



class Product:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock

    def __str__(self) -> str:
        return self.name + ", cost: " +self.price + " ,in stock: " +self.stock    


Cart=[]
Products = [
    {"name": "Apples", "price": 1.99, "availability": 30},
    {"name": "Bread", "price": 2.5, "availability": 20},
    {"name": "Milk", "price": 3, "availability": 0},
    {"name": "Eggs", "price": 1.8, "availability": 40}
]


def menu():
    while(True):
        global students
        while(True):
            for act in Actions: 
                print(f'{act.value}:  {act.name}')
            

            user_input = int(input("Select action: "))
            if user_input < 0 or user_input > 4:
                print("Only numbers from 0 to 4 are allowed.")
                return
            user_selection = Actions(user_input)


            if user_selection == Actions.PRINT_ALL_PRODUCTS:
                for prod in Products: print(prod)

            if user_selection == Actions.ADD_TO_CART:
                yourChoose=int(input("select item: "))
                if yourChoose<0 or yourChoose > 3:
                    print("mefager! only numbers between 0-3! ")
                    return  
                    # need to find a way to make this go back to the menu insted of going out of the run
                choose = Products[yourChoose] 

                if (choose['availability']>=1):              
                    Cart.append(choose)
                else:
                    print("item is not avalible :(")
                

            if user_selection == Actions.SHOW_CART: 
                print(Cart)
                sum =0
                for item in Cart:
                    sum+=item['price']
                print(f"Total cost of items in cart: ${sum}")
                

            if user_selection == Actions.PAY:
                cashORcard = input("do you want to pay with cash or card?  ")
                if cashORcard == "cash" or cashORcard == "card":
                    print("thank you for buying here! now go away!")
                    
                    # Update product availability נותן בעדכונית
                    for item in Cart:
                        for product in Products:
                            if product["name"] == item["name"]:
                                product["availability"] -= 1
                                
                    Cart.clear()  
                else:
                    print("go away you idiot")

            if user_selection == Actions.EXIT: return
                
    
    
if __name__ =="__main__":
    menu()
    