
    

def generate_dictionary():
    """Reads land.txt file and generates a dictionary after splitting the text into lists and keys
       returns a dictionary"""
    
    file = open("land.txt", "r")
    dict_ = {} 
    lines = file.readlines();
    for each in lines:
        line = each.replace("\n", "").split(",")
        key = int(line[0])
        value = []
        for i in range(1, len(line)):
            value.append(line[i].strip())
        dict_[key] = value
    return dict_
    

    
    
def print_table(land_dict, columnNames):
    """Takes parameters land_dict as dictionary and columnNames as list
        returns none
        prints table of dictionary to shell"""
    
    num_cols = len(columnNames)
    header_row = "| " + " | ".join(columnNames) + " |"
    horizontal_line = ("|" + "-" * (len(header_row)-2) + "|")
    print(horizontal_line)
    print(header_row)
    print(horizontal_line)

    """Generates column lines and row lines according to length of each value in column
        dynamically calculates table length"""
    for key, value in land_dict.items():
        s = "|"
        entry = str(key)
        s += (" "*(len(columnNames[0]) - len(entry)+2) + entry + "|")
        
        for i in range(1, num_cols):
            entry = str(value[i-1])
            s += (" "*(len(columnNames[i]) - len(entry)+2) + entry + "|")
            
        print(s)
    print(horizontal_line)
        
            
