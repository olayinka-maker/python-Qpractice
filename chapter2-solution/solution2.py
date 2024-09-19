# 1. Write a program that asks the user to enter a word and then prints that word 25 times (each on
# separate lines).

word = input("Enter a Word : ")
for i in range(25):
    print(word)

# 2. Write a program that asks the user to enter a word and then prints that word 200 times, each on the
# same line.
newword = input("Enter a Word : ")
for i in range(200):
    print(newword,end=' ')

# 3. Write a program that uses a for loop to print the numbers 5, 6, 7, 8, 9, . . . 89, 90, all on the same line
# separated by spaces.

for i in range(5,91):
    print(i,end=' ')

# 4. Write a program that uses a for loop to print 2, 6, 10, 14, 18, . . . , 98, 102, all on the same line separated
# by spaces.

for i in range(2,103,4):
    print(i,end='  ')



# 5. Write a program that uses a for loop to print 29, 28, 27, 26, 26, . . . , 5, 4, all on the same line separated
# by spaces.


for i in range(29,3,-1):
    print(i,end='  ')

# 6. Write a program that uses a for loop to print the output below:
# 1. A
# 2. A
# 3. A
# 4. A
# 5. A

for i in range(1,6):
    print(i,'. A')

# 7. Write a program that uses a for loop to print out the first 20 perfect squares, all on the same line. The
# first few are 1, 4, 9, 16, 25, . . . .


for i in range(1,6):
    print(i**2)

# 8. Write a program that uses for loops to print out 40 A’s followed by 50 B’s, all on the same line.

for i in range(40):
    print("A",end=' ')
for i in range(50):
    print('B',end=' ')

# 9. Write a program that uses a for loop to print out ABCABCABC. . . , where ABC repeats 100 times. Print
# this all on the same line.

for i in range(100):
    print("ABC",end=' ')


# 10. Write a program that uses exactly three for loops to print the output below. It has 10 A’s, followed by
# 5 copies of BCD, followed by one E, followed by 15 F’s.

for i in range(10):
    print("A",end='')
for i in range(5):
    print('BCD',end='')
for i in range(1):
    print("E",end='')
for i in range(15):
    print('F',end='')

# 11. Write a program that asks the user to enter a number and then prints out the letter A that many times,
# all on the same line.

user_number = eval(input("Enter a Number : "))
for i in range(user_number):
    print('A')

# 12. Write a program that uses a loop and an input statement to ask the user to enter 10 numbers. After
# each number is entered, print out the square of that number.

for i in range(10):
    user_val = eval(input("Enter a Number : "))
    print(user_val**2)

# 13. Write a program that asks the user to enter a height and then draws a box like the one below that is
# 10 asterisks wide and as tall as specified by the user.
# **********
# **********
# **********
# **********


height = eval(input("Enter a Height : "))
for i in range(height):
    print('**********')


#14 print big C
size = eval(input('Enter size: '))
for i in range(size):
    print('*', end='')
print()    
for i in range(size-2):
    print('*')
for i in range(size):
    print('*', end='')
print()  

