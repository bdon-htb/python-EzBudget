import cfg, assets #Import other .py files.
from assets import colours #Import the colours dict individually because it's used pretty frequently.
#Tkinter imports

import tkinter as tk #Import tkinter.
from tkinter import filedialog #Handles windows explorer saving/opening.

import matplotlib #All matplotlib imports handle the graphing feature.
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class MessageBox(tk.Toplevel):
    def __init__(self, width=300, height=100, message='This is a message!', bg=colours['silver'], offset_x=0, offset_y=0):
        tk.Toplevel.__init__(self) #Initialize toplevel/window component.
        #Define the window's dimensions from the parameters.
        self.width = width
        self.height = height
        self.config(bg=bg) #Configure the background colour.
        self.setPosition(offset_x, offset_y) #Set the position of the window.
        self.message = tk.Label(self, text=message, fg=colours['darkgreen'], font=(assets.fonts['title'],10)) #Set the message font, colour, etc.
        self.message.pack() #Add the message to the gui. 
        self.slidebutton = tk.Button(self, text='Dismiss', command=self.destroy, fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green']) #Create the button to progress slides.
        self.slidebutton.pack() #Add the button to the gui.

    def setPosition(self, offset_x, offset_y): #Set the offset of the window based on the parent window.
        self.size = '{0}x{1}'.format(self.width, self.height) #Get the size variable from the window's predefined dimensions.
        self.offset = (str(offset_x - int(self.width/2.5)), str(offset_y + int(self.height/2))) #Create offset tuple.
        self.geometry('{0}+{1}+{2}'.format(self.size, self.offset[0], self.offset[1])) #Configure the tkinter geometry attribute.
        self.resizable(width=False, height=False) #Prevent the window from being resizable.

class CreateBox(tk.Toplevel): #Window that enables the user to create a new file.
    def __init__(self, parent, width=300, height=100, bg=colours['silver'], offset_x=0, offset_y=0):
        tk.Toplevel.__init__(self) #Initialize toplevel/window component.
        self.parent = parent #Get the parent widget and store as attribute for future reference.
        #Define the window's dimensions from the parameters.
        self.width = width 
        self.height = height
        self.config(bg=bg) #Configure the background colour.
        self.setPosition(offset_x, offset_y) #Set the position of the window.
        self.message = tk.Label(self, text='What would you like to call the file? (without .txt)', fg=colours['darkgreen'], font=(assets.fonts['title'],10)) #Set the message font, colour, etc.
        self.message.pack() #Add the message to the gui. 
        self.entry = tk.Entry(self) #Create the entry box for user input.
        self.entry.pack() #Add the entry box to gui.
        self.createbutton = tk.Button(self, text='Create New File', command=lambda: self.createNewFile(), fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green']) #Create the button that makes the new file.
        self.createbutton.pack(pady=(20,0)) #Add button to gui.

    def setPosition(self, offset_x, offset_y): #Set the offset of the window based on the parent window.
        self.size = '{0}x{1}'.format(self.width, self.height) #Get the size variable from the window's predefined dimensions.
        self.offset = (str(offset_x - int(self.width/2.5)), str(offset_y + int(self.height/2))) #Create offset tuple.
        self.geometry('{0}+{1}+{2}'.format(self.size, self.offset[0], self.offset[1])) #Configure the tkinter geometry attribute.
        self.resizable(width=False, height=False) #Prevent the window from being resizable.

    def createNewFile(self):
        file = self.entry.get() #Get the string in the entry box.

        banned_chars = ['\\', '/', ':', '*', '?', '<', '>', '|'] #Characters that cannot be used in file names.
        for char in banned_chars: #Iterate through every banned character.
            if char in file: #Check if character is in string.
                file = file.replace(char,'') #Remove from string.

        if file.replace(' ','').replace('\n','') != '': #Check for whitespace, escape characters, etc.
            file = '{0}\\{1}.txt'.format(cfg.data_dir, file) #Set the file name and location based on the user input and directory.
            with open(file, 'w') as f: #Open/Create file.
                f.write('Expense/Income, Name, Amount, Description\n') #Write first line of every valid data file.

            self.parent.file = file #Set the program file as the current written file.
            self.parent.open(open_explorer=False) #Open the file without opening windows explorer.
            self.parent.openEntryForm() #Allow the user to add it's first entry to the table.
            self.destroy() #Destroy/close the widget.

class TableEntryBox(tk.Toplevel):
    def __init__(self, parent, width=280, height=170, bg=colours['silver'], offset_x=0, offset_y=0):
        tk.Toplevel.__init__(self) #Initialize toplevel/window component.
        self.parent = parent #Get the parent widget and store as attribute for future reference.
        #Define the window's dimensions from the parameters
        self.width = width
        self.height = height
        self.config(bg=bg)  #Configure the background colour.
        self.setPosition(offset_x, offset_y)
        self.title = tk.Label(self, text='Please fill out the following form:', fg=colours['darkgreen'], font=(assets.fonts['title'],10))
        self.title.grid(row=0, columnspan=2)
        self.createEntries()
        self.okbutton = tk.Button(self, text='Insert Into Table', command=lambda: self.getInfo(), fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'])
        self.okbutton.grid(row=6, columnspan=2, pady=(20,0))

    def createEntries(self):
        self.trans_label = tk.Label(self, text='Transaction Type:', font=(assets.fonts['title'],10), fg=colours['darkgreen'])
        self.trans_label.grid(row=1,column=0, sticky='W')
        self.trans_var = tk.StringVar(self)
        self.trans_var.set('Income')
        self.trans_entry = tk.OptionMenu(self, self.trans_var, 'Income', 'Expense')
        self.trans_entry.config(fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=1, activebackground=colours['green'], width=14)
        self.trans_entry['menu'].config(fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0)
        self.trans_entry.grid(row=1,column=1, sticky='W')

        self.name_label = tk.Label(self, text='Name of Transaction:',font=(assets.fonts['title'],10), fg=colours['darkgreen'])
        self.name_label.grid(row=2,column=0, sticky='W')

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=2,column=1, sticky='W')

        self.amount_label = tk.Label(self, text='Amount:',font=(assets.fonts['title'],10), fg=colours['darkgreen'])
        self.amount_label.grid(row=3,column=0, sticky='W')
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=3,column=1)

        self.desc_label = tk.Label(self, text='Description (Optional):', font=(assets.fonts['title'],10), fg=colours['darkgreen'])
        self.desc_label.grid(row=4,column=0, sticky='W')
        self.desc_entry = tk.Entry(self)
        self.desc_entry.grid(row=4, column=1, sticky='W')

    def setPosition(self, offset_x, offset_y): #Set the offset of the window based on the parent window.
        self.size = '{0}x{1}'.format(self.width, self.height)
        self.offset = (str(offset_x + int(self.width/1.10)), str(offset_y + int(self.height/2))) #Create offset tuple.
        self.geometry('{0}+{1}+{2}'.format(self.size, self.offset[0], self.offset[1])) #Configure the tkinter geometry attribute.
        self.resizable(width=False, height=False)

    def getInfo(self):
        entry_info = [] #Initialize empty list.
        for entry in [self.trans_var, self.name_entry, self.amount_entry, self.desc_entry]:
            x_entry = entry.get()
            if x_entry.replace(' ','').replace('\n','') != '':
                entry_info.append(' '+ x_entry)
            else:
                entry_info.append(' None')

        table = self.parent.workspace.table
        table.addRow()
        for x in range(0, 4):
            table.entries[table.max_rows-1][x].insert('end', entry_info[x])
        self.destroy()

class HelpMenu(tk.Toplevel):
    def __init__(self, width=400, height=270, bg=colours['silver'], offset_x=0, offset_y=0):
        tk.Toplevel.__init__(self) #Initialize toplevel/window component.
        #Define the window's dimensions from the parameters
        self.width = width
        self.height = height
        self.config(bg=bg) #Configure the background colour.
        self.setPosition(offset_x, offset_y)
        self.slide_num = 0
        self.slides = [tk.PhotoImage(file=assets.help_menu['buttons']), tk.PhotoImage(file=assets.help_menu['menus']), tk.PhotoImage(file=assets.help_menu['steps'])]
        self.current_img = tk.Label(self, image=self.slides[0])
        self.nextbutton = tk.Button(self, text='Next Slide', fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], command=lambda:self.changeSlide())
        self.current_img.pack(side='top')
        self.nextbutton.pack(side='bottom', pady=(0,20))

    def setPosition(self, offset_x, offset_y): #Set the offset of the window based on the parent window.
        self.size = '{0}x{1}'.format(self.width, self.height)
        self.offset = (str(offset_x - int(self.width/2.5)), str(offset_y + int(self.height/2))) #Create offset tuple.
        self.geometry('{0}+{1}+{2}'.format(self.size, self.offset[0], self.offset[1])) #Configure the tkinter geometry attribute.
        self.resizable(width=False, height=False)

    def changeSlide(self):
        self.slide_num += 1
        if self.slide_num > 2: #Check that it doesn't exceed the maximum index in list..
            self.slide_num = 0
        self.current_img.config(image=self.slides[self.slide_num])


