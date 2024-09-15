# 1. Use several print statements to print out a triangle that looks exactly like the one below.
print('*')
print('**')
print('***')
print('****')


# 2. Use several print statements to print out the letter A exactly like the one below.
print('    *')
print('   *  *')
print('  ******')
print(' *       *')
print('*         *')



# 3. Write a line of code that computes and prints out the result of the computation 14 · 12
# 33 · 144 − 187

print((14*12) / (33*144 - 187))


# 4. Write a program that asks the user to enter a distance in kilometers and then prints out how far that
# distance is in miles. There are 0.621371 miles in one kilometer

distance = eval(input("Enter A Distance is Kilometers : "))
print("The Equivalent of your inputted distance in miles is :", 0.621371*distance)

# 5. Write a program that asks the user to enter their name. Then print out the user’s name three times on
# the same line

user_name = input("Enter Your Name : ")
print(user_name,end='')
print(user_name,end='')
print(user_name)

# 6. Write a program that asks the user to enter two numbers (you’ll probably want to use separate input
# statements for that). Then print out the result of adding those two numbers.

num1 = eval(input("Enter the first number : "))
num2 = eval(input("Enter the second number : "))

print('The Sum of your inputs is :', num1 + num2)



# 7. The Body Mass Index, BMI, is calculated as
# BMI =
# 703w
# h
# 2
# ,
# where w is the person’s weight in pounds and h is the person’s height in inches. Write a program that
# asks the user for their height their weight and prints out their BMI. [Note: one way to compute h
# 2
# is
# as h · h.]


weight =  eval(input("Enter Your Weight : "))
height =  eval(input('Enter Your Height : '))
print('BMI =', (750*weight)/(height*height))

# 8. Write a program that asks the user to enter five numbers (use five input statements). Then print out
# those numbers all on the same line, with each number separated from the others by exactly three
# spaces. Use the sep optional argument to the print statement to do this.

num1 = eval(input("Enter number 1 : "))
num2 = eval(input("Enter number 2 : "))
num3 = eval(input("Enter number 3 : "))
num4 = eval(input("Enter number 4 : "))
num5 = eval(input("Enter number 5 : "))

print(num1,end='   ')
print(num2,end='   ')
print(num3,end='   ')
print(num4,end='   ')
print(num5,end='   ')




# 9. Write a program that asks the user to enter a number. Store that number in a variable. Add 2 to that
# number, store the result in the same variable, and then print out the value of that variable

numberQ = eval(input("Enter a Number : "))
result = numberQ + 2
print(result)