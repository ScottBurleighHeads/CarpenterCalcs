import component_functions
user = ""
while True:
    print("\nSelect an option by typing a relevant number.")
    user = int(input("""
        1. Roof calulations.
        2. Materials list.
        3. Setout for timber componernts.
        4. Exit.

    Selction: """))
    if user == 4:
        break
    if user == 1:
        roof_type = ""
        while roof_type != "gable" or roof_type != "hip":
            roof_type = input("\nType \"gable\" or \"hip\" for the type of roof to be installed: ")
            roof_type.lower()
            if roof_type == "gable" or roof_type == "hip":
                break
            else:
                print("Invalid entry. Type only gable or hip: ")
                print(roof_type)
        layout_type = ""
        while layout_type != "a" or layout_type != "b":
            layout_type = input("""\nSelect a or b for the layout of the building:
            a)                       b)
             _____________________       ____________________
             |                   |       |                  |
      Width  |                   |       |                  | 
             |                   |       |                  |
             |___________________|       |__________        |
                    Length                          |       |
                                                    |       |
                                                    |       |
                                                    |_______|
        
            selection: """)
            
            layout_type.lower()
            if layout_type == "a":

                    length = float(input("Enter the length of the building in meters: "))
                    width = float(input ("Enter the width of the building in meters: "))
                    if roof_type == "gable":
                        component_functions.gable_rect_build(length,width)
                        break
                    elif roof_type == "hip":
                        component_functions.hip_rect_build(length,width)
                        break
            
            elif layout_type == "b":
                print(component_functions.L_building_values()) # Prints a layout of the building with reference to the lengths of the walls
                print("\nStill a work in progress.")
                input("Press enter to return to the menu")
                break
            else:
                print("\nInvalid input. Type a or b:")
    elif user == 2:
        print("\nStill a work in progress\n")
        input("Press enter to return to the main menu.")
    elif user == 3:
        while True:
            sel = int(input("""
            1. Baluster spacing
            2. stud spacing for walls
            3. Exit

            selection: """))
            print("\n")
            if sel == 1:
                while True:
                    try:
                        print("The measurements entered will set equal spacing from start to finish.\n")
                        print("Enter all measurements in meters\n")
                        length = float(input("Enter the opening length between the posts to place the balesters: "))
                        width_material = float(input("Enter the width of the balesters: "))
                        approx_spacing = float(input("Enter the approximate length of the gap between balesters: "))
                        print("Mark the handrails at measurements below and place the balester on the inside edge of the mark:\n")
                        component_functions.balustrade(length,width_material,approx_spacing)
                        input("\nPress enter to go back to the menu")
                        break
                    except Exception in error:
                        print("\nInvalid input.")
                        raise(error)
            elif sel == 2:
                while True:
                    print("Enter all measurements in meters.\n")
                    length = float(input("What is the length of the walls: "))
                    spacing = float(input("Enter the spacing: "))
                    if spacing < length:
                        break
                    else:
                        print("Invalid input. Please re-enter an input.") 
                
                sum_spaces = float(0)
                sum_list = []
                while sum_spaces < length:
                    list_item = round(sum_spaces,3)
                    sum_list.append(list_item)
                    sum_spaces += spacing
                sum_list.append(length)
                print("Mark plates at measurements shown below:\n")
                print(*sum_list, sep=",")
                input("\nPress enter to return to the main menu")
            else:
                break

    
