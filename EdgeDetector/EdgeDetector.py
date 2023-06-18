from tkinter.tix import FileEntry
import PIL.Image as Image
import PIL.ImageTk  as ImageTk
from Filters import Filters
import tkinter 



def FilterButton(chosenfilter,image):
    image=Filters.ApplyFilter(chosenfilter,image)
    image=Image.fromarray(image)
    tkimg=ImageTk.PhotoImage(image)
    ImageLabel.configure(image=tkimg)
    ImageLabel.image=tkimg

def LoadImage(path):
    global image
    global WidthEntryBox
    global HeightEntryBox
    image=Image.open(path)  

    if((str.isdigit(WidthEntryBox.get())  and str.isdigit(HeightEntryBox.get())) and 
       (int(WidthEntryBox.get()) in range(0,MaxWidth) and int(HeightEntryBox.get()) in range(0,MaxHeight))):
        image=image.resize([int(WidthEntryBox.get()),int(HeightEntryBox.get())])
    else:
        image=image.resize([MaxWidth,MaxHeight])
    

    tkimg=ImageTk.PhotoImage(image)
    ImageLabel.configure(image=tkimg)
    ImageLabel.image=tkimg
    

    
    

##create root window
RootWindow=tkinter.Tk()

RootWindow.title("Filtering Images")

## split window into two frames 
## image frame and button frame
ImageFrame=tkinter.LabelFrame(RootWindow,width=600,height=600)
ImageFrame.grid(row=0,column=0)

ButtonFrame=tkinter.LabelFrame(RootWindow,width=600,height=600)
ButtonFrame.grid(row=0,column=1)



## create input field to get file location
FileEntryLabel=tkinter.Label(ButtonFrame,text="File Path:")
FileEntryBox=tkinter.Entry(ButtonFrame)
FileEntryLabel.grid(row=0)
FileEntryBox.grid(row=1)

WidthLabel=tkinter.Label(ButtonFrame,text="Width:")
WidthEntryBox=tkinter.Entry(ButtonFrame)
WidthLabel.grid(row=2)
WidthEntryBox.grid(row=3)

HeightLabel=tkinter.Label(ButtonFrame,text="Height:")
HeightEntryBox=tkinter.Entry(ButtonFrame)
HeightLabel.grid(row=4)
HeightEntryBox.grid(row=5)

## Buttons

LoadButton=tkinter.Button(ButtonFrame,text="Load",command=lambda:LoadImage(FileEntryBox.get()))
LoadButton.grid(row=6)

VEdgesButton=tkinter.Button(ButtonFrame,text="Vertical Sobel",command=lambda:FilterButton(Filters.SobelVertical,image)) 
VEdgesButton.grid(row=7)

HEdgesButton=tkinter.Button(ButtonFrame,text="Horizontal Sobel",command=lambda:FilterButton(Filters.SobelHorizontal,image)) 
HEdgesButton.grid(row=8)

## constrains max height and width
MaxHeight=800
MaxWidth=1250


##loads the image
defaultfile=r"D:\Python\Convolutions\Images\minion.png"
ImageLabel=tkinter.Label(ImageFrame)
ImageLabel.pack()
LoadImage(defaultfile)




RootWindow.mainloop()
