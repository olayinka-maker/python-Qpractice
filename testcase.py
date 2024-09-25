# #formatted String
# first = "Hello"
# last = "World"
# full = f"{first} {last}"

# print(full)


# #useful string methods
# course = 'Python Programming'
# print(course.upper())
# print(course.strip())
# print(course.title())
# print(course.find("pro"))
# print(course.replace("P","H"))







# #numbers 
# x= 20
# print(bin(x))

# y =0x123e
# print(bin(y))



#Truty and Falsy values 
#Falsy values
#""
#0
#[]
#None(null)


#List Unpacking

numbers = [1,2,3]
first,second,third = numbers 

print(first)

numbers_2 = [1,2,2,3,4,5,5,6,6,7,6]

first,second,*rest ,other= numbers_2

print(other)


letters = ["a","b","c"]

for index,value in enumerate(letters):
    print(index,value)

 #adding an item to a list
letters.append("d")

#adding an item to a list at a particular position
letters.insert(0,"cooked")
print(letters)

#remove an item at the end of a list
letters.pop()
letters.pop(0)

#removing an item but you dont know the index 

letters.remove("b") #removes the first occurence of b in the list 


test= ["1","2","3","4","5"]
# del is used to remove a  range of items 
del test[0:2]
print(test)


#finding the index of a data in a list 


testList =["a","b","c"]
if "d" in testList:
    print(testList.index("b"))


#sorting a List 
lsort = [1,8,9,3,7,2]
lsort.sort()
print(lsort)
print(sorted(lsort,reverse=True))