# d = {"A":100, 'B':200}
# d["A"] = 400
# print(d)

# d = {'dog' : 'has a tail and goes woof!',
# 'cat' : 'says meow',
# 'mouse' : 'chased by cats'}

# word = input('Enter a word : ')
# print(f' The meaning of the word is: {d[word]}')


# points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
# 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
# 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
# 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

# score = sum([points[c] for c in points ])
# print(score)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# y = car.values()
# z= car.items()
# print(y)
# print(z)

# print(x) #after the change

# x = {'type' : 'fruit', 'name' : 'apple'}

# for y, z in x.items():
#     print(y + ':', z)

#     a = {'name' : 'John', 'age' : '20'}
# b = {'name' : 'May', 'age' : '23'}
# customers = {'c1' : a, 'c2' : b}

# print(customers['c2']['name'])


#while loop

# i = 1
# while i < 6:
#   print(i)
#   if i == 5:
#     break 
#   i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue 
  print(i)