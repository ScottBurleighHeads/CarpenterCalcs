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
        

        common_rafter_length = {" - full_length": full_length, " - birdsmouth": birdsmouth}
        return common_rafter_length

def hip_length(pitch,width,eaves_overhang,hip_thickness,ridge_thickness = 0.035):
    #constants
    halfspan = width/2
    hyp_multy = math.sqrt(2)                                           #Creates the mulitplier value to the halfspan for the hypotenuse.
    #x-plane length to birdsmouth
    hip_x_span = halfspan*hyp_multy                                     #Finds the diagonal length or hypotenuse of the x-plane component for the ridge
    apex_x_deduct = (ridge_thickness/2)*hyp_multy   
    birdmouth_x_deduct = hip_thickness/2 
    total_x_birdsmouth = hip_x_span - apex_x_deduct - birdmouth_x_deduct  #Full length to the birdsmouth in the x-plane
 
    #y-plane heights
    rise = halfspan*math.tan(math.radians(pitch))
    apex_y_deduct = (ridge_thickness/2)*math.tan(math.radians(pitch))
    total_y_birdsmouth = rise - apex_y_deduct
    #Pythagorean theorem giving length to birdsmouth to cut 
    length_to_birdsmouth = math.sqrt(total_y_birdsmouth**2 + total_x_birdsmouth**2)
    #Add eaves lining length to hip
    #x-plane_length plus over-hang
    pitch_hip = math.degrees(math.atan(total_y_birdsmouth/total_x_birdsmouth)) #pitch of hip and plumb cut
    hip_x_eave = (halfspan + eaves_overhang)*hyp_multy-apex_x_deduct
    hip_full_length = hip_x_eave/math.cos(math.radians(pitch_hip))
    hip_dict = {"Full length of hip:": round(hip_full_length,3), "Cut Birdsmouth:": round(length_to_birdsmouth,3)}
    
    return hip_dict

def creeper(rafter_length,rafter_birdsmouth,rafter_spacing,pitch):
    creeper_list = []
    creeper_decrement = rafter_spacing/math.cos(math.radians(pitch))
    creeper = rafter_length - creeper_decrement
    
    while creeper > ( 0 + rafter_length - rafter_birdsmouth):
        creeper_list.append(round(creeper,3))
        creeper = creeper - creeper_decrement
    return creeper_list
    
def gable_rect_build(length,width): #function to solve all the roofing requirement to frame a rectangular roof.
    
     while True:    # Gathering crucial information and storing in a dictionary.
        try:
            dict_table = {"Pitch:": [],
                          "Eave overhang:": [],
                          "Barge overhang:": [],
                          "Ridge:": {"Thickness:":[],"Length:":[]}, 
                          "Rafter spacing:": [], 
                          "Rafter lengths:": {"Total length:": [],"Length to birdsmouth:":[]}, 
                          "Number of rafters:": []}
            
            print ("\nEnter only the numbers of all of the following measurement in meters unless requested otherwise." 
                   "The input list will repeat if instructions are not followed.\n")
            dict_table["Pitch:"] = float(input("Enter the pitch of the roof in degrees: "))
            dict_table["Eave overhang:"]= float(input("\nEnter the overhang of the eaves: "))
            dict_table["Barge overhang:"] = float(input("\nEnter the overhang of the barge: "))
            
            barge = ""
            while barge != "yes" and barge != "no":
                barge = input("\nIs the barge on both sides of the property: type yes or no: ")
                barge.lower()
                if barge == 'yes':
                    dict_table["Ridge:"]["Length:"] = length + 2*dict_table["Barge overhang:"]
                elif barge == 'quit':
                    break
                else:
                    dict_table["Ridge:"]["Length:"] = length + dict_table["Barge overhang:"]
            
            dict_table["Ridge:"]["Thickness:"] = float(input("\nEnter the thickness of the ridge: ")) 
            dict_table["Rafter spacing:"] = float(input("\nEnter the spacing of your rafters in meters: "))
            dict_table["Rafter lengths:"] = common_rafter(dict_table["Pitch:"],width,dict_table["Eave overhang:"],
                                                          dict_table["Ridge:"]["Thickness:"])
            dict_table["Number of rafters:"] = ((math.ceil((length+dict_table["Barge overhang:"]*2)/dict_table["Rafter spacing:"])) +1)*2
            break
        except ZeroDivisionError:
            print("Error. You used zero in denominator or numerater.")
        except Exception as error:
            print("Invalid input. Enter only numbers")
            
       
                
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

