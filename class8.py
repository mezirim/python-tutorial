# basics in Python
# multiple assignment
name, age, gender = "roberta", 27,"male"

name, hobbies, biodata = "roberta", ["dancing", "singing"], {"age": 27, "gender": "female"}

#type keyword in python
#data types is just a type of data
# data types = int, str, booleans(bools), list, dict, tuples
my_name = "shedrach"
age = 23
height = 6.1
condition = True #bools must start with a capital letter
fav_sports = ["dancing", "singing"]

#reassining a list (singing to running)
fav_sports[1] = "running"
fav_sports.append("cooking")

# slicing in list: betwwen two number position
print(fav_sports[1:3])

single_list = ["tomato"] #we can have a single item in a list

print(fav_sports)
print(single_list)

my_dict = {"age": 20, "gemder": "female"}

# learning tuples
# tuples are list with curved brackets.

# DIFFERENCE BETWEEN A TUPLE AND A LIST
#1. readability (u cant chnage the details of a tuple with methods(append, sort)
#2. tuples use () while list use[]
#3. tuples are faster than list
#4. tuples takes less memory than list hence why its fast

fav_hobbies = ("dancing", "singing")
#fav_hobbies[1] = "running" #this wont run cause u can't modify a tuple
numbers = (1,2,3,4,5)
mixed_list = (1, "Roberta", 9.0)
print(fav_hobbies)

# a tuple cannot have a single element
# when a tuple have just a single element, it does not take the data type tuple, rather it takes an int, str, float, etc
single_tuple = (6,)
print(single_tuple)


#indexing in tuples
# indexing in tuples is the sames as on list (is used in getting an item on a list or tuples using numbers
print(numbers[2])
print(numbers[-2])

#slicing in tuples
print(numbers[1:4])
#it doesnt print the last number unless + 1 is added

#unpacking using tuples (very powerful)
name, age, gender = ("shedrach", 20, "male")
print (name, age, gender)


# example of unpacking in tuples and list 
def get_coordinates():
    return (10,20)

a,b = get_coordinates()

print(a)
print(b)

# concatenating tuples and list
tuple1 = (1,2)
tuple2 = (3,4)
concat_tuple = tuple1 + tuple2
print(concat_tuple)


# converting tuples to list and vice versa
# list and tuple is a keyword
list1 = list(tuple1)
print(list1)

tuple_to_list = tuple(list1)
print(tuple_to_list)

print(type(my_name))
print(type(age))
print(type(height))
print(type(condition))
print(type(fav_sports))
print(type(my_dict))
print(type(fav_hobbies))
print(type(single_tuple))


# comparing true and false 
print (True and True)
print (True and False)
print (False and True)
print (False and False)

# pow (is used in place of **, first one is base nmber second one is power number and the third is to get the remainder after division of the first two by the third number)
# (the percentage or the 3rd number when using pow just prints out the remainder)
print(10 % 3)
print(pow(2,4))
print(pow(5,4))
print(pow(5,4,4))
