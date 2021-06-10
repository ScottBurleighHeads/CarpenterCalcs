#This was a term two project for Coder Academy. I used my knowledge as a carpenter to build a program that can be used to calculate timber lengths and angles. This program will eliminate human error and increase productivity.

#Carpenters Handy assistant - Scott Malone

Statement of purpose and scope:



- identify the problem it will solve and explain why you are developing it.

This application will give the ability to the user to analyse roof framing components and establish results extremely fast. In the current industry applying the mathematics to solve the 
roofing calculations can be challenging. Alot of carpenters have no idea. I have witnessed some drawing full scale drawings on concrete slabs and walls to get the measurements. Some do have an 
idea themselves but fall back on measuring in situ lengths of timbers they cant calculate. Measuring in situ after basic calculations is the most used operation. It can also be very in-efficient 
due to the fact, manual measurements require labour and time. The labour at times can be difficult due to hard accessed areas, working at heights or limited man power to hold the tape measur. 
Roofing calculations are very systematic meaning they are always built the same way given the style of the build. In contrast, walls are different due to doors and windows can be placed anywhere 
and of different sizes. 

This app is being developed because it has the potential not only to help construction workers establish measurements but will greatly increase productivity. A construction worker only 
needs to take a few given details from a set of plans and input them into the application to be given a table with a cutting list. A future version of the program will use the cutting list to
establish a timber order list relevant to Australian hardwares. It will optimise the minumum amount of timber required. It can also have the ability to analyse costs and determine where the 
cheapest hardware would be to by the materials. 

- explain how a member of the target audience will use it.

Once the program is running in the terminal the program will direct the user on where to go and what do. The terminal has clear instructions with selection menu's amd 
direct questioning to the user to input information. The user will need to gather information from building plans, qualified personal or input the data in themselves if
there designing the job. The user will be given a printed table of results that they can then work from.
- identify the target audience

The target Audience:
        - Project managers : Project managers can use it for establishing expenses and ordering timber supplies.
        - Builders : A builder could use it to establish really fast quotes for clients.
        - Estimators : Estimators could use it for estimating project expenses.
        - Carpenters : Carpenters can use it to increase productivity and to work safer.
        - Well educated DIY personal : Small projects such as dog kennels and cubby houses.


Features:

1) Returns a table full of timber lengths to cut a rectangular gable roof.
2) Returns a table full of timber lengths to cut a rectangular hip roof.
3) Return a list of materials in Australian oderable lenths optimising amount of timber required and increasing productivity . (Incomplete).
4) Menu selection 3 is designed to be swiss army knife of carpentry. Simple tasks to give quick easy solutions. Currently it calculates spacing between timber components.
   
Brief intro description:

Designing the program I thought it productive and easier to interpret and debug if I create my own module of carpentry functions and import them into the main.
I tried to limit the main to menu's, questioning and small scale single use arithmatic.

Description 1) 

To design the algorithm to display a Table for a rectangualar gable roof I first had to break the algorithm into smaller components. Each component of the 
roof had its own algorithm. I created the common_rafter() function that takes in four arguments that the user will take from a set of building plans. Then I had to 
import the math module to perform trigonometric calculations and store the results into local variables. The common rafter function then stores the variables in a dictionary and 
returns the dictionary so the values can be placed in a table. The use of the dictionary is fitting with the algorithm due to being able to label the components of the roof with there values 
and returning the values to be used elsewhere. The main function takes in two parameters and asks the user a series of questions and stores the values in a local dictionary within 
the scope of the gable_rect_build() function. There is then a table algorithm design to take dictionary keys and values and displays them in a table. It does this through 
a nested for loop. The loop excepts and dictionary or nested dictionary and formats into a table.

Description 2)

Rectangular hip roof function has alot of similar code to description 1. I found it not productive to sort the similarities and place the code in a function so there is alot of copy and paste. The hip roof function
does have extra smaller functions attached. I designed a function to find the length and birdsmouth cuts of a hip. The function hip length has four parameters that returns two dictionary key 
and values. Importing the math library with trigonometric functions was required to do the calculations. Another function I created was to find the creepers of the building. Creepers have 
incrementing sizes. Due to creepers being different lengths it was required to store the result in a list of cutting length. To import the calculations I designed a while loop and
the append function to write to the list and return the list to the major function hip_rect_building.

Description 3)

Menu item 2 is incomplete. The project is a bit bigger then anticipated. I wanted to leave it in for future progess and program navigation imagery.

Description 4)

Item 3 in the menu. Currently named set-out for timber components. I want this section to be the swiss army knife of carpentry where there is a large list of carpentry activities that a carpenter can
use to quickly find an answer without paper, pens or the chance of human error. Currently I have two features that can be used. One uses a loop to print where to mark a timber beam to attach structural
timber. The other feature use a bit of arithmatic and a loop to print the layout of balesters in a balustrade insuring equal spacing through out the length of the balustrade. 

Throughout each feature there is try and except functions used to ensure that the user is inputing numeric values and that there not equal to zero. If a user types the wrong code a print statement will be display 
with an error message and the questions will be looped back to the start of the questions

User Interaction and Experience

While the program is in the terminal user interaction is very simple and user experience is non-atmospheric, dull and needs to be well informed to use program. It is a very specific program. you would get the same 
user experience from a calculator. The user will know how to interact with the program because it asks the user direct questions and instructs users through menu choices. The user may miss crucial instructions and return 
a misleading result. For example entering numeric values are mostly in units of meters unless asked otherwise. It is common practice to use millimeters in building and a user may have a bad user experence dealing with that 
concept. A later version I would like to usea mostly GUI to input data. I would like a user to be able to use a mouse to draw the set-out of the building. That would be good user experience.

Control flow diagram