class TitleBar(tk.Frame):
    def __init__(self, parent): #Initialize frame component.
        tk.Frame.__init__(self)
        self.config(background=colours['lightgreen']) #Set the background and dimensions.      
        self.createImages() #Load all images in titlebar.
        self.createTitle(parent) 
        self.createExitButton(parent) #Create the exitbutton.
        self.title.pack(side='left', padx=(486,0)) #Add to titlebar to gui.
        
    def createImages(self): #Load all images into PhotoImage objects.
        self.logo = tk.PhotoImage(file=assets.ui['logo'])
        self.exit_active = tk.PhotoImage(file=assets.ui['exit_button'][0])
        self.exit_inactive = tk.PhotoImage(file=assets.ui['exit_button'][1])

    def createTitle(self, parent):
        self.title = tk.Label(self, image=self.logo, bg=colours['lightgreen']) #Create a Label using the logo image.
        #Bind the frame to allow the user to move the entire window by dragging it.
        self.title.bind('<ButtonPress-1>', parent.startMove)
        self.title.bind('<ButtonRelease-1>', parent.stop)
        self.title.bind('<B1-Motion>', parent.onMotion)
        
    def createExitButton(self, parent): #Create the exitbutton.
        self.exitbutton = tk.Button(self, image=self.exit_inactive, command=parent.destroy, bg=colours['lightgreen'], borderwidth=0, activebackground=colours['lightgreen'])
        self.exitbutton.pack(side='right',padx=10) #Add to gui.
        #Bind the button to allow the colour to change when the mouse enters and exits its location.
        self.exitbutton.bind('<Enter>',self.setButtonImage)
        self.exitbutton.bind('<Leave>',self.setButtonImage) 

    def setButtonImage(self, event): #Change the image od the exit button.
        event = str(event.type)
        if event == 'Enter': #Check if the event is the mouse cursor entering the widget.
            self.exitbutton.config(image=self.exit_active) #Make the button light up.
        elif event == 'Leave': #Check if the event is the mouse cursor leaving the widget.SB
            self.exitbutton.config(image=self.exit_inactive) #Default the button image.

