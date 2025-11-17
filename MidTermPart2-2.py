import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


#Window setup
root = Tk()
root.title('CCSU App')
root.geometry('500x500')
root.resizable(0,0)
root.configure(bg='light blue')

#Make white in logo transparent and show it

img = Image.open ('logo.png')
#Pillow>=10 changed ANTIALIAS; this keeps it compatible
try:
    img = img.resize((100,100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100,100), Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()

newData = []
for item in data:
    # if pixel is white make it transparent; else keep it
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)


img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label (root, image=logo, bg='light blue')
logoLabel.place(x=1, y=1)


data = pd.read_csv("examfilehere.csv")

#Label used to display results
lb = Label(root, justify="left", bg="light blue", anchor= "w")
lb.place(x=130, y=150)

#Button 1: Calendar
def calendar():
    df = pd.DataFrame(data, columns=['CalendarDates'])
    selected_rows = df[~df['CalendarDates'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=100, y=140)

#Button 2: Buildings
def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=160, y=150)

#Button 3: Faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=200, y=150)

#Button 4: Business School
def school_of_business():
    programs = ("School of Business Departments",
                "-Accounting",
                "-Finance",
                "-Management & Organization",
                "-Marketing",
                "-Management Information Systems (MIS)",
                "-Business Analytics")
    lb.config(text="\n".join(programs))
    lb.place(x=100, y=270)

#Button 5: MIS Department
def mis_department():
     programs = ("MIS Department Core Courses",
                 '-Intro to MIS,'
                 '-Databases Management',
                 '-Systems Analysis & Design'
                 '-Business Analytics/Data Visualization',
                 '-Network and Information Security',
                 '-Project Management')
     lb.config(text="\n".join(programs))
     lb.place(x=90, y=270)

button1 = Button(root,text="Calendar", command=calendar, fg="white", bg="blue", highlightbackground="blue", padx=5, pady=5)
button1.place(x=30, y=110)

button2 = Button(root,text="Buildings", command=building, fg="white", bg="blue", highlightbackground="blue", padx=5, pady=5)
button2.place(x=170, y=110)

button3 = Button(root, text="Faculty", command=faculty, fg="white", bg="blue", highlightbackground="blue",padx=5, pady=5)
button3.place(x=330, y=110)

button4 = Button(root, text="School of Business", command= school_of_business, fg="white", bg="blue", highlightbackground="blue", padx=5, pady=5)
button4.place(x=30, y=200)

button5 = Button(root, text= "MIS Department", command=mis_department, fg="white", bg="blue", highlightbackground="blue", padx=5, pady=5)
button5.place(x=270, y=200)

mainloop()

