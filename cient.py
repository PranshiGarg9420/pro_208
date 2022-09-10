from threading import Thread
import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

SERVER= None
IP_ADDRESS= '127.0.0.1'
PORT= 8050
BUFFER_SIZE= 4096


def musicWindow():
    window= Tk()
    window.title('Music Window')
    window.geometry('600x600')
    window.configure(bg='pink')
    
    selectlabel = Label(window, text= "Select Song",bg='pink', font = ("Calibri",15))
    selectlabel.place(x=2, y=1)
    
    listbox = Listbox(window,height = 15,width = 52,activestyle = 'dotbox',bg='pink',borderwidth=2, font = ("Calibri",14))
    listbox.place(x=10,y=40)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play", width=13,bd=1,bg='tomato',font = ("Calibri",14))
    PlayButton.place(x=30,y=440)
    
    Stop=Button(window,text="Stop",bd=1,width=13,bg='tomato', font = ("Calibri",14))
    Stop.place(x=200,y=440)
    
    Upload=Button(window,text="Upload",width=13,bd=1,bg='tomato', font = ("Calibri",14))
    Upload.place(x=30,y=490)
    
    Download =Button(window,text="Download",width=13,bd=1,bg='tomato', font = ("Calibri",14))
    Download.place(x=200,y=490)

    infoLabel = Label(window, text= "",fg= "blue",bg='tomato', font = ("Calibri",11))
    infoLabel.place(x=4, y=550)
    
    window.mainloop()





def setup():
    global IP_ADDRESS
    global SERVER
    global PORT

    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()
