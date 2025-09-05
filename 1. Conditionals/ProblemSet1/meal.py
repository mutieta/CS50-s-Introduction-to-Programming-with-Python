def main():
    meal_time = input("What time is it? ")
    meal_time = convert(meal_time)
    if meal_time >= 7 and meal_time <= 8:
        print("breakfast time")
    elif meal_time >= 12 and meal_time <= 13:
        print("lunch time")
    elif meal_time >= 18 and meal_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60 


if __name__ == "__main__":
    main()