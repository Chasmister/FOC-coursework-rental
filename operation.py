#OPERAION

import datetime
import read
import write

def rent_land():
    """Allows a customer to rent land, calculates total amount, generates bills, and updates land data.
       returns: none
       Modifies text files
       Prints to shell"""
      
    #Personal details of customer
    customer_name = input("|Please enter your name first: ")
    phone_number = input("|Please enter your Phone Number: ")
    address = input("|Please enter your Address: ")
    
    current_date = datetime.datetime.now()#returns current date and time
    formatted_date = current_date.strftime("%Y-%m-%d")#date formatted using strftime
    grand_total = 0
    print("|"+"-" * 62)
    bill_dict = {}
    rent_loop = True
    land_rented = False

    #loop does not end until user does not want to rent any more lands
    while rent_loop == True:
        try:
            land_to_rent = int(input("|Which land would you like to rent? : " ))
            print("|"+ "-" * 62)
            dict_ = read.generate_dictionary()
            
            total_amount = 0
            if land_to_rent in dict_:
                row = dict_[land_to_rent] 
                
                if row[4] == 'Available':
                    
                    rent_duration = int(input("|How long would you like to rent? (in months) : "))
                    print("|"+ "-" * 62)
                    total_amount = rent_duration * int(row[3])
                    grand_total = grand_total + total_amount
                    
                    customer_details = [customer_name, phone_number, address, formatted_date, grand_total]
                    additional_data = [rent_duration, total_amount] #this is the additional data only visible in the bill
                    
                    row.pop()#Removes "availability" column
                    row.extend(additional_data)
                    
                    bill_dict[land_to_rent] = row
                    land_rented = True
                
                else:
                    print("|This land is not available, please enter a different land ID")
            else:
                 print("|This land is not on the list, please enter a valid ID")
        
                
            rent_more = (input("|Would you like to continue renting land? (Y/N) : ")).upper()
            print("|"+ "-" * 62)
            print()
            if rent_more == 'N':
                rent_loop = False

        except ValueError:
            print("Please enter valid integer values")
     
    if land_rented == True:
        write.generate_bill(bill_dict, customer_details, "rent")
        write.update_land_data(bill_dict)
     
                    

                

def return_land():
    """Allows a customer to return land, calculates fine and price with fine, generates bills, and updates land data.
       returns: none
       Modifies text files
       Prints to shell """

    #Personal details of customer    
    customer_name = input("|Please enter your name first: ")
    phone_number = input("|Please enter your Phone Number: ")
    address = input("|Please enter your Address: ")
    
    current_date = datetime.datetime.now() # returns current date and time
    formatted_date = current_date.strftime("%Y-%m-%d") #date formatted using strftime
    
    grand_total = 0
    print("|"+"-" * 62)
    bill_dict = {}
    return_loop = True
    land_returned = False
     #loop does not end until user does not want to return any more lands
    while return_loop == True:
        try:
        
            land_to_return = int(input("|Which land would you like to return?"))
            dict_ = read.generate_dictionary()
            
            if land_to_return in dict_:
                row = dict_[land_to_return]
                if row[4] == 'Not Available':
                    initial_duration = int(input("|How long were you planning to rent? (in months) : "))    
                    final_duration = int(input("|How long did you rent? (in months) : "))
                    
                    price = int(row[3]) * final_duration
                    delayed_duration = 0
                    """fine is calculated according to number of extra months rented
                        amount of fine placed is 10%"""
                    if final_duration > initial_duration:
                        delayed_duration = final_duration - initial_duration
                        fine = int(0.10 * float((delayed_duration * int(row[3]))))
                        price_with_fine = price + fine
                    else:
                        price_with_fine = price
                        
                    grand_total = grand_total + price_with_fine
                     
                    customer_details = [customer_name, phone_number, address, formatted_date, grand_total]
                    additional_data = [fine, price_with_fine] #this is the additional data only visible in the bill
                    
                    row.pop()#Removes "availability" column
                    row.extend(additional_data)
                    bill_dict[land_to_return] = row
                    land_returned = True
                else:
                    print("|This land is already available, please enter a different land ID")
            else:
                 print("|This land is not on the list, please enter a valid ID")
                
            return_more = (input("|Would you like to continue returning lands? (Y/N) : ")).upper()
            print("|"+ "-" * 62)
            print()
            if return_more == 'N':
                return_loop = False

        except ValueError:
            print("Please enter valid integer value")
            
    if land_returned == True:           
        write.generate_bill(bill_dict, customer_details, "return") 
        write.update_land_data(bill_dict)
        
                
