import time
print("Welcome to RedBus")
time.sleep(1)
print("You will have a Safe Journey with us")
time.sleep(1)
log_in = int(input("Do you want to : \n1. Log in \n2. Sign Up \nEnter your Choice : "))
if log_in==1:
    email= input("\nEnter your Email : ")
    password = int(input("Enter your PIN : "))
if log_in==2:
    time.sleep(2)
    nam = input("\nEnter your name : ")
    age = int(input("Enter your age (Note : Age should be greater than 18) : "))
    if age>18:pass
    else:print("Invalid Age")
    email = input("Enter your E-mail : ")
    password = int(input("Enter the Pin (6 Digits): "))
    def get_numeric_password():
        while True:
            password = input("Please enter your 6-digit numeric password: ").strip()
            if password.isdigit() and len(password) == 6:return password
            else:print("Invalid input. Password must be exactly 6 digits long and numeric.")
    get_phone_number= int(input("Enter your Phone Number : "))
    def get_phone_number(): 
        while True: 
            phone_number = input("Please enter your 10-digit phone number: ").strip()      
            phone_number = ''.join(filter(str.isdigit, phone_number))
            if len(phone_number) == 10: return phone_number
            else:print("Invalid input. Please enter exactly 10 digits.")
    cap = input("Fill the Captcha(AzzEE987) : ")
    if cap == "AzzEE987":pass
    else:print("Fill the Captcha again.")
