from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('============================')
    print('==========Welcome!==========')
    print('========Weed Market=========')
    print('============================')

    print('Select a option: ')
    print('1 - Register a product')
    print('2 - List products')
    print('3 - Buy a product')
    print('4 - Show cart')
    print('5 - Close order')
    print('6 - Exit')

    option = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        show_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Ckeck back often!')
        sleep(2)
        exit(0)
    else:
        print('Ivalid input')
        sleep(1)
        menu()


def register_product() -> None:
    print('Product register')
    print('----------------')
    name: str = input('Input the product name: ')
    price: float = float(input('Input the price: '))
    product = Product(name, price)
    products.append(product)

    print(f"The product '{product.name}' was registeres successfully")
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Product list')
        print('=============')
        for line in products:
            print(line)
            print('--------------------')
            sleep(1)
    else:
        print("There aren't product registered yet")
    sleep(1)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Input the product code: ')
        print('------------------')
        print('Available products: ')
        for line in products:
            print(line)
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product:
            if len(cart) > 0:
                is_in_cart: bool = False
                for item in cart:
                    quant = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(
                            f'The product {product.name} has {quant + 1} units in cart')
                        is_in_cart = True
                        sleep(2)
                        menu()
                if not is_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} wad added to the cart')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} was added')
                sleep(2)
                menu()
        else:
            print(f"The code {code} could'n be found")
            sleep(1)
            menu()

    else:
        print("There aren't product registered yet")
        sleep(1)
        menu()


def show_cart() -> None:
    if len(cart) > 0:
        print("Products in cart: ")
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                sleep(1)
    else:
        print("There aren't product registered yet")
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Cart Products:')
        for line in cart:
            for data in line.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
            print('--------------------------')
            sleep(1)
        print(f'Your invoice is {format_float_str_currency(total_value)}')
        print('Check back often')
        cart.clear()
        sleep(5)
    else:
        print("There aren't product registered yet")
    sleep(1)
    menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None

    for line in products:
        if line.cod == code:
            p = line
    return p


if __name__ == '__main__':
    main()
