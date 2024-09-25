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


# 4. The distance between two numbers on the number line is the absolute value of the difference of the
# two numbers. For instance, the distance between 3 and 7.2 is |3 − 7.2| = 4.2. Write a program that
# asks the user for two numbers and prints out the distance between them.

first_number = eval(input("Enter The First Number : "))
second_number = eval(input("Enter The Second Number: "))

abs_diff = abs(first_number-second_number)
print(abs_diff)

# 5. Write a program that asks the user to enter a positive number and then prints out the square root of
# that number rounded to 2 decimal places.

from math import sqrt

positive_number = eval(input("Enter a POsitive Number : "))
print(round(sqrt(positive_number,2)))


# 6. Write a program that prints out the numbers from 1 to 20 and their square roots, rounded to 4 decimal
# places, with the square root of the number being on the same line as the number.

from math import sqrt

for i in range(1,21):
    print(i, round(sqrt(i), 4))