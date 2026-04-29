# loops in Python

# while loops
# i cant have two variables in a code if you do the second one overides the first one example:
value = 1
value = 2
value = value + 5
print(value)

# if value < 10:
#     print(9)
# elif value < 9:
#     print(8)

while value <100:
    value = value + 1
    print(value)
    if value == 28:
        break
    print(f"this is my current value{value}")

while value <= 10:
    value = value + 1
    if value == 5:
        continue
    print(value)
# + 1 is always added so that python can include the last number

# for loops
# for loops on strings 
word = "photosynthesis"
for x in word:
    print(x)

word2 = "parallelogram" 
for y in word2:
    print(y)

#this is a dict in a list
states_in_nigeria = [{"state": "Abia", "capital": "umuahia",}, {"state": "Enugu", "capital": "enugu",}, {"state": "lagos", "capital": "ikeja",}]
for x in states_in_nigeria:
    print(x)


# names = ["shedrach", "roberta", "stanley", "tomiwa"]
# surnames = ["ogbonna", "king", "igwe", "robert"]

# #for loop in list
# for x in names:
#     print(x)

# for loop on range
for x in range(10):
    print (x)
for x in range(4, 10):
    print (x)

# to loop in 5 
for x in range (0, 100, 5):
    print (x)

# to loop in 100
for x in range(0, 1000, 100):
    print (x)


names = ["shedrach", "roberta", "stanley", "tomiwa"]
surnames = ["ogbonna", "king", "igwe", "robert"]

for x in names:
    if x == "shedrach":
        continue
    if x == "stanley":
        break
    print(x)

# nested loops
for x in names:
    for y in surnames:
        print(x,y)