from datetime import date
# Digital Secret Library


secret_password = "book"
trial = 0
entry = []

while True:
    user_password = input("what's your secret password")
    
    if user_password == secret_password:
        while True:
            user_choice = input("A(new entry),or B(old entry)")
            if user_choice == "A":
                new_entry = input("input new entry")
                entry_date = {"new_entry": new_entry, "Tdate" : date.today()}
                entry.append(entry_date)
            elif user_choice == "B":
                print(entry)
            else:
                break
    else:
        trial = trial + 1
        if trial == 3:
            print("youre logged out") 
            break
        continue
    break