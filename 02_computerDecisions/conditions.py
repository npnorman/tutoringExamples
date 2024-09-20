# Nicholas Norman
# 19 Sep 2024
# conditions.py
# Showcase how a condition evaluates and logic

#booleans
    #typically we start boolean statements with "is"
isCorrect = True

#relation operators

x = 5
y = 10

isEqual = x == y

isLessThan = x < y

isGreaterThan = x > y

isLessThanOrEqual = x <= y

isGreaterThanEqual = x >= y

print("Relational Operators: ")
print(f"{x} is equal to {y}: {isEqual}")
print(f"{x} is less than {y}: {isLessThan}")
print(f"{x} is greater than {y}: {isGreaterThan}")
print(f"{x} is less than or equal to {y}: {isLessThanOrEqual}")
print(f"{x} is greater than or equal to {y}: {isGreaterThanEqual}")

#comparing a string

name = "Nick"
isNick = name == "Nick"

print("\nString comparison:")
print(f"{name} is equal to 'Nick'")

#logic table (and, or, not)

p = True
q = False

print(f"p={p} q={q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not (p and q): {not (p and q)}")
print(f"not (p or q): {not (p or q)}")
print(f"note: this is not the same as")
print(f"not p and q {not p and q}")