from tkinter import *
from tkinter.ttk import Button

window = Tk()
window.title("My first GUI Program")
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)

#Label

my_label = Label(text="I am a Label", font=("Arial",11,"bold"))
my_label_miles = Label(text="I am a Label", font=("Arial",11,"bold"))
my_label_kms = Label(text="I am a Label", font=("Arial",11,"bold"))
my_label_result = Label(text="I am a Label", font=("Arial",11,"bold"))
#my_label.pack()

my_label.config(text= "Is equal to:")
my_label.grid(column = 0, row = 1)

my_label_miles.config(text= "Miles")
my_label_miles.grid(column = 2, row = 0)

my_label_kms.config(text= "Kms.")
my_label_kms.grid(column = 2, row = 1)

my_label_result.config(text= "")
my_label_result.grid(column = 1, row = 1)
#Button
def button_clicked():
    miles = int(input.get())
    kilometers = miles*1.60934
    #new_text = input.get()
    my_label_result.config(text=kilometers)
    my_label_result.grid(column = 1, row = 1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row = 2)

# button2 = Button(text="Miles")
# button2.grid(column = 2, row = 0)

#Entry
input = Entry(width=10)
input.grid(column = 1, row = 0)


window.mainloop()