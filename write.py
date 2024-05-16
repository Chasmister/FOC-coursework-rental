import datetime
import read

def generate_bill(bill_dict, customer_details, bill_type):
    """Takes parameters bill_dict and dictionary, customer_details as list and bill_type as string
       generates a unique bill formed through concatenation of variables
       returns none
       prints bill to shell
       creates txt file"""
    if bill_type.upper() == "RENT":
        file = open(customer_details[0] + " " + customer_details[3] + " Rent" + ".txt", "w")
        file.write(f"\t\t CUSTOMER DETAILS \n")
        file.write("-" * 65)
        file.write("\n")
        file.write(f"Customer Name : {customer_details[0]} \n")
        file.write(f"Phone Number : {customer_details[1]} \n")
        file.write(f"Customer Name : {customer_details[2]} \n")
        file.write(f"Date : {customer_details[3]} \n")
        file.write("-" * 65)
        file.write("\n\n")
        file.write(f"Land Details: \n\n" )
        
        columnNames = ("land ID", "Location", "Direction", "Anna", "Price per Month", "Duration", "Total Amount")
    else:
        file = open(customer_details[0] + " " + customer_details[3] + " Return" + ".txt", "w")
        file.write(f"\t\t CUSTOMER DETAILS \n\n")
        file.write("-" * 65)
        file.write("\n")
        file.write(f"Customer Name : {customer_details[0]} \n")
        file.write(f"Phone Number : {customer_details[1]} \n")
        file.write(f"Customer Name : {customer_details[2]} \n")
        file.write(f"Date : {customer_details[3]} \n")
        file.write("-" * 65)
        file.write("\n\n")
        file.write(f"Land Details: \n\n" )
        
        columnNames = ("land ID", "Location", "Direction", "anna", "price", "Fine", "Price after Fine")
    
    num_cols = len(columnNames)
    header_row = "| " + " | ".join(columnNames) + "  |\n"
    horizontal_line = ("|" + "-" * (len(header_row)-2) + "|\n")
    file.write(horizontal_line)
    file.write(header_row)
    file.write(horizontal_line)
    
    for key, value in bill_dict.items():
        s = "|"
        entry = str(key)
        s += (" "*(len(columnNames[0]) - len(entry)+2) + entry + "|")
        
        for i in range(1, num_cols):
            entry = str(value[i-1])
            s += (" "*(len(columnNames[i]) - len(entry)+2) + entry + "|")
            
        file.write(s + "\n")
    file.write(horizontal_line)
    file.write(f"|Grand Total : {customer_details[4]} \n")
    file.write(horizontal_line) 
      
    print(f"\t\t\t Your bill has been generated")
    print()
    read.print_table(bill_dict, columnNames)
    print(f"|Grand Total : {customer_details[4]}")
    print(horizontal_line)
    print()
        
def update_land_data(bill_dict):
    """Takes parameter bill_dict as dictionary
       modifies land.txt and updates land stock to either available or not available"""
    dict_ = read.generate_dictionary()
    file = open("land.txt", "w")
    for key, value in dict_.items():
        if key in bill_dict:
            if value[4] == 'Available':
                value[4] = 'Not Available'
            else:
                value[4] = 'Available'
        file.write(str(key) + "," + value[0] + "," + value[1] + "," + str(value[2]) + "," + str(value[3]) + "," + value[4])
        file.write("\n")
        
