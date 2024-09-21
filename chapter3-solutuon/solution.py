#1. Write a program that asks the user for two numbers x and y and then prints out the result of x^y

x = int(input("Enter a  number for X:"))
y = int(input("Enter a  number for Y:"))

print(x**y)

# 2. Write a program that does the following computation in Python: 9 + 3
# 8 − 2
# . The result should come out
# to 2. Be careful about order of operations

print((9+3)//(8-2))

# 3. Some board games require you to reduce the number of cards you are holding by half, rounded
# down. For instance, if you have 10 cards, you would reduce to 5 and if you had 11 cards you would
# also reduce to 5. With 12 cards you would reduce to 6. Write a program that asks the user to enter
# how many cards they have and print out what their hand would reduce to under this rule.


user_card_no = int(input("How Many Cards Do you have with you? "))
print(round(user_card_no//2))