def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    number_found = False
    for i in range(len(s)):
        if s[i].isdigit():
            number_found = True
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
        elif not s[i].isalnum():
            return False
    if number_found and s[-1].isalpha():
        return False
    return True


main()