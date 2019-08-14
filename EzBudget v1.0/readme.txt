===========================================================================
Author: Brandon Phillips
===========================================================================
Class/Section: ICS4U
===========================================================================
Date: 12/13/2018
===========================================================================
Version: 1.0
===========================================================================
Unit/Question: CA
===========================================================================
Programming Language: Python 3.x
===========================================================================
Problem Description: An interactive GUI application that allows the user
to keep track of their income and expenses.
===========================================================================
Program Assumptions: User wants to use the program, user has a computer or 
compatible device equipped with Linux/Windows/MacOS, python 3.x, the 
Pygame library and the 'Arial' font installed.
===========================================================================
Feature of Program: Interactive, completely custom and easy to use GUI,
a helpful help menu that can be freely moved around during runtime, a graph
option to help visualize the data, and a stats option to display useful 
stats to the user.
===========================================================================
Restrictions: There is only a pie chart options in the graphs widget,
the user can't manipulate more than one file at a time, there is no auto-
saving feature and only the provided stats in the stats option can be 
displayed ( i.e. the user cannot ask to see a more specific stat).
===========================================================================
Known Errors: None known.
===========================================================================
Implementation Details:
 
Note: If the correct version of python is installed, simply opening the
main.py file should run the application.

-Windows: Open the start menu by pressing the 'Windows' button in the
lower-left corner of the desktop. In the start menu, search 'run' and 
select the application of the same name. Once the run menu is open, type
in cmd and press the Enter key. This should open the windows command
prompt. Once its open, enter the command cd\ + the directory of the folder 
the .py file is in and press Enter again. Finally, enter 'main.py'
.py program (including the .py extension!) and the program should run.

-Mac: Open the terminal program by going into the Utilities folder located
in the Applications folder. Once in the terminal type cd + the name of the 
program's folder directory and press enter. Finally, enter the main.py
and the application should run.

-Linux: Open up the terminal program. The method of doing so varies between
distros (i.e. In GNOME the Terminal is located in the Accessories folder 
inside the Applications folder). Once in the terminal enter cd ~/ + the 
directory of the main.py folder and press enter. Finally enter
main.py program and the program should run! Make sure the script is 
executable through chmod + x prior to running.

Another Note: These instructions assume that the user has access to the
aforementioned programs necessary to run. If the programs aren't available 
due to restrictions please contact your network's administrator for 
further assistance or seek a potential alternative method online.
===========================================================================
Additional Files: Aside from this readme file: main.py, widgets.py, cfg.py, 
and assets.py. All image files in the ui folder, all fonts in the font 
folder, and any necessary data in the data folder.