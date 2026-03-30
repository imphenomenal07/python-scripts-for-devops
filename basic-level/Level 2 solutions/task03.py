# 3️. Print multiplication table of a number

num = int(input("Enter the number: "));
print(f"Table of {num} is")
for i in range(1, 11):
    table=num*i
    print(table)
