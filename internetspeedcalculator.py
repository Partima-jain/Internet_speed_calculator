from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down: str = str(round(sp.download()/(10**6),2))+"Mbps"
    up = str(round(sp.upload() / (10 ** 6), 2)) + "Mbps"
    down_label.config(text=down)
    up_label.config(text=up)

sp = Tk()  # calling tkinter class tk using variable sp
sp.title("Internet Speed")
sp.geometry("500x500")
sp.config(bg="lavender")


lab = Label(sp,text="Internet speed test",font=("Fixedsys",20,"bold"),bg="lavender",cursor="cross")
lab.place(x=100,y=50,height=30,width=250)

lab = Label(sp,text="Download speed",font=("Fixedsys",20,"bold"),bg="lavender",cursor="cross")
lab.place(x=100,y=120,height=30,width=250)

down_label = Label(sp,text="00",font=("Fixedsys",20,"bold"),cursor="cross")
down_label.place(x=110,y=190,height=30,width=250)

lab = Label(sp,text="Upload speed",font=("Fixedsys",20,"bold"),bg="lavender",cursor="cross")
lab.place(x=100,y=260,height=30,width=250)

up_label = Label(sp,text="00",font=("Fixedsys",20,"bold"),cursor="cross")
up_label.place(x=110,y=330,height=30,width=250)

button = Button(sp,text="Check Internet",font=("Fixedsys",20,"bold"),bg="lavender",relief=RAISED,command=speedcheck)
button.place(x=110,y=400,height=30,width=250)

sp.mainloop()