def hip_rect_build(length,width):


    while True:    # Gathering crucial information and storing in a dictionary.
        try:
            dict_table = {"Pitch:": [],
                          "Eave overhang:": [],
                          "Ridge:": {" - Thickness:":[]," - Length:":[]}, 
                          "Rafter spacing:": [], 
                          "Rafter lengths:": {"Total length:": [],"Length to birdsmouth:":[]}, 
                          "Number of rafters:": []}
            
            print ("\nEnter only the numbers of all of the following measurement in meters unless requested otherwise." 
                   "The input list will repeat if instructions are not followed.\n")
            dict_table["Pitch:"] = float(input("Enter the pitch of the roof in degrees: "))
            dict_table["Eave overhang:"]= float(input("\nEnter the overhang of the eaves: "))
            dict_table["Ridge:"][" - Thickness:"] = float(input("\nEnter the thickness of the ridge: ")) 
            dict_table["Rafter spacing:"] = float(input("\nEnter the spacing of your rafters in meters: "))
            dict_table["Rafter thickness"] = float(input("\nEnter the thickness of the rafters: "))
            dict_table["Hip Thickness"] = float(input("\nEnter the thickness of the the hip: "))
            
            
            dict_table["Rafter lengths:"] = common_rafter(dict_table["Pitch:"],
                                                          width,dict_table["Eave overhang:"],
                                                          dict_table["Ridge:"][" - Thickness:"])
            
            dict_table["Crown end length:"] = common_rafter(dict_table["Pitch:"],
                                                            width - dict_table["Rafter thickness"],
                                                            dict_table["Eave overhang:"],
                                                            dict_table["Ridge:"][" - Thickness:"])
            dict_table["Number of crown ends"] = 2
            
            dict_table["Ridge:"][" - Length:"] = length - width + dict_table["Rafter thickness"]
            
            dict_table["Hip length: "]= hip_length(dict_table["Pitch:"],
                                                 width,
                                                 dict_table["Eave overhang:"],
                                                 dict_table["Hip Thickness"],
                                                 dict_table["Ridge:"][" - Thickness:"])
            
            dict_table["Creeper length pairs: "] = creeper(dict_table["Rafter lengths:"][" - full_length"],
                                                      dict_table["Rafter lengths:"][" - birdsmouth"],
                                                      dict_table["Rafter spacing:"],
                                                      dict_table["Pitch:"])
            
            dict_table["Number of rafters:"] = ((math.ceil(dict_table["Ridge:"][" - Length:"]/dict_table["Rafter spacing:"])) +1)*2

    
            break
        
        except ZeroDivisionError:
            print("Error. You used zero in the denominator or numerater.")
        
        except Exception as error:
            print("Invalid input. Enter only numbers")
            
       
                
    #Creating a Table to print

    high_str_len = 0
    for key in dict_table: #Finding the longest length of the keys to set the width of the table
        a = (len(key))
        if a > high_str_len:
            high_str_len = len(key)+ 26
        
        
    print("\n")
    print("Item\t\t\t\tunits\n")
    for key in dict_table:
        if isinstance(dict_table.get(key),float) == True or isinstance(dict_table.get(key),int) == True:
            space = " "*(high_str_len - len(key))
            print(f"{key}{space}{str(dict_table[key])}")
        elif isinstance(dict_table.get(key),int) == False and isinstance(dict_table.get(key),float) == False:
                
            print(key)
            for item in dict_table[key]:
                try:
                    space = " "*(high_str_len - len(item))
                    print(f"{item}{space}{str(dict_table[key][item])}")
                except:
                    pass
    print(dict_table["Creeper length pairs: "])
    

          
              






