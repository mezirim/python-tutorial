# part 1
number_of_students = 28
cost_per_bus = 45000
number_of_buses = 2
cost_per_meal = 850
number_of_meals = 3
cost_per_ticket = 1250
souvenir_budget_per_student = 500
extra_expenses = 12500

# part 2
total_transportation_cost = cost_per_bus * number_of_buses
print(f"total transport cost {total_transportation_cost}")
total_food = cost_per_meal * number_of_meals * number_of_students
print(f"total food {total_food}")
total_tickets = cost_per_ticket * number_of_students
print(f"total ticket {total_tickets}")
total_souvenirs = souvenir_budget_per_student * number_of_students
print(f"total souvenir {total_souvenirs}")
#Grand Total Cost of the trip
grand_total_cost = total_transportation_cost + total_food + total_tickets + total_souvenirs + extra_expenses
print(f"grand total cost {grand_total_cost}")
#cost per student
cost_per_student = grand_total_cost/number_of_students
print(f"cost per student {cost_per_student}")
#part 3
if grand_total_cost > 250000:
    print("budget is too high! need to reduce expenses")
elif grand_total_cost >= 180000:
    print("budget is acceptable")
else:
    print("great! budget is under control")

# part 4
if number_of_students >= 30:
    print("10% discount on sum")
elif number_of_students>= 25:
    print("5% discount on sum")
else:
    print("no discount")
# FINAL AMOUNT AFTER DISCOUNT
# 5% 
divide = 5/100
diff = 1 - divide
print(diff)
discounted_price_student = cost_per_student * diff
print(discounted_price_student)
print (f"because the number of sudents is greater than 29, you get a 5% discount = {discounted_price_student}")