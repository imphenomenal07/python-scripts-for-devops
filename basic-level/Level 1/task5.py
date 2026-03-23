# 5️. Swap two numbers with using third variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = num1
num1 = num2
num2 = num3
print(num1, num2)


# Swap two numbers without using third variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = num2, num1
print(num1, num2)
