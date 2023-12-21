import json

# If the address changes, enter the new address
# Read the file json(load-->Convert to file python)
with open('/home/maryam/PycharmProjects/hall_information.json', 'rt') as json_file:
    information = json.load(json_file)
print("This site provides ticketing services. Welcome to our site")
# show the names of the halls
for introduction in information:
    print("Hall information: ", introduction)
select_salon = str(input("Which hall do you want (first_hall or second_hall) ? "))
select_salon = select_salon.lower()
select_salon_user = select_salon
# Checking the existence of the hall in the json file
if select_salon in information:
    select_salon = information[select_salon]
    # print(select_salon)
# Show rows of the selected hall
    rows = select_salon.keys()
    print("Rows of your chosen hall: ")
    for row in rows:
        print(row)
    select_row = str(input("Please enter the row you want: "))
    select_row_user = select_row
# Checking the existence of the row in the json file
    if select_row in select_salon:
        row_information = select_salon[select_row]
        # print(row_information)
# Row confirmation by the user
        confirmation_row = input("Do you confirm your selected row (yes or no)? ")
        confirmation_row = confirmation_row.lower()
# Show seats of the selected row
        if confirmation_row == 'yes':
            print("NUMBER_SEAT of your chosen row: ")
            seats = row_information["number_seat"]
            for seat in seats:
                print(seat)
            select_number_seat = input("Please enter the seat number you want: ")
            select_number_seat_user = select_number_seat
# Checking the existence of the seat in the json file
            if select_number_seat in seats:
                # Check the position of the seat
                seat_list = seats.index(select_number_seat)
                seat_status = row_information["status"][seat_list]
                if seat_status == "available":
                    # Show seat price
                    print("PRICE of your chosen seat: ")
                    price = row_information["price"]
                    print("price: ", price)
                    # price confirmation by the user
                    confirmation_price = input("Do you confirm the price (yes or no)? ")
                    confirmation_price = confirmation_price.lower()
                    # Changing the seat status to sold and updating the json file
                    if confirmation_price == 'yes':
                        row_information["status"][seat_list] = "sold"
                        # If the address changes, enter the new address
                        # write the file json(dump-->Convert to file json)(indent-->The amount of indentation)
                        with open('/home/maryam/PycharmProjects/hall_information.json',
                                  'wt') as json_file:
                            json.dump(information, json_file, indent=2)
                        print("Your ticket has been successfully purchased")
                        print("Your ticket information: ")
                        # Display the general information of the purchased ticket for the customer
                        print(f"hall name: {select_salon_user}", f"row: {select_row_user}",
                              f"seat number: {select_number_seat_user}", f"price: {price}")
                    else:
                        print("Ticket purchase was cancelled :( ")
                elif seat_status == "sold":
                    print("This seat has already been sold :( ")
            else:
                print("Your selected SEAT could not be found :( ")
    else:
        print("Your selected ROW could not be found :( ")
else:
    print("Your selected HALL could not be found :( ")