class Menu(tk.Frame): #Contains all the buttons located at the top of the window.
    def __init__(self, parent):
        tk.Frame.__init__(self) #Initialize frame componet.
        self.config(background=colours['darkgreen']) #Set the colour and dimensions of toolbar.
        self.createImages() #Load all necessary assets into images.
        self.createToolButtons(parent)

    def createImages(self): #Load all images.
        self.img_waffle = tk.PhotoImage(file=assets.ui['waffle'])

    def createToolButtons(self, parent):
        self.waffle = tk.Button(self, image=self.img_waffle, bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'],command=lambda:parent.toggleToolBox(True)) #Waffle expands and minimizes toolbar.
        self.waffle.grid(row=0,column=0, pady=3, ipadx=5)

        self.filebutton = tk.Menubutton(self, font=(assets.fonts['title'], 12), text='File', fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], highlightcolor=colours['green'])
        self.filebutton.grid(row=0,column=1)
        self.filemenu = tk.Menu(self.filebutton, tearoff=0, bd=0, bg=colours['darkgreen'], font=(assets.fonts['title'], 8), fg=colours['lightgreen'])
        self.filemenu.add_command(label='New File', command=lambda:parent.new())
        self.filemenu.add_command(label='Open File', command=lambda:parent.open())
        self.filemenu.add_command(label='Save File', command=lambda:parent.save())
        self.filebutton['menu'] = self.filemenu
        self.helpbutton = tk.Button(self, font=(assets.fonts['title'], 12), text='Help', fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], highlightcolor=colours['green'], command=lambda:parent.openHelpForm())
        self.helpbutton.grid(row=0,column=2, padx=(0,5))

