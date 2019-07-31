# super_tg_graphing
Setting up super_tg_graphing:
If you are unfamiliar with python I reccomend starting with downloading and installing pyzo(https://pyzo.org/). 
It is an integrated development environment which makes getting started with python fairly straightforward.
This program requires matplotlib, easygui, and pandas to run. If you are running a python version earlier than 3.7 you will also need to install tkinter(https://tkdocs.com/tutorial/install.html)
Note: I had issues running this with python 3.7 which were resolved when I installed the pillow package

This program is used for analyzing data outputted by SUPER_TG and comparing it to measured garnet traverses.
To use this program simply run main.py with python or python3 and follow the prompts. 


CSV file formatting:
Please format the csv file with the following header: 
x (mm),Ca,Mg,Fe,Mn 
Please avoid empty cells
If you are using a half traverse instead of a full one, the program assumes that 0 is at the center of the garnet


What this program does:
First this program will prompt you for the file locations of your SUPER_TG output and the csv file you have stored your garnet measurements
Next it plots the traverse and prompts you choose a place to split it. This is to compare it with the SUPER_TG output which is only a half traverse.
This will move x = 0 to the chosen core of the garnet.
If your csv file is a half traverse you may simply exit the window without making a selection. 


This will now plot the modelled profiles on top of the measured profiles. In a seperate window, the PT paths of the models will be plotted. 

More addiitons will be coming including:

-Statistical evaluation of how well each model matches the traverse
-Slection of an individual model, to highlight the corresponding profiles on each subplot as well as the corresponding PT path