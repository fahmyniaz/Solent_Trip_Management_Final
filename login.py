import sys
from tkinter import *
import sys
from tkinter import messagebox


def command1(event):

        if entry1.get() == 'admin' and entry2.get() == 'password':
            messagebox.showinfo('login', 'Login Success')


        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root = Tk()
top = Toplevel()

root.geometry('800x250')
top.geometry('800x350')
top.title('LOGIN SCREEN')
top.configure(background='#e3e8cd')
root.configure(background='#dbc39c')

Label(root, text="Welcome to my system, Please click the below button to continue!!!", fg='#34334b',bg='#dbc39c',font=(None, 16, 'bold')).place(x=30, y=100)

exitButton = Button(root, text="Click to Exit", command=root.destroy,height=3, width= 13,font=( 18)).place(x=320, y=150)

label1 = Label(top, text='Solent Trip Management Login page', bg='#e3e8cd', fg='cyan4', font=('Arial, 20'))

lbl1 = Label(top, text='Username:', fg='cyan4', background='#e3e8cd',font=('Helvetica',17))
entry1 = Entry(top)
lbl2 = Label(top, text='Password:',fg='cyan4', background='#e3e8cd', font=('Helvetica',17))
entry2 = Entry(top, show="*")
button2 = Button(top, text='Login', bg='#e3e8cd', font=('Arial, 15'), bd=3, command=lambda:command2())

entry2.bind('<Return>', command1)

lbl3 = Label(top, text='UN - admin / PW - password',background='#e3e8cd', font=('Arial, 14'))

lbl4 = Label(top, text='Please make sure you enter the correct password to open the next window.', background='black', fg='red', font=('Arial, 14'))

label1.place(x=200, y=10)
lbl1.place(x=250, y=80)

entry1.place(x=380, y=90)
lbl2.place(x=250, y=140)
entry2.place(x=380, y=147)
button2.place(x=360, y=200)
lbl3.place(x=260, y=250)
lbl4.place(x=80, y=280)

root.withdraw()
root.mainloop()