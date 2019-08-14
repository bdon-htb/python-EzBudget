import os #Import os module for getting file directories.

app_name = 'EzBudget' #Set the application name.

#Set window dimensions.
win_width = 800
win_height = 500
win_size = '{0}x{1}'.format(win_width,win_height)

#Set the directories of the necessary folders.
main_dir = os.path.dirname(__file__) #Get the directory of this module.
ui_dir = os.path.join(main_dir, 'ui') #Get the directory of the ui folder.
font_dir = os.path.join(main_dir, 'font') #Get the directory of the font folder.
data_dir = os.path.join(main_dir, 'data') #Get the directory of the data folder.