class ToolBox(tk.Toplevel):

    def __init__(self, parent, bg=colours['darkgreen']):
        tk.Toplevel.__init__(self) #Create window.
        self.overrideredirect(True) #Allows complete customization of how the window is handled.
        self.config(bg=bg)
        self.setPosition(parent)
        self.createImages()
        self.createButtons(parent)

    def createImages(self):
        self.img_editdata = tk.PhotoImage(file=assets.ui['edit_data'])
        self.img_graphs = tk.PhotoImage(file=assets.ui['graphs'])
        self.img_stats = tk.PhotoImage(file=assets.ui['stats'])

    def createButtons(self, parent):
        self.editbutton = tk.Button(self, image=self.img_editdata, bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], command=lambda:parent.workspace.displayTable()) #Edit button opens data edit menu.
        self.editbutton.grid(row=0,column=0)
        self.editlabel = tk.Label(self, text='Data', font=(assets.fonts['title'], 8), bg=colours['darkgreen'], fg=colours['lightgreen'])
        self.editlabel.grid(row=1)

        self.graphbutton = tk.Button(self, image=self.img_graphs, bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], command=lambda:parent.workspace.displayGraph()) #Edit button opens data edit menu.
        self.graphbutton.grid(row=2)
        self.graphlabel = tk.Label(self, text='Graphs', font=(assets.fonts['title'], 8), bg=colours['darkgreen'], fg=colours['lightgreen'])
        self.graphlabel.grid(row=3)

        self.statsbutton = tk.Button(self, image=self.img_stats, bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], command=lambda:parent.workspace.displayStats()) #Edit button opens data edit menu.
        self.statsbutton.grid(row=4)
        self.statslabel = tk.Label(self, text='Stats', font=(assets.fonts['title'], 8), bg=colours['darkgreen'], fg=colours['lightgreen'])
        self.statslabel.grid(row=5)

    def setPosition(self, parent): #Set the offset of the window based on the parent window.
        offset_x = 0
        offset_y = 33
        self.size = '42x156'
        self.offset = (str(parent.winfo_x() + offset_x), str(parent.winfo_y() + offset_y)) #Create offset tuple.
        self.geometry('{0}+{1}+{2}'.format(self.size, self.offset[0], self.offset[1])) #Configure the tkinter geometry attribute.
        
    def close(self): #Destroy the window.
        self.destroy()

class Workspace(tk.Frame): #Includes all the data manipulation widgets.
    def __init__(self, parent):
        tk.Frame.__init__(self) #Initialize frame component.
        self.parent = parent #Get the parent widget and store as attribute for future reference.
        self.bg = colours['silver'] #Configure the background colour.
        self.fg = colours['darkgreen'] #Configure the font colour.
        self.message = [0] #Initialize message object as list. (for referencing purposes)
        self.data = [] #Initialize table data as blank list.
        self.stats = None #Initialize stats widget.
        self.config(background=self.bg, height=468, width=800) #Set the background and dimensions.      
        #Set the startup welcome texts. 
        welcome_text = 'Welcome to EzBudget!' 
        empty_text = 'There is currently no file open. To get started, please press the \'Help\' button in the top left corner of this window.'
        #Convert the texts into tkinter label objects.
        self.welcome_label = tk.Label(self, text=welcome_text, font=(assets.fonts['title'],36), bg=self.bg, fg=self.fg, justify='center', wraplength=500)
        self.empty_label = tk.Label(self, text=empty_text, font=(assets.fonts['title'],12), bg=self.bg, fg=self.fg, justify='center', wraplength=500)
        self.entrybutton = tk.Button(self, font=(assets.fonts['title'], 10), text='Add New Entry', fg=colours['lightgreen'], bg=colours['darkgreen'], borderwidth=0, activebackground=colours['green'], highlightcolor=colours['green'], command=lambda:self.addTableEntry())
        #Create widgets.
        self.table = Table()
        self.graph = Graph(self)
        self.displayEmptyLabels() #Display the welcome messages.

    def displayEmptyLabels(self): #Display message if mode is currently empty.
        self.empty_label.pack(side='bottom',pady=(0,0))
        self.welcome_label.pack(side='top',pady=(150,0))

    def removeEmptyLabels(self): #Remove messages.
        self.empty_label.pack_forget()
        self.welcome_label.pack_forget()

    def displayTable(self): #Display the table.
        self.parent.toggleToolBox(False) #Close the toolbox.
        #Remove any widgets that are open.
        self.removeEmptyLabels()
        self.removeStats()
        self.removeGraph()
        #Add the table components to the gui.
        self.entrybutton.grid(row=1,column=0, pady=(5,10), sticky='W')
        self.table.grid(row=2, columnspan=2, sticky='S')

    def removeTable(self): #Remove the table.
        self.entrybutton.grid_forget()
        self.table.grid_forget()

    def displayGraph(self): #Display graph widget.
        self.parent.toggleToolBox(False) #Close the toolbox.
        #Remove any widgets that are open.
        self.removeEmptyLabels()
        self.removeStats()
        self.removeTable()
        self.graph.plot() #Calculate the data and plot the graph.
        self.graph.grid(row=1, columnspan=2, sticky='S', pady=(25,0)) #Add the graph to the gui.

    def removeGraph(self): #Remove the graph.
        self.graph.grid_forget()

    def displayStats(self): #Display the stats widget.
        self.parent.toggleToolBox(False) #Close the toolbox.
        #Remove any widgets that are open.
        self.removeEmptyLabels()
        self.removeTable()
        self.removeGraph()
        self.stats = StatsPage(self) #Create and calulate stats widget.
        self.stats.display() #Configure the stats display.
        self.stats.grid(row=1, columnspan=2, sticky='S', pady=(10,0)) #Add stats widget to gui.

    def removeStats(self): #Remove the stats widget.
        if self.stats != None: #Check if stats widget isn't already removed.
            self.stats.clear() #Clear the stats widget.
            self.stats.grid_forget()
            self.stats.destroy()
            self.stats = None #Reset back to None value.

    def addTableEntry(self): #Add another row to the table.
        if self.table.max_rows + 1 <= 20: #Check that user will not exceed table limit. (20 rows)
            self.parent.openEntryForm() #Open entry window for adding another row.
        else: #Else; assume limit has been reached.
            self.update() #Update the window
            #Calculate the window position.
            offset_x = self.winfo_rootx()
            offset_y = self.winfo_rooty()
            self.entrybutton.update() #Update the entry button.
            self.message = MessageBox(height=50, message='No more entries can be added. (max is 20)', offset_x=offset_x, offset_y=offset_y) #Create message alerting user limit has been reached.

