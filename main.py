import csv
from tkinter import *

FONT = ("Courier", 15, "normal")
BLACK = "#393e46"
WHITE = "#e8e8e8"
RED = "#f05454"
GREY = "#30475e"


def convert_file():
    new_path = new_path_entry.get()
    new_name = new_name_entry.get()
    origin_path = origin_path_entry.get()
    origin_name = origin_name_entry.get()

    words = open("./" + origin_path + "/" + origin_name + ".txt", mode="r")
    my_list = [line.split() for line in words]

    with open("./" + new_path + "/" + new_name + ".csv", mode="w") as f:
        writer = csv.writer(f)
        writer.writerows(my_list)


wd = Tk()
wd.title("txt to csv")
wd.config(padx=20, pady=20, bg=BLACK)
wd.minsize(width=400, height=170)

heading = Label(text="Enter Info:", fg=WHITE, bg=BLACK, font=FONT)
heading.grid(column=0, row=0, columnspan=1)

origin_path_entry = Entry(width=40)
origin_path_entry.grid(column=0, row=1, columnspan=1)
origin_path_entry.insert(0, "origin file path")

origin_name_entry = Entry(width=40)
origin_name_entry.grid(column=0, row=2, columnspan=1)
origin_name_entry.insert(0, "origin file name")

new_name_entry = Entry(width=40)
new_name_entry.grid(column=0, row=3, columnspan=1)
new_name_entry.insert(0, "new name")

new_path_entry = Entry(width=40)
new_path_entry.grid(column=0, row=4, columnspan=1)
new_path_entry.insert(0, "new path")

convert_btn = Button(width=20, text="Make CSV", command=convert_file, fg=WHITE, bg=GREY, activebackground=RED, activeforeground=BLACK)
convert_btn.grid(column=0, row=5, columnspan=1)

wd.mainloop()
