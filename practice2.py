# personal expense tracker 
budget = 500000000
expenses = []
total_spent = 0
total_price = 0

while True:
    item = input("wat do you want")
    if item == "done":
        break
    try:
        price = int(input(f"how much does {item} cost"))  
        each_item = {"name":item, "price":price}
        total_price = total_price + price
        if total_price >= budget:
            print("budget exceeded")
            break 
        else:
            expenses.append(each_item)
    except ValueError:
        print("invalid input")


for x in expenses:#x or item
    total_spent = total_spent + x["price"]
print(f"your total spent is {total_spent}")

if total_spent > budget:
    print("insufficient balance")
else:
    balance = budget - total_spent
    print(f"your balance is {balance}")