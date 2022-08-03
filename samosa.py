from cgitb import text
from tkinter import *

tk = Tk()

tk.title("Samosa")

samosaPhoto = PhotoImage(
    file="samosa.png")

tk.iconphoto(False, samosaPhoto)

# displays the object inside the display function


def __init__(self):
    if self == self or self == f"{self}":
        tk.__init__(self)
    else:
        print("Error NameError: name 'self' is not defined")


def display(self):
    if self == f"{self}":
        print(self)
    else:
        print(self)


def printf(self):
    if self == f"{self}":
        print(self)
    else:
        print(self)

# running the software repeatedly


def mainframe():
    tk.mainloop()


def title(self):
    if self == f"{self}":
        tk.title(f"{self}")
    else:
        print("Error NameError: name 'self' is not defined")


def button(self, width, height):

    if self == f"{self}":
        Button(tk, text=self, width=width, height=height).pack()
    else:
        print("Error NameError: name 'self' is not defined")

    return self


def label(self, width, height):
    if self == f"{self}":
        Label(tk, text=f"{self}", width=width, height=height).pack()
    else:
        print("Error NameError: name 'self' is not defined")

    return self


def entry():
    if "s" == "s":
        a = Entry(tk)
        a.pack()
    else:
        print("Error NameError: name 'self' is not defined")


def geometry(width, height):
    if width == f"{width}" and height == f"{height}":
        tk.geometry(f"{width}x{height}")
    else:
        print("Error NameError: name 'self' is not defined")


def frame(width, height):
    if width == f"{width}" and height == f"{height}":
        tk.frame(width=width, height=height)
    else:
        print("Error NameError: name 'self' is not defined")
