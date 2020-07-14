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
    

def gable_rect_build(length,width):
         print ("Enter all of the following measurement in meters.\n")
         pitch = float(input("Enter the pitch of the roof in degrees: "))
         eaves = float(input("\nEnter the width of the eaves: "))
         barge = float(input("\nEnter the overhang of the barge: "))
         ridge_thickness  = float(input("\nEnter the thickness of the ridge: ")) 
         spacing = float(input("\nEnter the spacing of your rafters in meters: "))
         rafter = common_rafter(pitch,width,eaves,ridge_thickness)
         Num_rafters = ((length+barge*2)/spacing +1)*2

gable_rect_build(20,10)
         






