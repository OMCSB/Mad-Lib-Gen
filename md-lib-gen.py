from cgitb import text
from re import T
from tkinter import *
from click import command
import random


def gen_story_Night():
    En1 = En1_var.get()
    En2 = En2_var.get()
    En3 = En3_var.get()
    En4 = En4_var.get()
    En5 = En5_var.get()

    Fin_txt = "The Night demonstrates terribly cruel acts by the Nazis against the Jews, also known as The Holocaust. {} family is in Sighet. They are ordered to move in segregated places and are forced to board a train to {} with only a {} in their hand. Cruelty can be assessed from the fact that various people have already foreseen their deaths. For example, Madam Schachter starts screaming at the top of her voice and imagining that there is a {} above their heads. Moishe of Beadle also warns the people that they would be driven to their deaths, yet nobody believes him. {} later remembers that people often took him as a lunatic. {}, who is in his teens during these events, witnesses his family’s death and the horrors of the concentration camps. {} questions his faith when he sees a young boy hanging on the gallows during {} day.".format(En1, En3, En5, En2, En1, En1, En1, En4)

    Str_night_window = Toplevel(Master)
    Str_night_window.title('Mad Lib Generator - Night')
    Lbl_rslt = Label(Str_night_window, text=Fin_txt, wraplength=300, justify='left').pack()

def md_lib_rndm_gen():
    Lst_of_kywrd = ('Night')
    # , 'Day', 'Happy', 'Sad', 'Funny')
    Kyword = "Night"
    # random.choice(Lst_of_kywrd)
    newWindow = Toplevel(Master)
    newWindow.title('Mad Lib Generator - {}'.format(Kyword))
    newWindow.geometry("600x600")
    if Kyword == 'Night':
        Lbl1 = Label(newWindow, text='Enter a name', ).grid(row=0, column=0)
        En1 = Entry(newWindow, textvariable=En1_var).grid(row=0, column=1)
        Lbl2 = Label(newWindow, text='Enter an object').grid(row=1, column=0)
        En2 = Entry(newWindow, textvariable=En2_var).grid(row=1, column=1)
        Lbl3 = Label(newWindow, text='Enter a place').grid(row=2, column=0)
        En3 = Entry(newWindow, textvariable=En3_var).grid(row=2, column=1)
        Lbl4 = Label(newWindow, text='Choose raining or clear').grid(row=3, column=0)
        En4 = Entry(newWindow, textvariable=En4_var).grid(row=3, column=1)
        Lbl5 = Label(newWindow, text='Enter a food').grid(row=4, column=0)
        En5 = Entry(newWindow, textvariable=En5_var).grid(row=4, column=1)
        Gen_bttn = Button(newWindow, text="Generate", width=25, command=gen_story_Night).grid(row=5, column=1)
    



    

Master = Tk()
Master.title('Mad Lib Generator')
Master.geometry("400x100")
En1_var, En2_var, En3_var, En4_var, En5_var = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Randomize_bttn = Button(Master, text='Click to Start!', width=25, command=md_lib_rndm_gen)
Randomize_bttn.pack()
Master.mainloop()

