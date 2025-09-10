
def main():

    fuel = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        percentage = (x / y) * 100
    except (ValueError, ZeroDivisionError): 
        print("Invalid input")
        return

    main()