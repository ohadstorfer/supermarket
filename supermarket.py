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

def load_products_from_json(filename):
    try:
        with open(filename, 'r') as file:
            products_data = json.load(file)
            return products_data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'.")

def save_products_to_json(filename, products):
    try:
        with open(filename, 'w') as file:
            json.dump(products, file, indent=4)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'.")


Cart = []
Products = load_products_from_json("cart.JSON")

def menu():
    while True:
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
                    print(f"{product['name']} - {product['price']}")


            if user_selection == Actions.ADD_TO_CART:
                canMoveOn = True

                while canMoveOn:
                    selected_item_index = input("Select item: ")
                    if selected_item_index.isdigit():
                        selected_item_index = int(selected_item_index)

                        if 0 <= selected_item_index < len(Products):
                            selected_product = Products[selected_item_index]
                            if selected_product['availability'] >= 1:
                                Cart.append(selected_product)
                                selected_product['availability'] -= 1
                                print("Item added to cart")
                                logging.debug(f'User added {selected_product} to the cart ')
                                canMoveOn = False
                            else:
                                print("Item is not available :(")
                                logging.debug(f'User failed to add {selected_product} to the cart because the item is not available')
                        else:
                            print("Invalid input! Please choose a number between 0 and {len(Products) - 1}.")
                            logging.error(f'User entered an invalid number: {selected_item_index}')
                    else:
                        print("Invalid input! Please enter a valid number.")
                        logging.error(f'User entered an invalid input: {user_input}')

            if user_selection == Actions.SHOW_CART:
                for item in Cart:
                    print(f"{item['name']} - {item['price']}")
                total_cost = sum(item['price'] for item in Cart)
                print(f"Total cost of items in cart: ${total_cost}")

            if user_selection == Actions.PAY:
                good = True
                while good: 
                    payment_method = input("Do you want to pay with cash or card? ")
                    if payment_method == "cash" or payment_method == "card":
                        print("Thank you for buying here! Now go away!")
                        logging.debug(f'User paid successfully')
                        for item in Cart:
                            for product in Products:
                                if product["name"] == item["name"]:
                                    product["availability"] -= 1
                        Cart.clear()
                        save_products_to_json("cart.JSON", Products)
                        good= False
                    else:
                        logging.error(f'User entered an invalid payment method: {payment_method}')
                        print("Invalid input! Please enter only 'cash' or 'card' ")

            if user_selection == Actions.EXIT:
                save_products_to_json("cart.JSON", Products)
                return



if __name__ == "__main__":
    menu()
