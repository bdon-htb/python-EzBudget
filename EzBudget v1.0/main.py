#Author: Brandon Phillips
#Date: 12/13/2018
#Name: main.py (EzBudget)
#Description: An interactive GUI application that allows the user to keep track of their income and expenses.

import widgets as w #Import all application widgets.

def run(): #Contains main program loop.
    app = w.MainWin() #Create application.
    app.mainloop() #Run application tkinter loop.

if __name__ == '__main__': #Only run program from this module. 
	run() #run the application.
