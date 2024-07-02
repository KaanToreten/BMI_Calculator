from tkinter import *
import math


wn = Tk()
wn.title("BMI Calculator")
wn.minsize(width=200, height=250)

def Button_cliked():
    global BMI
    weight = my_entry1.get()
    height = my_entry2.get()

    if weight == "" or height == "":
       my_label_result.config(text="Enter both weight and height!")
    else:
        try:
            BMI = float(weight) / pow(float(height)/100, 2)
            result_string = write_calucalate(BMI)
            my_label_result.config(text=result_string)
        except:
            my_label_result.config(text="Enter a valid number!")



my_label1 = Label(text="Enter Your weight (kg)")
my_label1.pack()

my_entry1 = Entry(width=20)
my_entry1.pack()

my_label2 = Label(text="Enter Your Height(cm)")
my_label2.pack()

my_entry2 = Entry(width=20)
my_entry2.pack()

my_button = Button(text="Calculate", command=Button_cliked)
my_button.config(padx=10, pady=10)
my_button.pack()

my_label_result = Label()
my_label_result.pack()
def write_calucalate(BMI):
    result_string = f"Your BMI is: {round(BMI,2)}. You are "
    if BMI >= 30:
        result_string += "obese"
    elif 30 > BMI >= 25:
        result_string += "overweight"
    elif 25 > BMI >= 18.5:
        result_string += "normal"
    else:
        result_string += "thin"
    return result_string

wn.mainloop()