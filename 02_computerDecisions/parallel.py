# Nicholas Norman
# 19 Sep 2024
# parallel.py
# Showcase parallel ifs

#When the statements are independent of each other, use parallel if statements

print("Lets check if the two numbers add up to 12 and if they multiply to 20")

x = input("x: ")
x = int(x)

y = input("y: ")
y = int(y)

if (x + y == 12):
    print("x + y is equal to 12")

if (x * y == 20):
    print("x * y is equal to 20")