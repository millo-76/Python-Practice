#sep 2nd into to python

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))

def compare_values(a, b):
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"

result = compare_values(var1, var2)
print(f"Comparison result: {result}")
