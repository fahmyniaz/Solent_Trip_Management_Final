import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *


window=Tk()
window.title("Calculator")
window.geometry("800x600")
window.configure(background='#fbe47c')


label1 = Label(window, text="Welcome to", fg="#2c5c2b",bg="#fbe47c",  font=(None, 24))
label1.grid(row=0, column=1, padx=5, pady=10)

label1 =Label(window, text="Trip Management Billing Section", fg="#2c5c2b",bg="#fbe47c",  font=(None, 24))
label1.grid(row=1, column=1, padx=5, pady=10)

label1=Label(window, text='ID',bg="#fbe47c", fg='blue', font=('Arial', 14))
label1.grid(row=4, column=0, padx=5, pady=10)

label1=Label(window, text='Total Amount:',bg="#fbe47c", fg='blue', font=('Arial', 14))
label1.grid(row=5, column=0, padx=5, pady=10)

label1=Label(window, text='No of Installment:',bg="#fbe47c", fg='blue', font=('Arial', 14))
label1.grid(row=6, column=0, padx=5, pady=10)

label1=Label(window, text='Amount per installment:', bg="#fbe47c",fg='blue', font=('Arial', 14))
label1.grid(row=7, column=0, padx=5, pady=10)

label1=Label(window, text='Amount Paid:', fg='blue',bg="#fbe47c", font=('Arial', 14))
label1.grid(row=8, column=0, padx=5, pady=10)

label1=Label(window, text='Total Payable:', fg='blue',bg="#fbe47c", font=('Arial', 14))
label1.grid(row=9, column=0, padx=5, pady=10)

total=IntVar()
installment=IntVar()
paid=IntVar()

textbox1=Entry(window, fg='blue', font=('Arial', 14))
textbox1.grid(row=4, column=1)

textbox1=Entry(window, textvariable=total, fg='blue', font=('Arial', 14))
textbox1.grid(row=5, column=1)

textbox1=Entry(window, textvariable=installment, fg='blue', font=('Arial', 14))
textbox1.grid(row=6, column=1)

emptylabel=Label(window, fg='green', font=('Arial', 14))
emptylabel.grid(row=7, column=1, padx=5, pady=10)


textbox1=Entry(window, textvariable=paid, fg='blue', font=('Arial', 14))
textbox1.grid(row=8, column=1)

emptylabel2=Label(window, fg='green', font=('Arial', 14))
emptylabel2.grid(row=9, column=1, padx=5, pady=10)


def totalPayable():  #event/command handling logic
    totals=total.get()-paid.get()
    emptylabel2.config(text='Your Payable amount is:' + str(totals))


def perInstallment():  # event/command handling logic
        instalments = total.get() / installment.get()
        emptylabel.config(text='Your per installment amount is:' + str(instalments))


button1 = Button(window, command=totalPayable, text='Total Payable', fg='blue', font=('Arial', 14))
button1.grid(row=11, column=1, sticky=W)

button1 = Button(window, command=perInstallment, text='Installment calculator', fg='blue', font=('Arial', 14))
button1.grid(row=12, column=1)


window.mainloop()
# Load the File