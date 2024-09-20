# Nicholas Norman
# 19 Sep 2024
# elseif.py
# Showcase how to use an elif or else statement

#Take in the users name
name = input("What is your name?: ")

#say hello depending on name
if (name == "Nick"):
    print("What a wonderful name!")

elif (name == "TimBL"):
    print("Hello Tim Berners-Lee, thanks for creating HTML")

elif (name == "Alan Turing"):
    print("Hello Alan Turing, aren't you supposed to be dead?")

else:
    #default cause
    print("Hello {}, it's nice to meet you!".format(name))