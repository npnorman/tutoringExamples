# Nicholas Norman
# 19 Sep 2024
# nested.py
# Showcase nested ifs


#When the statements or dependent on each other, use nested if statements

username = input("username (hint npn): ")
password = input("password (hint 123): ")

if (username == "npn"):
    if (password == "123"):
        print("Entering the matrix")
    else:
        print("Incorrect password")
else:
    print("incorrect username and password")