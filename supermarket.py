from enum import Enum
import json
import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

class Actions(Enum):
    PRINT_ALL_PRODUCTS = 0
    ADD_TO_CART = 1
    SHOW_CART = 2
    PAY = 3
    EXIT = 4

import json

def load_products_from_json(filename):
    try:
        with open(filename, 'r') as file:
            products_data = json.load(file)
            Products.extend(products_data)
            # print("Products loaded successfully from JSON.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'.")

class Product:
    def __init__(self, name, price, stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        return f"{self.name}, cost: {self.price}, in stock: {self.stock}"

Cart = []
Products = []

def menu():
    while True:
        global students
        while True:
            for action in Actions:
                print(f'{action.value}: {action.name}')

            moveON = True  
            while moveON:
                user_input = input("Select action: ")

                if user_input.isdigit():
                    user_input = int(user_input)

                    if 0 <= user_input <= 4:
                        moveON = False  
                    else:
                        print("Only numbers from 0 to 4 are allowed.")
                        logging.error(f'User entered an invalid number: {user_input}')
                else:
                    print("Invalid input! Please enter a valid number.")
                    logging.error(f'User entered an invalid input: {user_input}')



            user_selection = Actions(user_input)

            if user_selection == Actions.PRINT_ALL_PRODUCTS:
                for product in Products:
                    print(product)

            if user_selection == Actions.ADD_TO_CART:
                canMoveOn= True

                while canMoveOn:
                    selected_item_index = input("Select item: ")
                    if selected_item_index.isdigit():
                        selected_item_index = int(selected_item_index)

                        if selected_item_index < 0 or selected_item_index > 3:
                            print("Invalid input! Please choose a number between 0-3.")
                            logging.error(f'User entered an invalid number: {selected_item_index}')
                        else:
                            selected_product = Products[selected_item_index]
                            print("item added to cart")
                            canMoveOn=False

                    else:
                        print("Invalid input! Please enter a valid number.")
                        logging.error(f'User entered an invalid input: {user_input}')

                if selected_product['availability'] >= 1:
                    Cart.append(selected_product)
                    logging.debug(f'User succeeded in adding {selected_product} to the cart')
                else:
                    print("Item is not available :(")
                    logging.debug(f'User failed to add {selected_product} to the cart because the item is not available')

            if user_selection == Actions.SHOW_CART:
                print(Cart)
                total_cost = 0
                for item in Cart:
                    total_cost += item['price']
                print(f"Total cost of items in cart: ${total_cost}")

            if user_selection == Actions.PAY:
                payment_method = input("Do you want to pay with cash or card? ")
                if payment_method == "cash" or payment_method == "card":
                    print("Thank you for buying here! Now go away!")
                    logging.debug(f'User paid successfully')
                    for item in Cart:
                        for product in Products:
                            if product["name"] == item["name"]:
                                product["availability"] -= 1
                    Cart.clear()
                else:
                    logging.error(f'User entered an invalid payment method: {payment_method}')
                    print("Go away, you idiot!")

            if user_selection == Actions.EXIT:
                return

if __name__ == "__main__":
    load_products_from_json("cart.JSON")
    menu()



# רשימה למחר:
# לדאוג לפוקצייה PAY 
# כלומר שיהיה אפשר לנסות שוב להכניס ערך אחרי שהיוזר הכניס ערך לא נכון
# להשמיש את הקובץ ג'ייסון ככה שהוא יתעדכן, כולל אחרי רכישה שיתעדכן המלאי
# להעביר את כל הפונקציות לדף נפרד