class Table(tk.Frame):
    def __init__(self, file='data.txt'):
        tk.Frame.__init__(self)
        self.max_columns = 4 #Initialize maximum number of rows as 4 because there are 4 categories.
        self.max_rows = 0 #Initialize maximum number of columns as 0.
        self.entries = [] #Initialize tkinter entry widget list as blank list.

    def populateTable(self, file):
        #type, name, amount, desc, repeats
        self.content = [] #Initialize as empty list.
        with open(file, 'r') as f: #Open text file.
            for line in f: #Iterate through ever line.
                if line.replace(' ', '').replace('\n','') != '': #Check that there is no white spaces in file.
                    self.content.append(line.strip('\n')) #Add line to content list; strip away any whitespace.

        for items in range(0, len(self.content)): #Loop for as many times as they're items in content.
            self.content[items] = self.content[items].split(',') #Turn content into a 2d array.

            if len(self.content[items]) > 4: #Check if the line includes more than 4 categories (potential error).
                self.content[items] = self.content[items][:4] #Only include up to the first 4 elemnts (trim).
            elif len(self.content[items]) < 4: #Check if the line includes less than 4 categories (potential error).
                for x in range(0, 4):
                    if x > len(self.content[items]) - 1: #Check loop is exceeding the size of list.
                        self.content[items].append(' None')  #Append the 'None' string to list.

        for row in range(0, len(self.content)): #Loop for as many times as they're rows in table.
            row_entries = [] #Initialize local variable as blank list.
            for column in range(0,self.max_columns): #Loop for as many times as they're columns in table.
                entry = tk.Entry(self, font=(assets.fonts['title'], 10), fg=colours['darkgreen'], borderwidth=1) #Create tkinter entry object.
                entry.insert(0, self.content[row][column]) #Write the contents of the file into the table.
                if row == 0: #Check if it's the first row.
                    entry.config(disabledbackground=colours['darkgreen'], disabledforeground=colours['lightgreen'],state='disabled')
                else:
                    entry.config(bg=colours['lightgreen'])
                entry.grid(row=row,column=column)
                row_entries.append(entry) #Collect the individual entry into the row list.
            self.entries.append(row_entries) #Collect all entries in a single row in list.

        self.max_rows = len(self.content) #Record the number of rows for later use.
    
    def addRow(self):
        self.max_rows += 1 #Increment number of rows.
        row_entries = []
        for column in range(0, self.max_columns): #Loop for as many times as they're columns in table.
            entry = tk.Entry(self, font=(assets.fonts['title'], 10), fg=colours['darkgreen'], bg=colours['lightgreen'], borderwidth=1) #Create tkinter entry object.
            row_entries.append(entry)
            entry.grid(row=self.max_rows,column=column)
        self.entries.append(row_entries)

    def parseTable(self): #Get all the entries of the table and return the strings as a 2d array.
        table = [] #Initialize local variable.
        for row in range(0, self.max_rows): #Iterate for as many times as they're rows in table.
            row_entries = []
            for column in range(0, 4):
                row_entries.append(self.entries[row][column].get()) #Record what is current in the table cell.
            table.append(row_entries)
        return table

    def clearTable(self):
        for row in self.entries:
            for entry in row:
                entry.grid_forget() #Remove entry from wiget.
                entry.destroy() #Destroy individual entry widget.

        #Reset variables
        self.entries = [] 
        self.maxrows = 0

