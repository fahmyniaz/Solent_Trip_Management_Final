import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

def load_data():
    with open('json/tripleg.json') as f:
        return json.load(f)

# Save the file with new data
def save_data(json_data):
    with open('json/tripleg.json', 'w') as f:
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
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['startlocation'])
    e3.insert(0,select['destination'])
    e4.insert(0,select['transportprovider'])
    e5.insert(0,select['transportmode'])
    e6.insert(0, select['pointofinterest'])
    e7.insert(0, select['transferpoint'])

def Add():
    id = e1.get()
    startlocation = e2.get()
    destination = e3.get()
    transportprovider = e4.get()
    transportmode = e5.get()
    pointofinterest = e6.get()
    transferpoint = e7.get()

    create_one_item_in_json(
            {"id": json.dumps(id), "startlocation": json.dumps(startlocation),
             "destination": json.dumps(destination), "transportprovider": json.dumps(transportprovider), "transportmode": json.dumps(transportmode)
             , "pointofinterest": json.dumps(pointofinterest), "transferpoint": json.dumps(transferpoint)})
    messagebox.showinfo("information", "Trip Leg details saved successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e1.focus_set()


def update():
    id = e1.get()
    startlocation = e2.get()
    destination = e3.get()
    transportprovider = e4.get()
    transportmode = e4.get()
    pointofinterest = e6.get()
    transferpoint = e7.get()

    update_one_item_in_json(0,
                            {"id": json.dumps(id), "startlocation": json.dumps(startlocation),
                             "destination": json.dumps(destination), "transportprovider": json.dumps(transportprovider),
                             "transportmode": json.dumps(transportmode)
                                , "pointofinterest": json.dumps(pointofinterest),
                             "transferpoint": json.dumps(transferpoint)})

    messagebox.showinfo("information", "Trip Leg details Updated successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e1.focus_set()

def delete():
    empId = e1.get()
    delete_one_item_from_json(0)
    messagebox.showinfo("information", "Trip Leg Details Deleted successfully...")

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e1.focus_set()

def show():

        records = load_data()
        print(records)

        for x in records:
            listBox.insert("", "end", values=(x['id'],x['startlocation'], x['destination'],x['transportprovider'],x['transportmode'],x['pointofinterest'],x['transferpoint']))


root = Tk()
root.geometry("820x700")
root.configure(background='#fbe47c')
global e1
global e2
global e3
global e4
global e5
global e6
global e7


tk.Label(root, text="Welcome to", fg="#2c5c2b",bg="#fbe47c", font=(None, 24)).place(x=360, y=15)
tk.Label(root, text="Trip Leg Management", fg="#2c5c2b",bg="#fbe47c", font=(None, 30)).place(x=250, y=55)

tk.Label(root, text="ID",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=110)
Label(root, text="Start Location",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=140)
Label(root, text="Destination",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=170)
Label(root, text="Transport Provider",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=200)
Label(root, text="Mode of Transport",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=230)
Label(root, text="Point of Interest",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=260)
Label(root, text="Transfer Point",bg="#fbe47c", font=(None, 10, 'bold')).place(x=270, y=290)
Label(root, text="Please close this window to open the next window, Thank you...",fg="red", bg="#fbe47c",font=(None, 10, 'bold')).place(x=180, y=630)

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

Button(root, text="Add",command = Add,height=3, width= 13,fg="green",font=(None, 10, 'bold')).place(x=210, y=330)
Button(root, text="Update",command = update,height=3, width= 13,fg="blue",font=(None, 10, 'bold')).place(x=380, y=330)
Button(root, text="Delete",command = delete,height=3, width= 13,fg="red",font=(None, 10, 'bold')).place(x=540, y=330)

cols = ('id', 'startlocation', 'destination','transportprovider','transportmode')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=1)
    listBox.place(x=10, y=400)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
# Load the File