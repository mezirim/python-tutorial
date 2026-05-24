#food delivery runner
Restaurants = {
    "avila":{
        "menu":{"chicken":{"price": 5.99}, "rice":{"price": 10.00}, "beans":{"price": 12.00}}
        }, 
    "KFC":{
        "menu":{"fries":{"price": 6.50}, "milkshake":{"price":8.99}, "nuggets":{"price": 3.50}}
        }, 
    "macd":{
        "menu":{"coke":{"price": 3.99}, "Spag":{"price": 15.00}, "water":{"price": 2.50}}
        }
    }

tax = 4.50
delivery = 3.99
cart = []


for x in Restaurants:
    print(x)
while True:
    request = input("choose a restaurant")

    for item, x in Restaurants[request]["menu"].items():
        print(item,x)
    while True:
        choose = input("choose an item")
        if choose == "next":
            break
        price = Restaurants[request]["menu"][choose]["price"]
        order = {"choice":choose, "price":price}
        cart.append(order)
        print(cart)
        

    break  

subtotal = 0
total = 0
for x in cart:
    subtotal = subtotal + x["price"]
    print(subtotal)
total = subtotal + tax + delivery
total = round(total,2)
print("-------Receipt-------")
print(cart)
print("---------------------")
print(f"subtotal{subtotal}")
print(f"total{total}")



        
