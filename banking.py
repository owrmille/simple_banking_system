import random
import sqlite3

CREATE_CARD_TABLE = "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT UNIQUE, pin TEXT, balance INTEGER DEFAULT 0);"
DROP_TABLE = "DROP TABLE IF EXISTS card;"

INSERT_CARD = "INSERT INTO card (number, pin) VALUES (?, ?);"
GET_ALL_CARDS = "SELECT * FROM card;"
DELETE_CARD = "DELETE FROM card WHERE number = ? AND pin = ?;"

ADD_BALANCE = "UPDATE card SET balance = balance + ? WHERE number = ?;"
DELETE_MONEY = "UPDATE card SET balance = balance - ? WHERE number = ?;"

GET_BALANCE_BY_CARD = "SELECT balance FROM card WHERE number = ? AND pin = ?;"
GET_CARD_BY = "SELECT * FROM card WHERE number = ? AND pin = ?;"
GET_CARD_BY_NUMBER = "SELECT * FROM card WHERE number = ?"

def create_tables(connection):
    with connection:
        connection.execute(CREATE_CARD_TABLE)

def drop_tables(connection):
    with connection:
        connection.execute(DROP_TABLE)

def add_card(connection, number, pin):
    with connection:
        connection.execute(INSERT_CARD, (number, pin))

def delete_card(connection, number, pin):
    with connection:
        connection.execute(DELETE_CARD, (number, pin))

def add_money(connection, money, number):
    with connection:
        return connection.execute(ADD_BALANCE, (money, number))

def delete_money(connection, money, number):
    with connection:
        return connection.execute(DELETE_MONEY, (money, number))

def get_all_cards(connection):
    with connection:
        return connection.execute(GET_ALL_CARDS).fetchall()

def get_card_inf_by(connection, number, pin):
    with connection:
        return connection.execute(GET_CARD_BY, (number, pin)).fetchall()

def get_card_by_number(connection, number):
    with connection:
        return connection.execute(GET_CARD_BY_NUMBER, (number, )).fetchall()

def print_menu():
    print('1. Create an account', '2. Log into account', '0. Exit', sep='\n')

def print_log_menu():
    print('1. Balance', '2. Add income', '3. Do transfer', '4. Close account', '5. Log out', '0. Exit', sep='\n')

def algorithm(nums2):

    for i in range(1, 10):
        if i % 2 != 0:
          nums2[i-1] *= 2
        if nums2[i-1] > 9:
          nums2[i-1] -= 9

    s = (8 + sum(nums2)) % 10

    return s

def Luhn_algorithm(nums):
    nums2 = nums.copy()
    s = algorithm(nums2)

    if s != 0:
        nums.append(10 - s)
    else:
        nums.append(0)

    return nums

def check_Luhn_algorithm(nums):
    nums2 = nums.copy()
    s = algorithm(nums2)

    if s != 0:
        return 0
    else:
        return 1

def create_card():
    nums = Luhn_algorithm([random.randint(0, 9) for i in range(9)])
    number = '400000' + ''.join(list(map(str, nums)))
    pin = ''.join(list(map(str, [random.randint(0, 9) for i in range(4)])))
    add_card(connection, number, pin)

    return get_card_inf_by(connection, number, pin)[0]

def transfer(card_inf):
    print('Enter card number:')
    transfer_card = input()
    nums = list(map(int, transfer_card))[6:]

    if check_Luhn_algorithm(nums) != 0:

        try:
            a = get_card_by_number(connection, transfer_card)[0]
            print('Enter how much money you want to transfer:')
            money = int(input())

            if get_card_by_number(connection, card_inf[1])[0][3] < money:
                print('Not enough money!')

            else:
                add_money(connection, money, transfer_card)
                delete_money(connection, money, card_inf[1])
                print('Success!')
        except:
            print('Such a card does not exist.')

    else:
        print('Probably you made mistake in card number. Please try again!')

def log_menu(card_inf):
    print_log_menu()
    command = int(input())

    log_menu_commands = [1, 2, 3]

    if command == 1:
        print('Balance:', get_card_inf_by(connection, card_inf[1], card_inf[2])[0][3], ' ', sep='\n')

    elif command == 2:
        print('Enter income:')
        money = int(input())
        add_money(connection, money, card_inf[1])
        print('Income was added!')

    elif command == 3:
        transfer(card_inf)

    elif command == 4:
        delete_card(connection, card_inf[1], card_inf[2])
        print('The account has been closed!')

    elif command == 5:
        print('You have successfully logged out!', ' ', sep='\n')

    elif command == 0:
        print('Bye!')
        return

    if command in log_menu_commands:
        log_menu(card_inf)
    else:
        menu()

def menu(card_inf=[]):
    print_menu()
    command = int(input())

    if command == 0:
        print('Bye!')

    elif command == 1:
        card_inf = create_card()
        print('Your card has been created', 'Your card number:', card_inf[1], 'Your card PIN:', card_inf[2], ' ', sep='\n')
        menu(card_inf)

    elif command == 2:
        print('Enter your card number:')
        input_card = input()
        print('Enter your PIN:')
        input_pin = input()

        try:
            card_inf = get_card_inf_by(connection, input_card, input_pin)[0]
            print('You have successfully logged in!', ' ', sep='\n')
            log_menu(card_inf)
        except:
            print('Wrong card number or PIN!', ' ', sep='\n')
            menu(card_inf)


connection = sqlite3.connect("card.s3db")
drop_tables(connection)
create_tables(connection)
menu()