time.sleep(1)
options = int(input("\nSelect one option : \n1. Bus Tickets \n2. Train Tickets \n3. Help\n4. About us\nEnter your choice : "))
time.sleep(2)
if options==1:
    time.sleep(1)
    print("\nTravel Details : ")
    time.sleep(1)
    date = int(input("\nSelect Date : \n1. 30th June 2024 \n2. 1st July 2024 \n3. 2nd July 2024 \n4. 3rd July 2024 \nEnter your choice : "))
    print("\nPlease select the appropriate options : ")
    bus_from_state = int(input("\nState : \n1. Karnataka \n2. Delhi \n3. Maharashtra \nEnter your choice : "))
    if bus_from_state == 1:
        time.sleep(1)
        bus_from_city1 = int(input("\nHere is the list of the cities : \n1. Bangalore \n2. Mysore \nEnter your city number : "))
        if bus_from_city1 == 1:
            time.sleep(1)
            bus_to_city1 = int(input("\nHere is the list of the cities where you can go : \n1. Ooty(Tamli nadu) \n2. Mysore \n3. Hyderabad \nEnter your choice : "))
            if bus_to_city1 == 1:
                time.sleep(1)
                buses1 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses1 ==1:
                    print("\nBus Details : \nTimings : 22:30 to 6:45 \nDuration : 8hr 15min \nPrice : 1199.00 \nAvailable Seats = 11")
                    bus_tickets1 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets1 <11:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price1 = bus_tickets1*1199
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Ooty")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 22:30 to 6:45")
                    print("Duration : 8hr 15min")
                    print("Effective Price : ",ticket_price1)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses1 ==2: 
                    print("\nBus Details : \nTimings : 06:00 to 14:00 \nDuration : 8hr 00min \nPrice : 888.00 \nAvailable Seats = 30") 
                    bus_tickets2 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets2 <30:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price2 = bus_tickets2*888
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Ooty")
                    print("\nBus Details : ")
                    print("Bus name : Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)]")
                    print("Timings : 06:00 to 14:00")
                    print("Duration : 8hr 00min")
                    print("Effective Price : ",ticket_price2)
                    confirm2 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus") 
            elif bus_to_city1 == 2:
                buses2 = int(input("\nHere the following buses : \n1. Vankayas [(Non-AC)(Sleeper)] \n2. Gopal Travellers [(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses2 ==1:
                    print("\nBus Details : \nTimings : 22:o0 to 7:27 \nDuration : 8hr 00min \nPrice : 1599.00 \nAvailable Seats = 27")
                    bus_tickets3 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets3 <27:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price3 = bus_tickets3*499
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Mysore")
                    print("\nBus Details : ")
                    print("Bus name : Vankayas [(Non-AC)(Sleeper)]")
                    print("Timings : 22:o0 to 00:00")
                    print("Duration : 2hr")
                    print("Effective Price : ",ticket_price3)
                    confirm3 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses2 ==2: 
                    print("\nBus Details : \nTimings : 20:42 to 06:50 \nDuration : 10hr 18min \nPrice : 899.00 \nAvailable Seats = 21") 
                    bus_tickets4 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets4 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price4 = bus_tickets4*899
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Mysore")
                    print("\nBus Details : ")
                    print("Bus name : Gopal Travellers [(Volvo)(AC)(Sleeper)(Madiwala)]")
                    print("Timings : 20:42 to 00:47")
                    print("Duration : 2hr 5min")
                    print("Effective Price : ",ticket_price4)
                    confirm4 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus") 
            elif bus_to_city1 == 3:
                buses3 = int(input("\nHere the following buses : \n1. KSM Roadways [(Non-AC)(Sleeper)] \n2. VSR Tours and Travels[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses3 ==1:
                    print("\nBus Details : \nTimings : 22:o0 to 7:27 \nDuration : 8hr 00min \nPrice : 1599.00 \nAvailable Seats = 25")
                    bus_tickets5 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets5 <25:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price5 = bus_tickets5*1599
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Hyderabad")
                    print("\nBus Details : ")
                    print("Bus name : KSM Roadways [(Non-AC)(Sleeper)]")
                    print("Timings : 22:o0 to 7:27")
                    print("Duration : 8hr 00min")
                    print("Effective Price : ",ticket_price5)
                    confirm5 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses3 ==2: 
                    print("\nBus Details : \nTimings : 20:42 to 06:50 \nDuration : 10hr 18min \nPrice : 899.00 \nAvailable Seats = 22") 
                    bus_tickets6 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets6 <22:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price6 = bus_tickets6*899
                    print("\nFinal Details : ")
                    print("From : Bangalore")
                    print("To : Hyderabad")
                    print("\nBus Details : ")
                    print("Bus name : VSR Tours and Travels[(Volvo)(AC)(Sleeper)(Madiwala)]")
                    print("Timings : 20:42 to 06:50")
                    print("Duration : 10hr 18min")
                    print("Effective Price : ",ticket_price6)
                    confirm6 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus") 
        elif bus_from_city1 == 2:
            bus_to_city2 = int(input("\nHere is the list of the cities where you can go : \n1. Hyderabad \n2. Bangalore \nEnter your choice : "))
            if bus_to_city2 ==1:
                buses4 = int(input("\nHere the following buses : \n1. BSR Tours And Travels [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses4 ==1:
                    print("\nBus Details : \nTimings : 17:30 to 06:10 \nDuration : 12h 40m \nPrice :  1160 \nAvailable Seats = 33")
                    bus_tickets7 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets7 <33:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price7 = bus_tickets7*1160
                    print("\nFinal Details : ")
                    print("From : Mysore")
                    print("To : Hyderabad")
                    print("\nBus Details : ")
                    print("Bus name : BSR Tours And Travels [(Non-AC)(Sleeper)]")
                    print("Timings : 17:30 to 06:10")
                    print("Duration : 12h 40m")
                    print("Effective Price : ",ticket_price7)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses4 ==2:
                    print("\nBus Details : \nTimings : 17:30 to 06:10 \nDuration : 12h 40m \nPrice : 1160 \nAvailable Seats = 33")
                    bus_tickets8 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets8 <33:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price8 = bus_tickets8*1160
                    print("\nFinal Details : ")
                    print("From : Mysore")
                    print("To : Hyderabad")
                    print("\nBus Details : ")
                    print("Bus name : BSR Tours And Travels [(Non-AC)(Sleeper)]")
                    print("Timings : 17:30 to 06:10")
                    print("Duration : 12h 40m")
                    print("Effective Price : ",ticket_price8)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
            elif bus_to_city2 ==2:
                buses5 = int(input("\nHere the following buses : \n1. BSR Tours And Travels [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses5 ==1:
                    print("\nBus Details : \nTimings : 17:30 to 21:45 \nDuration : 04h 15m \nPrice :  281 \nAvailable Seats = 30")
                    bus_tickets9 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets9 <33:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price9 = bus_tickets9*281
                    print("\nFinal Details : ")
                    print("From : Mysore")
                    print("To : Bangalore")
                    print("\nBus Details : ")
                    print("Bus name : BSR Tours And Travels [(Non-AC)(Sleeper)]")
                    print("Timings : 17:30 to 21:45")
                    print("Duration : 04h 15m")
                    print("Effective Price : ",ticket_price9)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses5 ==2:
                    print("\nBus Details : \nTimings : 01:30 to 05:40 \nDuration : 04h 10m \nPrice : 554 \nAvailable Seats = 16")
                    bus_tickets10 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets10 <16:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price10 = bus_tickets10*1160
                    print("\nFinal Details : ")
                    print("From : Mysore")
                    print("To : Bangalore")
                    print("\nBus Details : ")
                    print("Bus name : BSR Tours And Travels [(Non-AC)(Sleeper)]")
                    print("Timings : 01:30 to 05:40")
                    print("Duration : 04h 10m")
                    print("Effective Price : ",ticket_price10)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
    elif bus_from_state==2:
        bus_from_city3 = int(input("\nHere is the list of pick-up areas : \n1. Kaushambi bus stand \n2. Anand Vihar ISBT Terminal \nEnter your choice : "))
        if bus_from_city3 ==1:
            bus_to_city3 = int(input("\nHere is the list of the cities where you can go : \n1. Bareilly \n2. Noida  \nEnter your choice : "))
            if bus_to_city3 == 1:
                buses6 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses6 ==1:
                    print("\nBus Details : \nTimings : 22:30 to 4:45 \nDuration : 6hr 15min \nPrice : 399.00 \nAvailable Seats = 21")
                    bus_tickets11 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets11 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price11 = bus_tickets11*399
                    print("\nFinal Details : ")
                    print("From : Kaushambi bus stand")
                    print("To : Bareilly")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 22:30 to 4:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price11)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses6 ==2:
                    print("\nBus Details : \nTimings : 22:30 to 4:30 \nDuration : 6hr 0min \nPrice : 699.00 \nAvailable Seats = 21")
                    bus_tickets12 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets12 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price12 = bus_tickets12*699
                    print("\nFinal Details : ")
                    print("From : Kaushambi bus stand")
                    print("To : Bareilly")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 22:30 to 4:30")
                    print("Duration : 6hr 0min")
                    print("Effective Price : ",ticket_price12)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
            if bus_to_city3 == 2:
                buses7 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses7 ==1:
                    print("\nBus Details : \nTimings : 09:30 to 10:30 \nDuration : 1hr 0min \nPrice : 99.00 \nAvailable Seats = 21")
                    bus_tickets14 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets14 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price14 = bus_tickets14*99
                    print("\nFinal Details : ")
                    print("From : Kaushambi bus stand")
                    print("To : Noida")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 09:30 to 10:30")
                    print("Duration : 1hr 0min")
                    print("Effective Price : ",ticket_price14)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses7 ==2:
                    print("\nBus Details : \nTimings : 09:30 to 10:30 \nDuration : 1hr 0min \nPrice : 199.00 \nAvailable Seats = 21")
                    bus_tickets15 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets15 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price15 = bus_tickets15*199
                    print("\nFinal Details : ")
                    print("From : Kaushambi bus stand")
                    print("To : Noida")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 09:30 to 10:30")
                    print("Duration : 1hr 0min")
                    print("Effective Price : ",ticket_price15)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
        elif bus_from_city3==2: 
            bus_to_city4 = int(input("\nHere is the list of the cities where you can go : \n1. Bareilly \n2. Noida  \nEnter your choice : "))
            if bus_to_city4 == 1:
                buses8 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses8 ==1:
                    print("\nBus Details : \nTimings : 22:30 to 4:45 \nDuration : 6hr 15min \nPrice : 399.00 \nAvailable Seats = 21")
                    bus_tickets16 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets16 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price16 = bus_tickets16*399
                    print("\nFinal Details : ")
                    print("From : Anand Vihar ISBT Terminal")
                    print("To : Bareilly")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 22:30 to 4:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price16)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses8 ==2:
                    print("\nBus Details : \nTimings : 22:30 to 4:30 \nDuration : 6hr 0min \nPrice : 699.00 \nAvailable Seats = 21")
                    bus_tickets17 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets17 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price17 = bus_tickets17*699
                    print("\nFinal Details : ")
                    print("From : Anand Vihar ISBT Terminal")
                    print("To : Bareilly")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 22:30 to 4:30")
                    print("Duration : 6hr 0min")
                    print("Effective Price : ",ticket_price17)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
            if bus_to_city4 == 2:
                buses9 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)(Madiwala)] \nEnter your choice : "))
                if buses9 ==1:
                    print("\nBus Details : \nTimings : 09:30 to 10:30 \nDuration : 1hr 0min \nPrice : 99.00 \nAvailable Seats = 21")
                    bus_tickets18 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets18 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price18 = bus_tickets18*99
                    print("\nFinal Details : ")
                    print("From : Anand Vihar ISBT Terminal")
                    print("To : Noida")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 09:30 to 10:30")
                    print("Duration : 1hr 0min")
                    print("Effective Price : ",ticket_price18)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses9 ==2:
                    print("\nBus Details : \nTimings : 09:30 to 10:30 \nDuration : 1hr 0min \nPrice : 199.00 \nAvailable Seats = 21")
                    bus_tickets19 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets19 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price19 = bus_tickets19*199
                    print("\nFinal Details : ")
                    print("From : Anand Vihar ISBT Terminal")
                    print("To : Noida")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 09:30 to 10:30")
                    print("Duration : 1hr 0min")
                    print("Effective Price : ",ticket_price19)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")   
    elif bus_from_state ==3:
        bus_from_city4 = int(input("\nHere is the list of cities : \n1. Mumbai  \n2. Pune \nEnter your Choice : "))
        if bus_from_city4 ==1:
            bus_to_city5 = int(input("\nHere are the list of cities where you can go : \n1. Nasik \n2. Pune \nEnter your Choice : "))
            if bus_to_city5==1:
                buses10 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)] \nEnter your choice : "))
                if buses10==1:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets20 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets20 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price20 = bus_tickets20*1399
                    print("\nFinal Details : ")
                    print("From : Mumbai ")
                    print("To : Nasik")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price20)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses10==2:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 2399.00 \nAvailable Seats = 21")
                    bus_tickets21 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets21 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price21 = bus_tickets21*2399
                    print("\nFinal Details : ")
                    print("From : Mumbai ")
                    print("To : Nasik")
                    print("\nBus Details : ")
                    print("Bus name : Gubera Express[(Volvo)(AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price21)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
            if bus_to_city5==2:
                buses11 = int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)] \nEnter your choice : "))
                if buses11==1:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets22 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets22 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price22 = bus_tickets22*1399
                    print("\nFinal Details : ")
                    print("From : Mumbai ")
                    print("To : Pune")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price22)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                elif buses11==2:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 2399.00 \nAvailable Seats = 21")
                    bus_tickets23 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets23 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price23 = bus_tickets23*2399
                    print("\nFinal Details : ")
                    print("From : Mumbai ")
                    print("To : Pune")
                    print("\nBus Details : ")
                    print("Bus name : Gubera Express[(Volvo)(AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price23)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
        elif bus_from_city4 ==2:
            bus_to_city6 = int(input("\nHere are the list of cities where you can go : \n1. Nasik \n2. Mumbai \nEnter your Choice : "))
            if bus_to_city6 ==1:
                buses12 =  int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)] \nEnter your choice : "))
                if buses12 ==1:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets24 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets24 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price24 = bus_tickets24*1399
                    print("\nFinal Details : ")
                    print("From : Pune ")
                    print("To : Nasik")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price24)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses12 ==2:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets25 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets25 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price25 = bus_tickets25*1399
                    print("\nFinal Details : ")
                    print("From : Pune ")
                    print("To : Nasik")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price25)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
            if bus_to_city6 ==2:
                buses12 =  int(input("\nHere the following buses : \n1. Mayura Bus [(Non-AC)(Sleeper)] \n2. Gubera Express[(Volvo)(AC)(Sleeper)] \nEnter your choice : "))
                if buses12 ==1:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets26 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets26 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price26 = bus_tickets26*1399
                    print("\nFinal Details : ")
                    print("From : Pune ")
                    print("To : Mumbai")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price26)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
                if buses12 ==2:
                    print("\nBus Details : \nTimings : 20:30 to 2:45 \nDuration : 6hr 15min \nPrice : 1399.00 \nAvailable Seats = 21")
                    bus_tickets27 = int(input("\nEnter number of tickets you want to book : "))
                    if bus_tickets27 <21:
                        pass
                    else:print("\nEnter number of tickets again")
                    ticket_price27 = bus_tickets27*1399
                    print("\nFinal Details : ")
                    print("From : Pune ")
                    print("To : Mumbai")
                    print("\nBus Details : ")
                    print("Bus name : Mayura Bus [(Non-AC)(Sleeper)]")
                    print("Timings : 20:30 to 2:45")
                    print("Duration : 6hr 15min")
                    print("Effective Price : ",ticket_price27)
                    confirm1 = input("Do you want to confirm your purchase(yes/no) : ").lower()
                    print("Thanks for visiting RedBus")
