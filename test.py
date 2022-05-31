import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

def load_data():
    with open('json/trip.json') as f:
        return json.load(f)

# Save the file with new data
def save_data(json_data):
    with open('json/trip.json', 'w') as f:
        json.dump(json_data, f, indent=8)

# Read an Item from file
def get_one_item_from_json(id):
    json_data = load_data()
    for x in json_data:
        if x['id'] == id:
            return x

# Create New Item and save it into file
def create_one_item_in_json(d):
    json_data = load_data()
    json_data.append(d)
    save_data(json_data)

# Delete One Item from Json
def delete_one_item_from_json(id):
    json_data = load_data()
    del json_data[id]
    save_data(json_data)

# Update One Item from JSON
def update_one_item_in_json(id, data):
    json_data = load_data()
    json_data[id] = data
    save_data(json_data)


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['name'])
    e3.insert(0,select['startdate'])
    e4.insert(0,select['nooftravellers'])
    e5.insert(0, select['nooftriplegs'])


def Add():
    id = e1.get()
    name = e2.get()
    startdate = e3.get()
    nooftravellers = e4.get()
    nooftriplegs = e5.get()



    create_one_item_in_json(
            {"id": json.dumps(id), "name": json.dumps(name),
             "startdate": json.dumps(startdate), "nooftravellers": json.dumps(nooftravellers), "nooftriplegs": json.dumps(nooftriplegs)
             , "contact": json.dumps(contact), "tripcordinator": json.dumps(tripcordinator), "noofstaffs": json.dumps(noofstaffs), "tripmode": json.dumps(tripmode)
                , "total": json.dumps(total)
                , "noofinstallment": json.dumps(noofinstallment), "perinstallmeht": json.dumps(perinstallmeht),
             "paid": json.dumps(paid), "payable": json.dumps(payable)
             })
    messagebox.showinfo("information", "Trip details saved successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e1.focus_set()


def update():
    id = e1.get()
    name = e2.get()
    startdate = e3.get()
    nooftravellers = e4.get()
    nooftriplegs = e5.get()
    contact = e6.get()
    tripcordinator = e7.get()
    noofstaffs = e8.get()
    tripmode = e9.get()
    total = e10.get()
    noofinstallment = e11.get()
    perinstallmeht = e12.get()
    paid = e13.get()
    payable = e14.get()

    update_one_item_in_json(0,
                            {"id": json.dumps(id), "name": json.dumps(name),
                             "startdate": json.dumps(startdate), "nooftravellers": json.dumps(nooftravellers),
                             "nooftriplegs": json.dumps(nooftriplegs)
                                , "contact": json.dumps(contact), "tripcordinator": json.dumps(tripcordinator),
                             "noofstaffs": json.dumps(noofstaffs), "tripmode": json.dumps(tripmode)
                                , "total": json.dumps(total)
                                , "noofinstallment": json.dumps(noofinstallment),
                             "perinstallmeht": json.dumps(perinstallmeht),
                             "paid": json.dumps(paid), "payable": json.dumps(payable)
                             })
    messagebox.showinfo("information", "Trip details Updated successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e1.focus_set()

def delete():
    empId = e1.get()
    delete_one_item_from_json(0)
    messagebox.showinfo("information", "Trip Details Deleted successfully...")

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e1.focus_set()

def show():

        records = load_data()
        print(records)

        for x in records:
            listBox.insert("", "end", values=(x['id'], x['name'], x['startdate'], x['nooftravellers'], x['nooftriplegs'], x['contact'], x['tripcordinator'], x['noofstaffs'],x['tripmode'], x['total'], x['noofinstallment'], x['perinstallmeht'], x['paid'],x['payable']))

window=Tk()
window.title("Calculator")
window.geometry('800x600')


label1 = Label(window, text="Welcome to", fg="#2c5c2b",bg="#fbe47c",  font=(None, 24))
label1.grid(row=0, column=1, padx=5, pady=10)

label1 =Label(window, text="Trip Management", fg="#2c5c2b",bg="#fbe47c",  font=(None, 30))
label1.grid(row=1, column=1, padx=5, pady=10)

label1=Label(window, text='Total Amount:', fg='blue', font=('Arial', 14))
label1.grid(row=4, column=0, padx=5, pady=10)

label1=Label(window, text='No of Installment:', fg='blue', font=('Arial', 14))
label1.grid(row=5, column=0, padx=5, pady=10)

label1=Label(window, text='Amount per installment:', fg='blue', font=('Arial', 14))
label1.grid(row=6, column=0, padx=5, pady=10)

label1=Label(window, text='Amount Paid:', fg='blue', font=('Arial', 14))
label1.grid(row=7, column=0, padx=5, pady=10)

label1=Label(window, text='Total Payable:', fg='blue', font=('Arial', 14))
label1.grid(row=8, column=0, padx=5, pady=10)

total=IntVar()
installment=IntVar()
paid=IntVar()

textbox1=Entry(window, textvariable=total, fg='blue', font=('Arial', 14))
textbox1.grid(row=4, column=1)

textbox1=Entry(window, textvariable=installment, fg='blue', font=('Arial', 14))
textbox1.grid(row=5, column=1)

emptylabel=Label(window, fg='green', font=('Arial', 14))
emptylabel.grid(row=6, column=1,sticky=W, pady=10)


textbox1=Entry(window, textvariable=paid, fg='blue', font=('Arial', 14))
textbox1.grid(row=7, column=1)

emptylabel2=Label(window, fg='green', font=('Arial', 14))
emptylabel2.grid(row=8, column=1,sticky=W, pady=10)


def totalPayable():  #event/command handling logic
    totals=total.get()-paid.get()
    emptylabel2.config(text='Your total is:' + str(totals))


def perInstallment():  # event/command handling logic
        instalments = total.get() / installment.get()
        emptylabel.config(text='Your per installment is:' + str(instalments))


button1 = Button(window, command=totalPayable, text='Total Payable', fg='blue', font=('Arial', 14))
button1.grid(row=9, column=1, sticky=W)

button2 = Button(window, command=perInstallment, text='Per Installment', fg='blue', font=('Arial', 14))
button2.grid(row=6, column=2, sticky=W)



window = Tk()
window.geometry("1010x690")
window.configure(background='#fbe47c')
global e1
global e2
global e3
global e4
global e5

cols = ('ID', 'Name', 'Start Date','No of Travellers','No of Trip Legs', 'Contact', 'Trip Cordinator','No of Support Staffs','Trip Mode')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=430)

show()
listBox.bind('<Double-Button-1>',GetValue)


window.mainloop()
# Load the File