#main

import read
import operation

main_loop = True 


#main column names used in displaying data of land file.
columnNames = ("land ID", "Location", "Direction", "Anna", "Price Per Month", "Availability")

#main loop does not end until user inputs value 3.
while main_loop == True:
    print("\n\n\n\n")
    print("-" * 65)
    print(f"\t\t TechnoProperty Nepal Pvt. Ltd")
    print("-" * 65)
    print("\t\t" + "|1.| Rent Land")
    print("\t\t" + "|2.| Return Land")
    print("\t\t" + "|3.| Exit program")
    print("-" * 65)
    print()
    try:
        user_input = int(input("Enter what would you like to do? (1|2|3) : "))
        print("-" * 65)
        if user_input == 1: #rent
            print("")
            print(" Land Details:" + "\n")
            """A dictionary containing land details is generated
                then it is displayed
                then the appropriate operation is performed"""
            land_dict = read.generate_dictionary()
            read.print_table(land_dict, columnNames)
            operation.rent_land()
            print()
            print(f"\t\t\tThank you for renting")
            print("\n\n")
        elif user_input == 2: #return
            print("")
            """A dictionary containing land details is generated
                then it is displayed
                then the appropriate operation is performed"""
            land_dict = read.generate_dictionary()
            read.print_table(land_dict, columnNames)
            operation.return_land()
            print()
            print(f"\t\t\tThank you for returning")
            print("\n\n")
            print()
        elif user_input == 3: #end program
            print("Thank you for using this program!")
            print("Have a great day!")
            break
        else:
            print("Invalid input, please choose any number between (1, 2, 3)")

    #ValueError is the error found when data types dont match or is invalid
    except ValueError:
        print("Please enter an *Integer* between 1, 2 and 3")
        
    
