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

# numbers = [1,2,3]
# first,second,third = numbers 

# print(first)

# numbers_2 = [1,2,2,3,4,5,5,6,6,7,6]

# first,second,*rest ,other= numbers_2

# print(other)


# letters = ["a","b","c"]

# for index,value in enumerate(letters):
#     print(index,value)

#  #adding an item to a list
# letters.append("d")

# #adding an item to a list at a particular position
# letters.insert(0,"cooked")
# print(letters)

# #remove an item at the end of a list
# letters.pop()
# letters.pop(0)

# #removing an item but you dont know the index 

# letters.remove("b") #removes the first occurence of b in the list 


# test= ["1","2","3","4","5"]
# # del is used to remove a  range of items 
# del test[0:2]
# print(test)


# #finding the index of a data in a list 


# testList =["a","b","c"]
# if "d" in testList:
#     print(testList.index("b"))


# #sorting a List 
# lsort = [1,8,9,3,7,2]
# lsort.sort()
# print(lsort)
# print(sorted(lsort,reverse=True))


#lamda expression or function

# x = lambda a : a + 2
# print(x(5))

# #multiple args 
# x = lambda a,b,c: a +b+c+ 2 
# print(x(5,3,4))


# #using lambda with  map functon
# items = [("prd1",10),("prd3",10),("prd2",12)]
# for item in items:
#     print(item)
# data = list(map(lambda item : item[1], items))
# print(data)


# #filter with lambda
# items = [("prd1",10),("prd3",9),("prd2",12)]
# for item in items:
#     if(item[1] >= 10):
#         print(item[1])



# ## now using filter function

# filteredData = list(filter( lambda item : item[1] >= 10,items))
# print(filteredData)

# ##using list comprehesion to achieve the tsk above
# newFilteredData = [item for item in items if item[1] >= 10]
# print(f"data ${newFilteredData}")


# #list Comprehension

# filteredData = [item[1] for item in items]
# print(filteredData)


# list1 =  [1,2,3]
# list2 = [10,20,30]

# x = zip("aeebc",list1,list2)
# print(list(x))

# #stack in python
 
# testlist = [1,2,3]
# print(testlist[-1])


# #queue

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if  not queue:
#     print("empty")

# #dictionary examples
# d = {'dog' : 'has a tail and goes woof!',
# 'cat' : 'says meow',
# 'mouse' : 'chased by cats'}

# word = input('Enter a word : ')
# print('The definition is:', d[word])



# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
# 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
# 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
# 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
# score = sum([points[c] for c in points])
# print(score)


# deck = [{'value':i, 'suit':c}
# for c in ['spades', 'clubs', 'hearts', 'diamonds']
# for i in range(2,15)]

# prin = deck[0]["value"]
# print(deck)


# d = {'A':100, 'B':200,'C':100,}
# value = [x[1] for x in d.items() if x[1] == 100 ]
# print(value)


