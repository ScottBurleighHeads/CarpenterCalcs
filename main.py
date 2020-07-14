import component_functions

user = ""
while user != 4:
    print("\nSelect an option by typing a relevant number.")
    user = int(input("""
        1. Roof calulations.
        2. Materials list.
        3. Setout for timber componernts.
        4. Exit.

    Selction: """))

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
    while layout_type != "a" or layout_type != "b" :
        layout_type = input("""\nSelect a or b for the layout of the building:
        a)                       b)
         _____________________       ____________________
         |                   |       |                  |
         |                   |       |                  | 
         |                   |       |                  |
         |___________________|       |__________        |
                                                |       |
                                                |       |
                                                |       |
                                                |_______|
    
    selection: """)
        
        if layout_type == "a":

            length = input("Enter the length in meters: ")
            width = input ("Enter the width in meters: ")
            break
        
        elif layout_type == "b":
            print(component_functions.L_building_values()) # Prints a layout of the building with reference to the lengths of the walls
            break
        else:
            print("\nInvalid input. Type a or b:")        
            
        

    
