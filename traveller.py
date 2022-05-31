import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

def load_data():
    with open('json/traveller.json') as f:
        return json.load(f)

# Save the file with new data
def save_data(json_data):
    with open('json/traveller.json', 'w') as f:
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
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['name'])
    e3.insert(0,select['address'])
    e4.insert(0,select['dob'])
    e5.insert(0, select['email'])
    e6.insert(0, select['passportno'])
    e7.insert(0, select['nic'])
    e8.insert(0, select['contact'])


def Add():
    id = e1.get()
    name = e2.get()
    address = e3.get()
    dob = e4.get()
    email = e5.get()
    passportno = e6.get()
    nic = e7.get()
    contact = e8.get()

    create_one_item_in_json(
            {"id": json.dumps(id), "name": json.dumps(name),
             "address": json.dumps(address), "dob": json.dumps(dob), "email": json.dumps(email), "passportno": json.dumps(passportno),
             "nic": json.dumps(nic), "contact": json.dumps(contact)})
    messagebox.showinfo("information", "Travellers details Saved Successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e1.focus_set()


def update():
    id = e1.get()
    name = e2.get()
    address = e3.get()
    dob = e4.get()
    email = e5.get()
    passportno = e6.get()
    nic = e7.get()
    contact = e8.get()

    update_one_item_in_json(0,
            {"id": json.dumps(id), "name": json.dumps(name),
             "address": json.dumps(address), "dob": json.dumps(dob), "email": json.dumps(email), "passportno": json.dumps(passportno),
             "nic": json.dumps(nic), "contact": json.dumps(contact)})

    messagebox.showinfo("information", "Travellers details Updated Successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e1.focus_set()

def delete():
    empId = e1.get()
    delete_one_item_from_json(0)
    messagebox.showinfo("information", "Travellers details Deleted successfully...")

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e1.focus_set()

def show():

        records = load_data()
        print(records)

        for x in records:
            listBox.insert("", "end", values=(x['id'],x['name'], x['address'],x['dob'],x['email'],x['passportno'], x['nic'],x['contact']))


root = Tk()
root.geometry("820x860")
root.configure(background='#fbe47c')
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8

tk.Label(root, text="Welcome to", fg="#2c5c2b",bg="#fbe47c", font=(None, 24)).place(x=350, y=15)
tk.Label(root, text="Traveller Management", fg="#2c5c2b", bg="#fbe47c",font=(None, 30)).place(x=230, y=55)

tk.Label(root, text="ID", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=110)
Label(root, text="Name", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=140)
Label(root, text="Address", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=170)
Label(root, text="DOB (DD/MM/YYYY)", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=200)
Label(root, text="Email", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=230)
Label(root, text="Passport Number", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=260)
Label(root, text="NIC", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=290)
Label(root, text="Contact", bg="#fbe47c",font=(None, 10, 'bold')).place(x=270, y=320)
Label(root, text="Please close this window to open the next window, Thank you...",fg="red", bg="#fbe47c",font=(None, 10, 'bold')).place(x=180, y=670)

e1 = Entry(root, width=30)
e1.place(x=395, y=110)

e2 = Entry(root, width=30)
e2.place(x=395, y=140)

e3 = Entry(root, width=30)
e3.place(x=395, y=170)

e4 = Entry(root, width=30)
e4.place(x=395, y=200)

e5 = Entry(root, width=30)
e5.place(x=395, y=230)

e6 = Entry(root, width=30)
e6.place(x=395, y=260)

e7 = Entry(root, width=30)
e7.place(x=395, y=290)

e8 = Entry(root, width=30)
e8.place(x=395, y=320)



Button(root, text="Add",command = Add,height=3, width= 13,fg="green",font=(None, 10, 'bold')).place(x=220, y=360)
Button(root, text="update",command = update,height=3, width= 13,fg="blue",font=(None, 10, 'bold')).place(x=380, y=360)
Button(root, text="Delete",command = delete,height=3, width= 13,fg="red",font=(None, 10, 'bold')).place(x=540, y=360)

cols = ('id', 'name', 'address','dob','email', 'passportno', 'nic','contact')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=440)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
# Load the File