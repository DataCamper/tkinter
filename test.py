from tkinter import *


root = Tk()
root.title("Form")


# Necessary Functions

def show_info():
	name_show = Label(root, text="Hi dear " + fname.get() + " " + lname.get())
	Address_show = Label(root, text="You live in " + Address.get() + " and the zip code is " + ZipCode.get())
	DOB_show = Label(root, text="You were born in " + DOB.get())

	name_show.grid(row=6, column=0, columnspan=2)
	Address_show.grid(row=7, column=0, columnspan=2)
	DOB_show.grid(row=8, column=0, columnspan=2)


# Creating the forms

fname = Entry(root, width=30)
lname = Entry(root, width=30)
Address = Entry(root, width=30)
DOB = Entry(root, width=30)
ZipCode = Entry(root, width=30)


# Creatinh labels for forms

fname_label = Label(root, text="First Name:")
lname_label = Label(root, text="Last Name:")
Address_label = Label(root, text="Address:")
DOB_label = Label(root, text="Date of Birth:")
ZipCode_label = Label(root, text="Zip/Postal Code:")


# Placing the Labels and Forms

fname_label.grid(row=0, column=0)
fname.grid(row=0, column=1)

lname_label.grid(row=1, column=0)
lname.grid(row=1, column=1)

Address_label.grid(row=2, column=0)
Address.grid(row=2, column=1)

DOB_label.grid(row=3, column=0)
DOB.grid(row=3, column=1)

ZipCode_label.grid(row=4, column=0)
ZipCode.grid(row=4, column=1)


# Adding a Button

Btn1 = Button(root, text="Show", command=show_info, padx=10, pady=10)
Btn1.grid(row=5, column=0, columnspan=2)




root.mainloop()