class Graph(tk.Frame): #Graph widget
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.fig = Figure(figsize=(6,4), dpi=100, facecolor=colours['lightgreen'], edgecolor=colours['darkgreen'], linewidth=10) #Configure graph window's colors, size, etc.
        self.fig.suptitle('Income v. Expense', fontsize=10)
        self.ax = self.fig.add_subplot(1,1,1) #Configure subplot grid as '1x1 grid, first subplot.
        self.canvas = None #Initialize canvas.

    def plot(self):
        self.clear() #Clear graph.
        table = self.parent.table.parseTable() #Get all the data in the table.
        labels = ('Income', 'Expense') #Set the labels of the graph.
        sizes = [0,0] #Initialize pie graph size.
        income = 0 #Initialize income percentage as 0.
        expense = 0 #Initialize expense percentage as 0.
        total = 0 #Initialize total amount as 0.

        for row in table[1:]: #Iterate through every row except the first.
            try:
                if row[0].replace(' ','') == labels[0]:
                    income += float(row[2])
                elif row[0].replace(' ','') == labels[1]:
                    expense += float(row[2])
            except:
                #print('Note: row {0} has an invalid amount entered. Please fix immediately'.format(table.index(row) + 1))
                pass

        total = income + expense #Calculate total amount.

        if total != 0:
            income = int(round(income/total * 100))  #Calculate approximate percentage.
            expense = int(100 - income)
            sizes = [income, expense]
            self.ax.pie(sizes)
            self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            self.ax.axis('equal')
            self.draw()

    def clear(self): #Remove any preexisting graphs.
        self.ax.clear()
        if self.canvas != None:
            self.canvas._tkcanvas.destroy()
            self.canvas = None

    def draw(self):
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class StatsPage(tk.Frame): #Stats widget.
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)
        self.stat_names = []
        self.stat_amounts = []

    def calculateStats(self):
        table = self.parent.table.parseTable()

        #Initialize stats.
        self.total_income = 0
        self.total_expense = 0

        self.income_list = []
        self.expense_list = []

        self.average_income = 0
        self.average_expense = 0

        self.median_income = 0
        self.median_expense = 0

        self.net_profit = 0

        self.h_income = 0 #Initialize highest income amount.
        self.h_income_name = None 
        self.h_income_desc = None
        self.h_expense = 0 #Initialize highest expense amount.
        self.h_expense_name = None 
        self.h_expense_desc = None

        self.l_income = 0 #Initialize lowest income amount.
        self.l_income_name = None 
        self.l_income_desc = None
        self.l_expense = 0 #Initialize highest income amount.
        self.l_expense_name = None
        self.l_income_desc = None

        self.stat_names = []
        self.stat_amounts = []

        labels = ('Income', 'Expense')

        first_income = True
        first_expense = True

        for row in table[1:]: #Iterate through table, exclude first row.
            try:
                amount = float(row[2])
                if row[0].replace(' ','') == labels[0]:

                    self.total_income += amount
                    self.income_list.append(amount)

                    if first_income: #If the first income entry in table, set it to the lowest by default.
                        self.l_income = amount
                        self.l_income_desc = row[3]
                        first_income = False

                    if amount > self.h_income: #Check if amount is larger than the record holder.
                        self.h_income = amount
                        self.h_income_name = row[1]
                        self.h_income_desc = row[3]

                    if amount < self.h_income: #Check if maount is less than the record holder
                        self.l_income = amount
                        self.l_income_name = row[1]
                        self.l_income_desc = row[3]

                elif row[0].replace(' ','') == labels[1]:
                    self.total_expense += amount
                    self.expense_list.append(amount)

                    if first_expense: #If the first expense entry in table, set it to the lowest by default.
                        self.l_expense = amount
                        self.l_expense_desc = row[3]
                        first_expense = False

                    if amount > self.h_expense: #Check if amount is larger than the record holder.
                        self.h_expense = amount
                        self.h_expense_name = row[1]
                        self.h_expense_desc = row[3]

                    if amount < self.h_expense: #Check if maount is less than the record holder
                        self.l_expense = amount
                        self.l_expense_name = row[1]
                        self.l_expense_desc = row[3]
            except:
                print('Note: row {0} has an invalid amount entered. Please fix immediately'.format(table.index(row) + 1))

        self.net_profit = self.total_income - self.total_expense

        if len(self.income_list) != 0:
            self.average_income = round(self.total_income / len(self.income_list))
        else:
            self.average_income = 0

        if len(self.expense_list) != 0:
            self.average_expense = round(self.total_expense / len(self.expense_list))
        else:
            self.average_expense = 0

        if len(self.income_list) > 1:
            middle = int(len(sorted(self.income_list))/2) - 1
        elif len(self.income_list) <= 1:
            if len(self.income_list) < 1:
                self.income_list = ['None']
            middle = 0

        self.median_income = self.income_list[middle]

        if len(self.expense_list) > 1:
            middle = int(len(sorted(self.expense_list))/2) - 1
        elif len(self.expense_list) <= 1:
            if len(self.expense_list) < 1:
                self.expense_list = ['None']
            middle = 0

        self.median_expense = self.expense_list[middle]

        self.stats = {       
            'Total Income':self.total_income,
            'Total Expense':self.total_expense,
            'Average Income':self.average_income,
            'Average Expense':self.average_expense,
            'Median Income':self.median_income,
            'Median Expense':self.median_expense,
            'Net Profit':self.net_profit,
            'Highest Income Amount':self.h_income,
            'Highest Income Name':self.h_income_name, 
            'Highest Income Description':self.h_income_desc,
            'Highest Expense Amount':self.h_expense,
            'Highest Expense Name':self.h_expense_name, 
            'Highest Expense Description':self.h_expense_desc,
            'Lowest Income Amount':self.l_income,
            'Lowest Income Name':self.l_income_name, 
            'Lowest Income Description':self.l_income_desc,
            'Lowest Expense Amount':self.l_expense,
            'Lowest Expense Name':self.l_expense_name,
            'Lowest Expense Description':self.l_income_desc}

    def display(self):
        self.calculateStats()
        self.clear()
        row = 0
        for stat in self.stats:
            name = tk.Label(self, text=stat + ':', font=(assets.fonts['title'],11), bg=self.parent.bg, fg=colours['darkgreen'])
            self.stat_names.append(name)
            name.grid(row=row, column=0, sticky='E')

            amount = tk.Label(self, text=self.stats[stat], font=(assets.fonts['title'],11), bg=self.parent.bg, fg=colours['darkgreen'])
            self.stat_amounts.append(name)
            amount.grid(row=row, column=1, sticky='W')

            row += 1


    def clear(self):
        for label in self.stat_names:
            label.grid_forget()

        for label in self.stat_amounts:
            label.grid_forget()

        self.stat_names = []
        self.stat_amounts = []

