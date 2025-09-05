
Expression = str(input("Expression: "))
x, y, z = Expression.split(" ")
x = float(x)    
z = float(z)


if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")   
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/" and z != 0:
    print(f"{x / z:.1f}")


