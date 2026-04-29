import random
#part 1
product = ["crisps", "water", "candy", "redbull", "biscuit", "book"]
stock = {"crisps":5,"water":20,"candy":2,"redbull":6,"biscuit":15,"book":17}
price = {"crisps":2,"water":3,"candy":4,"redbull":7,"biscuit":10,"book":5}
student_grade = [40,50,60,60,70,80,90,97]

#part 2
print(len(product))
product.append("pen")
product.append("pencil")
print (product)
stock["pen"] = 12
stock["pencil"] = 4
price["pen"] = 15
price["pencil"] = 11
print (stock)
print (price)
product.pop(-6)
print (product)
product.sort()
print (product)

#part 3
rnd_num = random.randint(0,5)
print(rnd_num)

total_crisps_sales =0
rotal_water_sales = 0
total_candy_sales = 0
total_biscuit_sales = 0
total_book_sales = 0
total_pen_sales =0
total_pencil_sales =0

# crips
print (f"crips stock amt {stock["crisps"]}")
if stock["crisps"] > rnd_num:
    print("sell stock")
    # to reduce stock
    stock["crisps"] = stock["crisps"] - rnd_num
elif stock == 0:
    print("out of stock")
else:
    print("sell only what is left")
    stock["crisps"] = 0
    
# water
print (f"water stoct amt {stock['water']}")
if stock["water"] > rnd_num:
     print("sell stock")
     stock["water"] = stock["water"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     total_water_sales = price["water"] * stock["water"]
     stock["water"] = 0
print(stock)

# candy
print (f"candy stoct amt {stock['candy']}")
if stock["candy"] > rnd_num:
     print("sell stock")
     stock["candy"] = stock["candy"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     stock["candy"] = 0
print(stock)

# redbull
print (f"redbull stoct amt {stock['redbull']}")
if stock["redbull"] > rnd_num:
     print("sell stock")
     total_redbull_sales = price["redbull"] * rnd_num
     stock["redbull"] = stock["redbull"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     total_redbull_sales = price["redbull"] * stock["redbull"]
     stock["redbull"] = 0
print(stock)

# biscuit
print (f"biscuit stoct amt {stock['biscuit']}")
if stock["biscuit"] > rnd_num:
     print("sell stock")
     stock["biscuit"] = stock["biscuit"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     stock["biscuit"] = 0
print(stock)

# book
print (f"book stoct amt {stock['book']}")
if stock["book"] > rnd_num:
     print("sell stock")
     stock["book"] = stock["book"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     stock["book"] = 0
print(stock)

# pen
print (f"pen stoct amt {stock['pen']}")
if stock["pen"] > rnd_num:
     print("sell stock")
     stock["pen"] = stock["pen"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     stock["pen"] = 0
print(stock)

# pencil
print (f"pencil stoct amt {stock['pencil']}")
if stock["pencil"] > rnd_num:
     print("sell stock")
     stock["pencil"] = stock["pencil"] - rnd_num
elif stock == 0:
     print("out of stock")
else:
     print("sell only what is left")
     total_pencil_sales = price["pencil"] * rnd_num
     stock["pencil"] = 0
print(stock)


total_revenue = total_redbull_sales + total_crisps_sales + total_biscuit_sales + total_pencil_sales + total_candy_sales + total_water_sales + total_book_sales + total_pen_sales
print(f"total revenue generated ${total_revenue}")
print(f"total stock left {stock}")
# part 4
def analyze_grades(student_grade):
        if student_grade >= 90:
            print ("excellent")
        elif student_grade >= 80:
            print ("very good")
        elif student_grade >= 70:
             print ("good")
        elif student_grade >= 60:
            print ("pass")
        else:
            print ("needs improvement")
analyze_grades(65)