elif options==2:
    print("\nTravel Details : ")
    date = int(input("\nSelect Date : \n1. 30th June 2024 \n2. 1st July 2024 \n3. 2nd July 2024 \n4. 3rd July 2024 \nEnter your choice : "))
    print("\nSelect your pickup location : ")
    train_state = int(input("\nEnter State : \n1. Karnataka \n2. Tamil Nadu \n3. Maharashtra \nEnter your choice : "))
    if train_state==1:
        train_pickup1=int(input("Here are the list of cities : \n1. Bangalore \n2. Mysore \nEnter your choice : "))
        if train_pickup1==1:
            train_drop1=int(input("\nEnter your drop location : \n1. Mysore \n2. Mangalore \nEnter your choice : "))
            if train_drop1==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mysore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mysore \nTime : 18:00 to 20:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mysore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mysore \nTime : 18:00 to 20:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            elif train_drop1==2:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 22:00 to 10:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 22:00 to 10:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 22:00 to 10:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 18:00 to 00:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
        elif train_pickup1==2:
            train_drop2=int(input("\nEnter your drop location : \n1. Bangalore \n2. Chennai \nEnter your choice : "))
            if train_drop2==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mysore \nTo : Bangalore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mysore \nTo : Bangalore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Bangalore \nTo : Mangalore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            if train_drop2==2:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mysore \nTo : Chennai \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mysore \nTo : Chennai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mysore \nTo : Chennai \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mysore \nTo : Chennai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
    elif train_state==2:
        train_pickup2=int(input("Here are the list of cities : \n1. Chennai \n2. Vellore \nEnter your choice : "))
        if train_pickup2==1:
            train_drop3 = int(input("\nEnter your drop location : \n1. Bangalore \n2. Vellore \nEnter your choice : "))
            if train_drop3==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Chennai \nTo : Bangalore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Chennai \nTo : Bangalore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Chennai \nTo : Bangalore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Chennai \nTo : Bangalore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            if train_drop3==2:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Chennai \nTo : Vellore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Chennai \nTo : Vellore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Chennai \nTo : Vellore \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Chennai \nTo : Vellore \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
        elif train_pickup2==2:
            train_drop4 = int(input("\nEnter your drop location : \n1. Chennai \n2. Ponducherry \nEnter your choice : "))
            if train_drop4==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Vellore \nTo : Chennai \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Vellore \nTo : Chennai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Vellore \nTo : Chennai \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Vellore \nTo : Chennai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            if train_drop4==2:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Vellore \nTo : Ponducherry \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Vellore \nTo : Ponducherry \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Vellore \nTo : Ponducherry \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Vellore \nTo : Ponducherry \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
    elif train_state==3:
        train_pickup3=int(input("Here are the list of cities : \n1. Mumbai \n2. Pune \nEnter your choice : "))
        if train_pickup3==1:
            train_drop5 = int(input("\nEnter your drop location : \n1. Nasik \n2. Delhi \nEnter your choice : "))
            if train_drop5==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mumbai \nTo : Nasik \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mumbai \nTo : Nasik \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00 \nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mumbai \nTo : Nasik \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mumbai \nTo : Nasik \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            if train_drop5==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mumbai \nTo : Delhi \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mumbai \nTo : Delhi \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Mumbai \nTo : Delhi \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Mumbai \nTo : Delhi \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
        elif train_pickup3==2:
            train_drop6 = int(input("\nEnter your drop location : \n1. Mumbai \n2. Nasik \nEnter your choice : "))
            if train_drop6==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Pune \nTo : Mubabi \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Pune  \nTo : Mumbai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Pune \nTo : Mumbai \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Pune  \nTo : Mumbai \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
            if train_drop6==1:
                select_train = int(input("\nHere are the list of Trains : \n1. Vande Bharat \n2. Shatabdi Express \nEnter your choice : "))
                if select_train ==1:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Pune \nTo : Nasik \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Pune  \nTo : Nasik \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                elif select_train==2:
                    select_time = int(input("\nSelect time : \n1. 22:00 \n2. 18:00\nEnter your choice : "))
                    if select_time==1:
                        print("Here are the details : \nFrom : Pune \nTo : Nasik \nTime : 22:00 to 00:00 \nDuration : 2hr \nTicket Price : 399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
                    elif select_time==2:
                        print("Here are the details : \nFrom : Pune  \nTo : Nasik \nTime : 18:00 to 20:00 \nDuration : 12hr \nTicket Price : 1399")
                        confirm = input("Do you want to confirm your purchase(yes/no) : ").lower()
                        print("Thnaks for using Redbus")
elif options==3:
    print("\nWelcome to red:Buddy")
    time.sleep(2)
    b = int(input("\nSelect help topic : \n1. Bus Ticket Problem \n2. Train Ticket Problem \n3. Other Topics \nEnter your choice : "))
    if b == 1:
        time.sleep(2)
        c = int(input("\nHelp Topics : \n1. Ticket Booking \n2. Ticket Reschedule / Cancellation \n3. Bus Cancellation \n4. Offers \n5. Payments & Refunds\nEnter your choice : "))
        if c == 1:
            d = int(input("\nFAQs : \n1. I am unable to go beyond search option. What do I do? \n2. How to book a bus ticket on redBus? \n3. Where can I view the bus ticket that I have booked through redBus? \n4. How to check the availability of buses? \n5. Do I need to create an account to book bus tickets on redBus? \n6. How to sign-up or login to redBus? \n7. Can I book State Road Transport Corporation bus tickets from redBus? \n8. Will I have to pay extra money for booking online tickets on redBus? \n9. I am unable to select a specific seat/operator/date/route. What do I do? \nEnter your choice : "))
            if d ==1:print("\nWorry not! We've got you. Try following the below steps: \n1. Open the redBus App \n2. Input the boarding and dropping location and search for your bus. \n3. Ensure your redBus app is up-to-date: Confirm that you have the most recent version installed.\n4. Check your internet connectivity. \n5. Clear app cache: Clearing the app's cache can help resolve temporary glitches. \n6. Restart your device: Occasionally, a straightforward restart can address minor concerns.")
            elif d==2:print("\nBooking bus tickets on redBus platform is a very simple 6 step process: \n1. On the redBus app home page, enter origin, destination, and date of journey and click on Search. \n2. A list of buses will be displayed. Tap on the bus that you like, and you will be taken to the next screen. \n3. 3. Select a seat of your choice and click on Select Boarding and Dropping Points. \n4. On the next screens select the boarding and dropping points of your choice. \n5. On the next screen, enter your contact details and Passenger information and Tap on Proceed . Note: Please check all the information carefully before moving ahead. \n6. Select a payment method after reviewing booking details and make the payment.")
            elif d==3:print("\nFollow the steps given below: \n1. Tap on My Bookings tab on the app home page. \n2. Tap on the journey for which you want to view the ticket.")
            elif d==4:print("\nChecking the availability of the buses is very simple and can be done in 5 easy steps as follows: \n1. On the home page, enter the desired source, destination, and date of travel. \n2. All available buses will be shown to you to choose from. We show a lot of useful information such as fare, journey duration, amenities, bus ratings, etc so that you can choose the bus that you like the best. \n3. Once you select the bus that you like the best, you can check the available seats and choose the seat of your choice. \n4. In case there are no buses available for your requirement, you will see a “No services found” message on your screen. \n5. You can try changing the date or enter other nearby cities as source/destination, as per your requirement.")
            elif d==5:print("\nNo, you can book bus tickets without creating a \nredBus account by providing required passenger details. \nHowever, we recommend you to create an account \nso that you get the latest information about bus availability, ticket details and other features \nwhich will help you book faster during future transactions.")
            elif d==6:print("\nIt's very easy to sign-up or login on redBus App/Website using your mobile number and \nvalidating with an OTP. You can also login using your Google account. If the OTP is not received, \ninvestigate the following: \n1. Confirm if you entered the correct phone number. \n2. Ensure your text message inbox is not full. \n3. Check if your phone is set to block messages from unknown senders. \n4. Verify if your phone carrier is blocking the message. \n5. Check for a stable internet connection. \nIf the issue persists, attempt restarting your device. \n1. Ensure you have the latest version of the redBus App; update it if needed. \n2. Clear the app cache and retry the login process. \n3. For Google account users, reset the email password and attempt logging in again.")
            elif d==7:print("\nYes, you can book SRTC (State Road Transport Corporation) bus tickets using redBus website or mobile app. Some of the major SRTC includes.\n1. APSRTC - Andhra Pradesh State Road Transport Corporation. \n2. TSRTC - Telangana State Road Transport Corporation. \n3. HRTC - Himachal Road Transport Corporation. \n4. MSRTC - Maharashtra State Road Transport Corporation. \n5. RSRTC - Rajasthan State Road Transport Corporation. \n6. BSRTC - Bihar State Road Transport Corporation. \n7. UPSRTC - Uttar Pradesh State Road Transport Corporation. \n8. KSRTC - Kerala State Road Transportation Corporation. \n9. SBSTC - South Bengal State Transportation Corporation. \n10. CTC - Calcutta Tramways Company. \n11. PEPSU - Patiala and East Punjab States Union Transportation Corporation. \n12. HPTDC - Himachal Pradesh Tourism Development Corporation. \n13. KTCL - Kadamba Transport Corporation. \n14. WBSTC - West Bengal State Transportation Corporation. \n15. ASTC - Assam State Transport Corporation. \n16. KSTDC - Karnataka State Tourism Development Corporation. \n17. TSTDC - Telangana State Tourism Development Corporation. \n18. NBSTC - North Bengal State Transport Corporation. \n19. KAAC - Karbi Anglong Autonomous Council Transport. \nWe are rapidly expanding our network with the other SRTC vendors as well. Stay tuned!")
            elif d==8:print("\nNo, there is no need to pay extra charges when booking bus ticket on redBus.")
            elif d==9:print("\nNo, there is no need to pay extra charges when booking bus ticket on redBus.")
            else: print("Thanks for visiting RedBus")
        elif c==2:
            time.sleep(2)
            e = int(input("\nFAQs : \n1. How to cancel a ticket? \n2. Are there any cancellation charges levied when a bus ticket is canceled? \n3. How to reschedule a ticket? \nEnter your choice : "))
            if e==1:print("\nHere are the steps to follow: \n1. Tap on My Bookings tab on the app home page. Tap on the ticket which you want to cancel. \n2. On the page, tap on the cancel button below the ticket details section. \n3. A popup will come. Select Cancel Ticket to proceed with Cancelation. \n4. On the next screen, Tap on the review Refund Details. \n5. Review the details on the next screen and confirm your Cancellation by clicking on Confirm Cancellation button. \nNote: Review the cancellation policy before canceling the ticket by tapping on view cancellation policy. \n6. You can track the refund status by going to the Bookings Tab and selecting the canceled ticket.")
            elif e==2:print("\nCancellation charges are levied as per the Cancellation Policy of the bus. These policies can differ from service to service. \nAll charges will be processed as per the terms and conditions mentioned in the Cancellation Policy.")
            elif e==3:print("\nHere are the rules that are to be followed : \n1. Tap on My Bookings tab on the app home page. Tap on the ticket for which you want to change the travel date. \n2. Tap on the Change Travel Date button below the ticket details section. \n3. Select a new date of journey and click on Search Buses . \n4. You will be shown a list of buses available on that date. Select a bus and then the seat of your choice. \n5. Pay the balance amount and your ticket will be rescheduled. You will receive a new ticket for the new date of travel.")
            else: print("Thanks for visiting RedBus")
        elif c==3:
            time.sleep(2)
            f= int(input("\nFAQs : \n1. Bus operator has cancelled the bus. What do I do? \nEnter your choice : "))
            if f==1:print("\nIf the bus is cancelled you will get the complete refund of the paid amount back to your \nsource of payment. Kindly click on the trip from the Help section of the app, \nselect Bus Cancellation issue and register a complaint so that we can do further investigation on the same.")
            else: print("\nThanks for visiting RedBus")
        elif c==4:
            time.sleep(2)
            g = int(input("\nFAQs : \n1. How do I apply the offer code? \n2. I am unable to apply the offer code. What do I do? \n3. Can I get discounts & offers on bus tickets at redBus? \n4. I have applied the promo code, but did not receive any cashback. What do I do? \nEnter your choice : "))
            if g==1:print("\nFollow the below steps to apply the offer code: \n1. Open the redBus App and ensure that you are logged in to your account. \n2. Navigate to the redBus Payment page. \n3. The offer Code section will appear where you can enter the offer code accurately and click ‘Apply’. \n4. Once the offer code is successfully applied, the discount will be reflected in your booking summary.  \n5. Choose your preferred payment method and complete the payment.")
            elif g==2:print("\nOpen the redBus App and ensure that you are logged in to your account. Navigate to the Payment page, where you can input the offer code. \nAfter entering the code, click the ‘Apply’ button. \nIf you encounter an error message, review the following guidelines: \n1. Check the terms and conditions for the applied offer. \n2. Note that all offers are exclusively valid for users who are logged into their accounts. \n3. Be aware that each offer code has a usage limit of one per customer email or mobile number.\n4. To access the terms and conditions, proceed to the offer section and select ‘View All.’ \n5. You will find a list of available offers; choose one and read through its terms and conditions. \n6. After understanding the terms, apply the chosen offer and finalize your booking.")
            elif g==3 :print("\nYes, you will get the best fares on bus tickets bookings on redBus by applying coupon codes before completing your transaction. To check for your eligible \noffers & to make your bus booking online at the lowest prices on redBus, kindly refer the Offers section")
            elif g==4:print("\nIf you used a valid cashback coupon code while making a booking, then the corresponding cashback will be credited to redBus wallet within 3 days after \ncompletion of journey. Please check the terms and conditions (https://www.redbus.in/info/OfferTerms#SUPERHIT ) of the promotional \noffer carefully. If you have not received the cashback yet as per the terms and conditions, \nkindly select the trip for which you did not receive the cashback from Help section on the app and register \na complaint by selecting “Offer related issue” for us to assist your further.")
            else: print("Thanks for visiting RedBus")
        elif c==5:
            time.sleep(2)
            h= int(input("\nFAQs : \n1. I am unable to select payment option. What do I do? \n2. How do I check my refund status and details? \n3. What are the payment options that are available on redBus? \n4. I missed the bus. Do I get a refund? \n5. How can I get a refund in case I cancel my ticket? \n6. My money has been deducted but the tickets are not booked. What should I do now? \n7. Will I get refund in case of a failed transaction? \nEnter your choice : "))
            if h==1:print("\nWhile on the payment page, you'll find various payment methods listed. If you're facing issue with a specific payment method, please try with an alternative payment option.\nIf the issue persists, consider the following steps: \n1. Ensure your redBus app is up-to-date: Confirm that you have the latest version of the redBus app installed on your device.\n2. Check for the error message - Take note of any error messages displayed.\n3. Check if you can access different payment methods successfully.\n4. Check your internet connection: Ensure that you have a stable internet connection. \n5. Clear the app's cache: Clearing the app's cache can help resolve temporary glitches.\n6. Restart your device: Sometimes, a simple device restart can rectify minor problems. \n7. Reach out to redBus support: If the problem continues, it's advisable to directly contact redBus customer support for assistance.")
            elif h==2:print("\nFollow the below simple steps to check your refund status and details on the redBus App: \n1. Open the redBus App \n2. Access the ‘My Bookings’ section\n3. Navigate to the ‘Cancelled’ tab\n4. Choose the correct and appropriate booking\n5. Click on ‘‘Refund Details.’’\n6. Your refund status will be visible\n7. To view the complete details click on ‘Show Details.’\n8. The refund breakdown, total refund amount, cancellation time, and refund initiation and deposited will be displayed")
            elif h==3:print("\nWe support all kinds of UPI payments (GPay, PhonePe etc), cards (credit and debit),\nnetbanking, wallets (Paytm, Ola Money), CredPay and BNPL (Simpl).") 
            elif h==4:print("\nredBus provides a 100 Percent refund if the bus is missed due to either redBus or its partner company's fault. \nHowever, if the bus is missed due to any other reason not directly related to redBus no refund is provided.")
            elif h==5:print("\nThe refund is provided as per with our cancellation policy. The refund /ncan be credited to the source of payment (Example: debit card, credit card, net banking) or credited \nto redBus wallet. Wallet credit can be used for bus booking in future (within 6 months of cancellation).")
            elif h==6:print("\nThe online booking confirmation might not get generated due to fluctuations in the bank networks \nin most of the cases. In such scenarios we suggest you to choose a different mode of \npayment to complete your transaction. Before booking a new ticket, please read the following: \n1. You will receive the ticket confirmation via SMS & email within 15 minutes if the booking amount is received by redBus. \nIf you do not receive the ticket or bus booking online confirmation details within 15 minutes, the deducted amount will be auto refunded to your source account within one hour. \nAfter 15 minutes you can go ahead and make a new booking. \n2. Sometimes, redBus might not receive the booking amount even if it’s deducted from your account. \nSuch a scenario may arise when your bank puts a hold on the payment. \nYour bank may release the hold on such payments in 24-48 hours, where the amount deducted is reversed by the bank. \nGo to the Booking/Payment Failures section in the chatbot to find out if redBus received the payment. \nIf the Payment Received by redBus is 'No' please go ahead and make a new bus booking with us. \nHowever, please be assured that you will get your refund if the ticket is not booked.")
            elif h==7:print("\nYes, the funds in case of a failed transaction if debited from redBus wallet is credited \nback in 15 minutes and if debited from source is credited back in 7 bank working days.")
            else: print("Thanks for visiting RedBus")
        else: print("Thanks for visiting RedBus")
    elif b==2: 
        time.sleep(2)
        i = int(input("\nHelp topics : \n1. Booking FAQs \n2. Tatkal FAQs \n3. Journey FAQs \n4. Cancellation FAQs \nEnter your choice : "))
        if i == 1:
            time.sleep(2)
            j= int(input("\nFAQs : \n1. How to book a train ticket on redBus App? \n2. I do not remember my IRCTC account password. How to book a ticket?\n 3. How do I change my boarding point while booking a train ticket? \n 4. How do I change the boarding point after the train ticket is booked?\n 5. How many people can I book on a single train ticket booking?\n6. Do I get to choose a seat or berth of my choice? \n7. Where can I view the train ticket that I have booked through redRail? \n8. How do I pay for my online train ticket booking that is made through redRail? \nEnter your choice : "))
            if j==1:print("\nBooking a train ticket on redBus app is very simple and can be done in 5 easy steps as follows: \n1. On the redBus App Home Page, click on the redRail icon. \n2. Enter origin, destination and date of journey and click on Search Trains. \n3. Train list with availability numbers in each class will be displayed. Select a train and class to be booked. \n4. Enter IRCTC user id, passenger details, select preferences (if any) and click Proceed. \n5. Select a payment method after reviewing booking details and make the payment.")
            elif j==2:print("\nIf you do not remember your IRCTC account password, click on 'Get New Password' on the Traveler detail’s page or IRCTC authentication page. \nIt will ask you to enter either Mobile no. or email id registered with IRCTC. \nChoose one option and after entering the details, you will get a new password on the mobile no/emailId entered by you. \nYou can use that password to book a ticket.") 
            elif j==3:print("\n1. On the traveler details page, click on the change button in the boarding station section. \n2. List of available boarding stations will appear. Select the new boarding station by tapping on it. \n3.Proceed with the booking.")
            elif j==4:print("\nBoarding point cannot be changed once the ticket is booked on redRail. \nIn this case, you need to cancel the booking and rebook it with the revised boarding point.")
            elif j==5:print("\nCustomers can book a maximum of 6 passengers in a single train ticket booking that is booked through redRail. \nHowever, in the case of Tatkal ticket, customers can book a maximum of 4 passengers in a single ticket booking.")
            elif j==6:print("\nNo, you cannot select your seat/berth. \nThe seat and berth are allocated by Indian Railways, and there is no control over this allocation. \nHowever, there is an option to choose seat/berth preferences while booking a ticket through redRail/redBus, but that is not guaranteed.")
            elif j==7:print("\nAfter you have successfully booked a train ticket through redRail, you will receive an email, a WhatsApp message and a text message containing the details about your booking. \nYou can also view your bookings under the 'My Bookings' section of the redBus app.")
            else: print("Thanks for visiting RedBus")
        elif i==2:
            time.sleep(2)
            k= int(input("\nFAQs; \n1. Can I book a train ticket under the Tatkal quota through redRail? \n2. What is the tatkal booking window for redRail? \n3. Why is Tatkal window different for redRail? \n4. Can I cancel a ticket booked under Tatkal Quota? \nEnter your choice : "))
            if k==1:print("\nYes, you can book Tatkal quota train tickets through redRail. \nWith the convenience of viewing updated trains and their berth availability, it is advisable to complete your online train ticket booking at the earliest through redRail.")
            elif k==2:print("\nTatkal E-ticket can be booked one day in advance for selected trains, excluding the departure date of the train from the departure station. \nIt can be booked from 10:15 on the opening day for AC class 1A/2A/3A/CC/EC/3E and from 11:15 for non-AC class SL/FC/2S.")
            elif k==3:print("\nThis is as per rules of the Indian railways, tatkal window for bookings on redRail \nbegin at 10.15AM (IST) for AC class and 11.15AM (IST) for non-AC class.")
            elif k==4:print("\nYes, a Tatkal ticket can be canceled, just like any other railway ticket. \nHowever, if you decide to cancel your Tatkal ticket, you will not receive any refund.")
            else: print("Thanks for visiting RedBus")
        elif i==3:
            time.sleep(2)
            l= int(input("\nFAQs : \n1.Where can I view the train ticket that I have booked through redRail? \n2. Do I need to carry any documents with me while I board my train? \n3. When does the train chart get prepared? \n4. I did not get seat or berth of my choice, what to do? \n5. How do I check my latest PNR status? \n6. My Ticket shows waitlisted, can I still travel? \n7. My booking class/ type was changed - what to do? \nEnter your choice : "))
            if l==1:print("\nAfter you have successfully booked a train ticket through redRail, you will receive an email, a WhatsApp message and a text message containing the details about your booking. \nYou can also view your bookings under the “My Bookings” section of the redBus app.")
            elif l==2:print("\nYou do not require a photo ID when you book your train ticket through redRail, but, you will need to carry an ID when you board the train. \nIDs such as PAN card, Voter ID, Driving License, Aadhar card or any other photo ID that has a serial number issued by the Central/State Government.")
            elif l==3:print("\nTrain chart preparation time is controlled by Indian Railways. \nThe chart is usually prepared 4 hours before departure of train from the charting station. \nFor early morning trains, the chart is usually prepared the night before.")
            elif l==4:print("\nIf you have selected seat or berth preferences while booking your ticket with redRail, it is subject to availability and not guaranteed.\nIf the desired seats are not available based on the preference, alternative seats will be assigned to the passengers.")
            elif l==5:print("\nYou can check your latest PNR status on the redBus/redRail mobile app in the following ways - \n1. Option 1: On the Home Page -> Under PNR Status Tab.  \n2. Option 2: Go to My bookings-> Select relevant booking ->Check latest PNR status")
            elif l==6:print("\nA passenger holding a waitlist e-ticket, even after chart preparation, will not be permitted to board the train. \nIf found traveling on the train, they will be treated as a passenger without a valid ticket, in accordance with Railway Rules.\nTicket amount paid will be automatically refunded if all passengers are Waitlisted (WL) on chart preparation. \nIf only a few passengers are WL, then customers not travelling will be required to file TDR to get refund.")
            elif l==7:print("\nDue to operational feasibility of the train sometimes some coaches are removed from the train, which may \nresult in the change of reservation status and your berth status is changed from one coach to another high capacity coach with the same number and type of option.")
            else: print("Thanks for visiting RedBus")
        elif i==4:
            time.sleep(2)
            m= int(input("\nFAQs: \n1. How to cancel a train ticket on redBus App?\n2. Are there any cancellation charges levied when a train ticket is canceled?\n3. Can I cancel my train ticket after the train departure?\n4. What happens if my trains get cancelled? Will my tickets be also cancelled?\n5. Can I cancel the ticket for only few passengers?\n6. Why is my Cancellation amount different from what is communicated by IRCTC?\n7. Can I cancel my train ticket after chart preparation?\n8. My train is delayed, Can I cancel my ticket and get the refund? \nEnter your choice : "))
            if m==1:print("\nTrain Ticket can be canceled on redBus app by following these simple steps: \n1. On the redBus app, click on My Bookings icon. \n2. On My Bookings, select redRail tab. The list of all upcoming bookings will be displayed. Select the booking to be canceled. \n3. On the booking details page, click on Review & Cancel button \n4. Select the passengers to be canceled. \n5. Click on Review Refund Details to see the details of cancellation charges applicable and refundable amount. Click on \nConfirm Cancelation and the ticket will be canceled.")
            elif m==2:print("\nYes, depending on when the cancellation was initiated, an amount might get deducted as per the cancellation and refund rules of IRCTC and Indian Railways. \nAlso, the Agent Service Charges and IRCTC convenience fees are non-refundable.")
            elif m==3:print("\nTrain tickets cannot be canceled online after the departure of the train. \nIn case of special cases that qualify for filing of TDR as per the rules of Indian Railways, user can file TDR.")
            elif m==4:print("\nIn such a case you don’t need to cancel your booking manually. \nIRCTC will automatically initiate a refund of ticket fare, which will be credited to the original mode of payment.")
            elif m==5:print("\nYes, it can be done. Please follow the steps below for partial cancellation:\n1. Log on to redbus/redRail website/mobile web and mobile application\n2. Go to My Bookings\n3. Select relevant Booked Ticket / PNR you wish to cancel\n4. Choose the passengers you wish to cancel the bookings for.\n5. Check cancellation and refund amount & Click on Submit.")
            elif m==6:print("\nIRCTC refund message does not contain multiple charges that are deducted as per the rules of Indian railways like convenience fee, Agent service fee, Payment gateway charges, etc. \nOther than this, few charges are non-refundable like Add on premium & discounts/wallet cash, if any, as applicable.")
            elif m==7:print("\nConfirmed ticket: Ticket cannot be canceled after chart preparation. \nRAC: Ticket can be cancelled before the 30 minute of the scheduled departure time of the train.\nWaitlisted ticket: Ticket can be cancelled before the 30 minute of the scheduled departure time of the train.")
            else: print("Thanks for visiting RedBus")
    elif b==3:
        time.sleep(2)
        n= int(input("\n1. 0Technical Issues \n2. redBus Referral Help \n3. New bus booking help \n4. Offers\nYour choice : "))
        if n==1:
            o= int(input("\nSure! Please let me know, how can I help you?\n1. Deactivate account\n2. No buses found\n3. Delete saved credit/debit card\n4. Incorrect fare displayed\nEneter your choice : "))
            if o==1:print("\nTo delete your account, please Login to redBus App and follow the below \nsteps. This action will permanently delete your account after 90days.\n1. Open app & click on 'My Account' -> 'Settings'\n2. Select “Account Settings” and click on Delete your account\n3. Account deletion information page will be displayed\n4. Click on 'Delete my Account' and proceed with Account deletion\n5. Confirmation page appears and account will be deactivated after 90 days\nPlease note\n1. This action will permanently delete your account\n2. Your payment & booking history information will be deleted\n3. You will need to re-enter all your details if you decide to use redBus services again\n4. You will be unsubscribed from our mailing list and stop receiving the latest deals and offers")
            elif o==2:print("\nYou will see a ‘No services found’ message, if there are no buses available for source, destination and date entered. \nYou can try changing the date or enter other nearby cities as source/destination, as per your requirement.")
            elif o==3: print("\nSaved cards help to make your booking process faster. \nThe information regarding your saved cards is completely safe and is not shared or visible to anyone. ")
            elif o==4: print("\nThe fares displayed on redBus are decided by the bus operators. \nThe bus operators can change the fares based on the demand.")
            else: print("Thanks for visiting RedBus")
        elif n==2:print("\nYour account is being reviewed for suspicious activity as our systems alerted us based on several behavioural factors. \nOnce we find nothing wrong upon a manual review, we will be releasing your account and you will be able to use referral features.")
        elif n==3: print("\nSure, I will be happy to help you! What do you need help with?")
        elif n==4:print("\nClick the below link to see all our exciting offers. \nIf you are unable to use any offer code, read the offer T&C to understand eligibility rules.\nhttps://b.redbus.com/5g51x1a")
        else: print("\nThanks for visiting RedBus")
    else: print("Thanks for visiting RedBus")
elif options==4:
    time.sleep(1)
    print("\nBOOK BUS TICKETS ONLINE\nredBus is India's largest brand for online bus ticket booking and offers an easy-to-use online bus and train ticket booking; with over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, redBus makes road journeys super convenient for travellers. A leading platform for booking bus tickets, redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.")
    time.sleep(1)
    print("\nBooking a bus ticket online on the redBus app or website is very simple. You can download the redBus app or visit redbus.in and enter your source, destination & travel date to check the top-rated bus services available. You can then compare bus prices, user ratings & amenities, select your preferred seat, boarding & dropping points and pay using multiple payment options like UPI, debit or credit card, net banking and more. With redBus, get assured safe & secure payment methods and guaranteed travel with the best seat and bus operator of your choice. Once the bus booking payment is confirmed, all you have to do is pack your bags and get ready to travel with the m-ticket, which you can show to the bus operator on your mobile before boarding the bus. Online bus ticket booking with redBus is that simple!")
    time.sleep(1)
    print("\nredBus also offers other exclusive benefits on online bus tickets like flexible ticket rescheduling options, easy & friendly cancellation policies, and instant payment refunds. With a live bus tracking feature, you can plan travel and never miss the bus. You can get the cheapest bus tickets by availing the best discounts for new & existing customers. With redDeals, you can also get exclusive & additional discounts on your online bus ticket booking. You will get 24/7 customer support on call, chat & help to resolve all your queries in English & local languages.")
    time.sleep(1)
    print("\nredBus offers Primo bus services, specially curated by redBus with highly rated buses and best-in-class service. With Primo by redBus, you can be assured of safe, comfortable, and on-time bus service at no additional cost. With multiple boarding and dropping points available across all major cities in India, you can select at your convenience and enjoy a smooth travel experience.")
    time.sleep(1)
    print("\nredBus operates in six countries, including India, Malaysia, Singapore, Indonesia, Peru, and Colombia. Through its website and app, it has sold over 220 million bus tickets worldwide. With over 36 million satisfied customers, redBus is committed to providing its users with a world-class online bus booking experience.")
    time.sleep(1)
    print("\nredBus offers bus tickets from some of the top private bus operators, such as Orange Travels, VRL Travels, SRS Travels, Chartered Bus, and Praveen Travels, and state government bus operators, such as APSRTC, TSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, and more. With redBus, customers can easily book bus tickets for different bus types, such as AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses, and more.")
else: print("Thanks for visiting RedBus")