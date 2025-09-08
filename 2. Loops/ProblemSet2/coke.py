coins = [25, 10, 5]
amount_due = 50

def main():
    amount = amount_due
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = get_coin()
        if coin is not None:
            amount -= coin
    print("Change Owed:", abs(amount))

def get_coin():
    while True:
        try:
            coin = int(input("Insert Coin: "))
            if coin in coins:
                return coin
            else:
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

main()

