import math

def L_building_values():
    print ("""
                     (a)
             ____________________
             |                  |
         (f) |                  | 
             |                  |
             |___________       | (b)
                  (e)   |       |
                        |       |
                     (d)|       |
                        |_______|
                           (c)
                            
            """)
    dict_values = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[]}
    count = 0
    for key in dict_values:
    
        dict_values[key] = int(input(f"Enter the value {key}: "))
        count+= 1

    return dict_values

def common_rafter(pitch,width,eaves_overhang,ridge_thickness = 0.035):

        cos_degrees = math.radians(30)
        cos_theta = math.cos(cos_degrees)

        calc_full_span = width/2 + eaves_overhang - ridge_thickness/2
        calc_birdsmouth = width/2 - ridge_thickness/2
        
        full_length = round(calc_full_span/cos_theta,3)
        
        birdsmouth = round(calc_birdsmouth/cos_theta,3)
        

        common_rafter_length = {"full_length": full_length, "birdsmouth": birdsmouth}
        return common_rafter_length
    

def gable_rect_build(length,width): #function to solve all the roofing requirement to frame a rectangular roof.

         # Gathering crucial information and storing in a dictionary.
         dict_table = {"Pitch:": [],"Eave overhang:": [],"Barge overhang:": [],"Ridge thickness and length:": {"Thickness:":[],"Length:":[]}, 
                       "Rafter spacing:": [], "Rafter lengths:": {"Total length:": [],"Length to birdsmouth:":[]} , "Number of rafters:": []}
         print ("Enter all of the following measurement in meters.\n")
         dict_table["Pitch:"] = float(input("Enter the pitch of the roof in degrees: "))
         dict_table["Eave overhang:"]= float(input("\nEnter the overhang of the eaves: "))
         barge = ""
         dict_table["Barge overhang:"] = float(input("\nEnter the overhang of the barge: "))
         while barge != 'yes' and barge != 'no':
            barge = input("\nIs the barge on both sides of the property: type yes or no: ")
            barge = barge.lower()
            if barge == 'yes':
                dict_table["Ridge thickness and length:"]["Length:"] = length + 2*dict_table["Barge overhang:"]
            else:
                dict_table["Ridge thickness and length:"]["Length:"] = length + dict_table["Barge overhang:"]
         dict_table["Ridge thickness and length:"]["Thickness:"] = float(input("\nEnter the thickness of the ridge: ")) 
         dict_table["Rafter spacing:"] = float(input("\nEnter the spacing of your rafters in meters: "))
         dict_table["Rafter lengths:"] = common_rafter(dict_table["Pitch:"],width,dict_table["Eave overhang:"],dict_table["Ridge thickness and length:"]["Thickness:"])
         dict_table["Number of rafters:"] = ((math.ceil((length+dict_table["Barge overhang:"]*2)/dict_table["Rafter spacing:"])) +1)*2
         
         #Creating a Table to print

         high_str_len = 0
         for key in dict_table: #Finding the longest length of the keys to set the width of the table
            a = (len(key))
            if a > high_str_len:
                high_str_len = len(key)+ 5
         
         
         print("\n")
         print("Item\t\t\t\tUnit\n")
         for key in dict_table:
            if isinstance(dict_table.get(key),float) == True or isinstance(dict_table.get(key),int) == True:
                space = " "*(high_str_len - len(key))
                print(f"{key}{space}{str(dict_table[key])}")
            elif isinstance(dict_table.get(key),int) == False and isinstance(dict_table.get(key),float) == False:
                
                print(key)
                for item in dict_table[key]:
                    space = " "*(high_str_len - len(item))
                    print(f"{item}{space}{str(dict_table[key][item])}")
                
                

gable_rect_build(20,10)
         






