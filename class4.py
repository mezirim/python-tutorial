# manipulating lists
fruits = ["mango", "orange", "grapes", "strawberry"]

# accessing the first item on the list
print(fruits[0])

# accessing the 2nd and 3rd item on the list
print(fruits[1], fruits[2])

# accessing the last item on the list 
print(fruits[-1])

# accessing the 2nd to the last item on the list
print(fruits[-2])

# getting the total number of fruits in the list
print(len(fruits))


# understanding methods
age = 14
age_to_string = str(age)

weight = "90" 
weight_to_int = int(weight)

# functions in python are generally written like this apple(), sum()
# methods in python are generally written like this .name()

# adding an item to a list
fruits.append("kiwi")

# adding an item to a specific position
fruits.insert(0, "kiwi")

# removing from a list
fruits.remove("mango")

# removing from a particular position
fruits.pop(-4)

# reversing a list
fruits.reverse()

# sorting a list
fruits.sort()

#reassigning in list
fruits[1] = "orange"

# Dictionaries
student = {"name": "Roberta", "course": "python", "grades": [90, 40, 60], "name": "sheezy", "active": True}
print(student["name"])
print(student["course"])
print(student["grades"])
print(student["active"])

# manipulating dicts

# adding to the dicts
student["height"] = "170cm"

# removing from a dict
student.pop("active")

# methods in dict
print(student.keys())
print(student.values())
print(student)

# conditional rendering - if and elif statements
grade = 35

if grade >= 100:
    print("A++ kid")
elif grade > 70:
    print("A")
elif grade >50:
    print("c")
else:
    print("this is a failure")

height = 100
width = 200
length = 0

if height > 90 and width < 201:
    print("big")
elif height >= 50 and width <= 80:
    print("meduim")
else: 
    print("small")

if height > 90 or width >= 200:
    print("nice size")
elif height < 90 or width < 200:
    print("nice small")
else:
    print("id manage")

if height >= 100 or width >= 200:
    print("cool")
elif height > 90 or width > 190:
    print("still cool")
else:
    print("well")

if height == 0:
    print("wow you are short")
else:
    print("what is your height")

if not length:
    print("true")
else:
    print("false")