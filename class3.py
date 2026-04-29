# function without an arguement
def greet ():
    print("good morrning")


greet()   

#function with an arguement
def greet (name,age,colour):
    print(f"good morning {name} iam {age} years old, her best colour is {colour}")

greet("roberta",22,"pink")


# class note
name = "shedeach" 
age = 22
occupation = "farmer"
height = 6

# function without an arg
my_sentence = f"{name} is age {age} and he is a {occupation}"
print(my_sentence)
# f keyword converts everything written after it into a string. and everytime is used in variables the coily braces must be added
# function with an arg
def greet(name, age, color):
    print(f" good morning {name}")
    print (f" i am age {age}")
    print (f" my fav color is {color}")

greet("shedrach", "22", "black") 

# inputs
# name = input("what is your name")
age = int(input("how old are you"))
print (f"i am {age + 2} years old")

# converting number to string = str()
# converting string to number = int()

# basic operators in python
# addition = +
# subtraction = -
# division = /
# multiplication = *
# exponential = **

# conditional operators
# greater than = > 
# lesser than = <
# greater than or equal to = >=
# lesser than or equal to = <=
#  equal to  ==
# and keyword, or keyword, not keyword, f keyword, type keyword


# add
sum = 2 + 3
print(sum)

# minus
diff = 4 - 1
print(diff)

# divide
divide = 8/2
print(divide)

# multiply
product = 8*2
print(product)

# exponentials
square = 5**2
print(square)

weight = 90
a = "one"
b = "one"
print(f"{weight + 10}")
print (f"{a + b}")
print(f"Iam {2 +2 +3 -5}")
