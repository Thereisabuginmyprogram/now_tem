tem = (input("Enter temperatures: "))
unit = tem[-1:].upper()
degree = int(tem[:-1])
if unit == "C": # to f
    degree = ((9 * degree) / 5) + 32
    unit = "F"
    print(str(int(degree)) + unit)
elif unit == "F": # to c
    degree = ((degree - 32) / 9) * 5
    unit = "C"
    print(str(int(degree)) + unit)
else:
    print("Wrong input")