class MainWin(tk.Tk): #Inherit the class tk.Tk;

    def __init__(self): #Initialize
        tk.Tk.__init__(self) #Run initialization of tk.Tk; create window.
        self.height = cfg.win_height
        self.width = cfg.win_width
        self.size = cfg.win_size
        self.toolbox = [] #Initialize toolbox as an empty list.
        self.file = None #Initialize file name.
        self.overrideredirect(True) #Allows complete customization of how the window is handled.
        self.title(cfg.app_name) #Set the name of window.
        self.geometry(cfg.win_size) #Set size of window.
        self.config(bg=colours['silver'])
        self.createWidgets() #Create widgets
        #self.iconbitmap(assets.ui['icon']) #This asset doesn't exist. IIRC I couldn't get this working.

    def createWidgets(self): #Create all widgets.
        self.createTitleBar()
        self.createMenu()
        self.createWorkspace()

    def createTitleBar(self):
        self.titlebar= TitleBar(self)
        self.titlebar.grid(row=0,column=1, sticky='NE') #Configure titlebar location.
        #Set the binding of the titlebar so that clicking it allows the window to be moved.
        self.titlebar.bind('<ButtonPress-1>', self.startMove)
        self.titlebar.bind('<ButtonRelease-1>', self.stop)
        self.titlebar.bind('<B1-Motion>', self.onMotion)

    def createMenu(self):
        self.menubar = Menu(self)
        self.menubar.grid(row=0,column=0)

    def toggleToolBox(self, state, *args): #Open/Close toolbox.
        if self.file != None: #Only allow toggling if a file is opened.
            if state == True: #Check if already open.
                self.toolbox.append(ToolBox(self)) #Create toolbox window
                self.menubar.waffle.config(command=lambda:self.toggleToolBox(False)) #Set the waffle to close on the next click.
            elif state == False: #Check if it's not open.
                for toolbox in self.toolbox: #Iterate through toolbox list (there should only be one, but just in case).
                    toolbox.close() #Close toolbox.
                    self.toolbox = [] #Reset toolbox list.
                self.menubar.waffle.config(command=lambda:self.toggleToolBox(True)) #Set the waffle to open on the next click.

    def createWorkspace(self): #Create workspace widget.
        self.workspace = Workspace(self)
        self.workspace.grid(row=1, columnspan=2,sticky='S') #Add workspace to gui.
        self.grid_propagate(False) #Prevent the workspace from auto-resizing to fit widgets.

    def openEntryForm(self): #Open table entry window (for adding another row).
        #Get the position of the table entry button.
        offset_x = self.workspace.entrybutton.winfo_rootx()
        offset_y = self.workspace.entrybutton.winfo_rooty()
        self.tableentry = TableEntryBox(self, offset_x=offset_x - 350,offset_y=offset_y) #Open table entry box for row addition.

    def openHelpForm(self): #Open help window.
        helpmenu = HelpMenu(offset_x=self.winfo_rootx() + 350,offset_y=self.winfo_rooty()-50)

    def startMove(self, event): #Initiate window movement.
        self.toggleToolBox(False) #Close the toolbox.
        #Get location of the event (mouse).
        self.x = event.x
        self.y = event.y

    def stop(self, event): #Ceaase window movement.
        self.x = None
        self.y = None

    def onMotion(self, event):
        #Calculate difference between old location to new location.
        mov_x = event.x - self.x 
        mov_y = event.y - self.y
        x = self.winfo_x() + mov_x
        y = self.winfo_y() + mov_y
        self.geometry('+{0}+{1}'.format(x,y)) #Set the location to new location (move)

    def new(self): #Creates new file.
        self.message = CreateBox(self, offset_x=self.winfo_rootx() + 350,offset_y=self.winfo_rooty() + 100)

    def open(self, open_explorer=True): #Opens file.
        if open_explorer:
            file = filedialog.askopenfilename(initialdir=cfg.main_dir,title='Select File', filetypes=(("Text Files","*.txt"),("All Files","*.*"))) #Open windows explorer.
            if file == '' and self.file != None: #Check if the user exists the file explorer while a file is already open.
                self.file = self.file #Keep the file the same.
            else:
                self.file = file #Update file.

        banned_chars = ['\\', '/', ':', '*', '?', '<', '>', '|'] #Characters that cannot be used in file names.
        for char in banned_chars: #Iterate through every banned character.
            if char in self.file: #Check if character is in string.
                self.file.replace(char,'') #Remove from string.

        if self.file.replace(' ','').replace('\n','') != '': #Check if filename is not just empty spaces.
            self.workspace.table.clearTable()
            self.workspace.table.populateTable(self.file)
            self.workspace.displayTable()
        else:
            self.file = None


    def save(self): #Save file.
        file = filedialog.asksaveasfilename(initialdir=cfg.main_dir,title='Select File', filetypes=(("Text Files","*.txt"),("All Files","*.*")))
        display_message = True #Initialize message box flag.
        if file == '' and self.file != None: #Check if the user exits the file explorer while a file is already open.
            self.file = self.file #Keep the file the same.
            display_message = False
        else:
            self.file = file #Update file.

        if self.file.replace(' ','').replace('\n','') != '':
            with open('{0}'.format(self.file), 'w') as f: #Open/Create file.
                table = self.workspace.table.parseTable() #Parse table.
                for row in range(0, len(table)):
                    for column in range(0,4):
                        if column == 3: #Check if last category.
                            end_char = '\n' #Add newline.
                        else: #Else; assume not the last category.
                            end_char = ',' #Add comma separator.

                        if table[row][column].replace(' ','').replace('\n','') == '': #Check if cell is just a empty string.
                            string = 'None' #Replace with none.
                        else:
                            string = table[row][column]

                        f.write(string + end_char) #Write category.

            self.update()
            #Calculate window position.
            offset_x = self.winfo_rootx()
            offset_y = self.winfo_rooty()
            if display_message: #Check if message should be displayed.
                self.message = MessageBox(message='File saved! It is located in the data folder.', offset_x=offset_x+int(self.winfo_width()/2.25), offset_y=offset_y+int(self.winfo_height()/3), height=60) #Message of completion.
        else:
            self.file = None #Reset the file name.
