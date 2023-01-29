# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter


win_width = 320
win_height = 200

mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.minsize(320, 200)
mainWindow['padx'] = 10
mainWindow['pady'] = 5

buttonRow = [['1', '2', '3', '*'],
             ['4', '5', '6', '-'],
             ['7', '8', '9', '+']]

last_row = ['0', ' = ', '', '/']

screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

center_x = int(screen_width/2 - win_width/2)
center_y = int(screen_height/2 - win_height/2)

mainWindow.geometry(f'{win_width}x{win_height}-{center_x}-{center_y}')

mainWindow.columnconfigure(0, weight=0)
mainWindow.columnconfigure(1, weight=0)
mainWindow.columnconfigure(2, weight=0)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=0)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=0)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=0)
mainWindow.rowconfigure(5, weight=0)

resultBox = tkinter.Entry(mainWindow)
resultBox.grid(row=0, column=0, sticky='we', columnspan=4)

clearButton = tkinter.Button(mainWindow, text='C', width=5)
clearButton.grid(row=1, column=0, sticky='w', )
# clearButton['padx'] = 15
# clearButton['pady'] = 5

clearAllButton = tkinter.Button(mainWindow, text='CE', width=5)
clearAllButton.grid(row=1, column=1, sticky='w', )
# clearAllButton['padx'] = 15
# clearAllButton['pady'] = 5

for row_index, row in enumerate(buttonRow):
    for cell_index, cell in enumerate(row):
        btns = tkinter.Button(mainWindow, text=cell, width=5)
        btns.grid(row=abs(row_index - 4), column=cell_index)

for btn_index, cell in enumerate(last_row):
    if btn_index == 1:
        btns = tkinter.Button(mainWindow, text=cell, width=12)
        btns.grid(row=5, column=btn_index, columnspan=2)
    elif cell == '':
        continue
    else:
        btns = tkinter.Button(mainWindow, text=cell, width=5)
        btns.grid(row=5, column=btn_index)


print(mainWindow.grid_size())

mainWindow.mainloop()


