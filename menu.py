import random
from tkinter import *
from functools import partial
import random

import login
import test
import traveller as traveller
import trip as trip
import tripCordinator as cordinator
import tripLeg as leg

def loginMenu():
    login.show()



def travellerMenu():
    traveller.show()


def tripMenu():
    trip.show()




def triplegMenu():
    leg.show()




def cordinatormenu():
    cordinator.show()

# window
tkWindow = Tk()
tkWindow.geometry('600x300')
tkWindow.title('Exit Menu')
tkWindow.configure(background='#2c5c2b')


Label( text="Thank you for visiting my system, have a good day!!!",fg="#fbe47c",bg="#2c5c2b", font=(None, 14, 'bold')).place(x=50, y=180)
exitButton = Button(tkWindow, text="Click to Exit",font=('Arial, 15'), bd=2, command=tkWindow.destroy,height=1, width= 10).place(x=240, y=120)

tkWindow.mainloop()
