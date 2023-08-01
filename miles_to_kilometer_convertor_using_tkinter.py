from tkinter import *
from tkinter import Label

window=Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400,height=300)
window.config(padx=40,pady=40)

def convertor():
    one_mile = 1.60934
    miles=miles_input.get()
    kilometer = round(float(miles) * one_mile)
    kilometer_result_label.config(text=kilometer)
#label
miles_input=Entry()
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles",font=("arial",20,"normal"))
miles_label.grid(column=2,row=0)

is_equal_to_label=Label(text=f"is equal to ",font=("arial",20,"normal"))
is_equal_to_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0",font=("arial",20,"normal"))
kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km",font=("arial",20,"normal"))
kilometer_label.grid(column=2,row=1)


#button
button=Button(text="Calculate",command=convertor)
button.grid(column=1,row=2)



window.mainloop()
