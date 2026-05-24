#The Flight and Travel Booking Tool

Destinations = {"london": {"number_of_seats":12}, "Paris":{"number_of_seats":9}, "new_york":{"number_of_seats":90}}

while True:
    destination = input("choose your destination")
    seat_to_book= int(input("how many seat"))
    
    if seat_to_book <= Destinations[destination]["number_of_seats"]:
        print("Booking successful")   
        break
    else:
        print("no available ticket")



