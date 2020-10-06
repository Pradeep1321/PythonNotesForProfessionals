"""
Chapter 62: tkinter
Released in Tkinter is Python's most popular GUI (Graphical User Interface) library

Section 62.1: Geometry Managers
Tkinter has three mechanisms for geometry management: place, pack, and grid.

The place manager uses absolute pixel coordinates.
The pack manager places widgets into one of 4 sides. New widgets are placed next to existing widgets.
The grid manager places widgets into a grid similar to a dynamically resizing spreadsheet

Place
The most common keyword arguments for widget.place are as follows:
x, the absolute x-coordinate of the widget
y, the absolute y-coordinate of the widget
height, the absolute height of the widget
width, the absolute width of the widget

Pack
widget.pack can take the following keyword arguments:
expand, whether or not to fill space left by parent
fill, whether to expand to fill all space (NONE (default), X, Y, or BOTH)
side, the side to pack against (TOP (default), BOTTOM, LEFT, or RIGHT)

Grid
The most commonly used keyword arguments of widget.grid are as follows:
row, the row of the widget (default smallest unoccupied)
rowspan, the number of columns a widget spans (default 1)
column, the column of the widget (default 0)
columnspan, the number of columns a widget spans (default 1)
sticky, where to place widget if the grid cell is larger than it (combination of N,NE,E,SE,S,SW,W,NW)

The rows and columns are zero indexed. Rows increase going down, and columns increase going right.

Never mix pack and grid within the same frame! Doing so will lead to application deadlock!


Section 62.2: A minimal tkinter Application
tkinter is a GUI toolkit that provides a wrapper around the Tk/Tcl GUI library and is included with Python.

Note: In Python 2, the capitalization may be slightly different, see Remarks section below.

Chapter 63: pyautogui module
pyautogui is a module used to control mouse and keyboard. This module is basically used to automate mouse click
and keyboard press tasks. For the mouse, the coordinates of the screen (0,0) start from the top-left corner. If you
are out of control, then quickly move the mouse cursor to top-left, it will take the control of mouse and keyboard
from the Python and give it back to you.

Section 63.1: Mouse Functions
These are some of useful mouse functions to control the mouse.
size()                          #gave you the size of the screen
position()                      #return current position of mouse
moveTo(200,0,duration=1.5)      #move the cursor to (200,0) position with 1.5 second delay
moveRel()                       #move the cursor relative to your current position.
click(337,46)                   #it will click on the position mention there
dragRel()                         #it will drag the mouse relative to position
pyautogui.displayMousePosition()  #gave you the current mouse position but should be done on terminal.

Section 63.2: Keyboard Functions
typewrite('')                                 #this will type the string on the screen where current window has focused.
typewrite(['a','b','left','left','X','Y'])
pyautogui.KEYBOARD_KEYS                       #get the list of all the keyboard_keys.
pyautogui.hotkey('ctrl','o')                  #for the combination of keys to enter.

Section 63.3: Screenshot And Image Recognition
.screenshot('c:\\path')                 #get the screenshot.
.locateOnScreen('c:\\path')             #search that image on screen and get the coordinates for you.
locateCenterOnScreen('c:\\path')        #get the coordinate for the image on screen.



"""
from tkinter import *


#  Place
class PlaceExample(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        top_text=Label(master,text="This is on top at the origin")
        #top_text.pack()
        top_text.place(x=0,y=0,height=50,width=200)
        bottom_right_text=Label(master,text="This is at position 200,400")
        #top_text.pack()
        bottom_right_text.place(x=200,y=400,height=50,width=200)


class GridExample(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        top_text=Label(self,text="This text appears on top left")
        top_text.grid() # Default position 0, 0
        bottom_text=Label(self,text="This text appears on bottom left")
        bottom_text.grid() # Default position 1, 0
        right_text=Label(self,text="This text appears on the right and spans both rows",
        wraplength=100)
        # Position is 0,1
        # Rowspan means actual position is [0-1],1
        right_text.grid(row=10,column=10,rowspan=20)


'''
# Spawn Window
if __name__=="__main__":
    root=Tk()
    #place_frame=PlaceExample(root)
    #place_frame.mainloop()
    grid_frame = GridExample(root)
    grid_frame.mainloop()
'''
#Section 62.2: A minimal tkinter Application
print("---------Section 62.2: A minimal tkinter Application------")

# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(Frame):
    def __init__(self, master):
        # Call superclass constructor
        Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create text box with "Hello World" text
        hello = Label(self, text="Hello World! This label can hold strings!")
        # Place text box into frame
        hello.grid(row=0, column=0)
# Spawn window
if __name__ == "__main__":
    # Create main window object
    root = Tk()
    # Set title of window
    root.title("Hello World!")
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root)
    # Start GUI
    hello_frame.mainloop()