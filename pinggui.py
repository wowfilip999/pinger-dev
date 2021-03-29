from tkinter import *
import config as conf
import platform
import platform
import os


to = platform.system()

p = platform.system()


teamthanks = Tk()
teamthanks.title("pinger-dev /development version/ for wiew app window close this window")
teamthanks.geometry("1400x700")

zuraximg = PhotoImage(file = "zurax.png")
dominikimg = PhotoImage(file = "dominik.png")
wowfilip999img = PhotoImage(file = "wowfilip999.png")

import webbrowser

def zuraxfunct():
 webbrowser.open("https://github.com/ZuraxCraft")

def dominikfunct():
 webbrowser.open("https://github.com/DominikSLK")

def filipfunct():
 webbrowser.open("https://github.com/wowfilip999")

thkt = Label(teamthanks,text="THANKS FOR DOWNLOADING BY PINGER DEVELOPERS TEAM",font="Italic")
dev1 = Button(teamthanks,text="ZuraxCraft",font="Italic",fg="green",image=zuraximg,bg="white",command=zuraxfunct,borderwidth=2)
dev2 = Button(teamthanks,font="Italic",fg="green",image=dominikimg,bg="white",command=dominikfunct,borderwidth=2)
dev3 = Button(teamthanks,fg="green",image=wowfilip999img,bg="white",command=filipfunct,borderwidth=2)
dev1text = Label(teamthanks,text="ZuraxCraft",font="Italic",fg="black",bg="gray")
dev2text = Label(teamthanks,text="DominikSLK",font="Italic",fg="black",bg="gray")
dev3text = Label(teamthanks,text="wowfilip999",font="Italic",fg="black",bg="gray")
thk = Button(teamthanks,text="about pinger",width=50,height=2,bg="lightgray",borderwidth=2)
tt = ("Italic", 17)
thkt.config(font=tt)

dev1text.place(x=500,y=100)
dev1.place(x=470,y=150)
dev2.place(x=640,y=150)
dev3.place(x=810,y=150)
dev3text.place(x=840,y=100)
dev2text.place(x=670,y=100)
#zuraximg.place(x=500,y=200)
thkt.place(x=410,y=20)
thk.place(x=500,y=500)



root = Tk()

root.title("pinger-dev")


if p == "Windows":
  root.geometry("1400x700")
  root.resizable(0, 0)

if p == "Linux":
  root.geometry("1400x700")
  root.resizable(0,0)

kn = Entry(root, width=30, font="Italic", bg="red")
png = Entry(root, width=40, font="Sans",bg="lightgray")
png.insert(END, "")
kn.insert(END, "")


# btn = Button(root,width=120,height=2,font="Italic",fg="red",text="waiting...")

def helpfunct():
 what = Label(root,text="here write url ->")
 what2 = Label(root,text="click waiting... for wiew settings ->")
 what3 = Label(root,text="after write url click here  ->")
 what.place(x=390,y=200)
 what2.place(x=390,y=100)
 what3.place(x=210, y=600)

def settingsfunct(): #tady je settings co vyběhne po kliknutí na wait
 btn.forget()
 settings = Tk()
 settings.title("pinger > settings") #vymyslíme asi lepší název pro app
 settings.geometry("1400x700")

 def chkset(): #zobrazí entry
  chkoption = Entry(settings,width=20)
  chkoption.insert(END , "")



  if chkoption == "all": # z toho nějak vykouzlím nastavení checku :D
    pass

  if chkotion == "basic":
    pass


 def quitset():
  settings.destroy()


 btnn = Button(root, width=120, height=2, font="Italic",fg="darkgreen",text="opened settings...", command=settingsfunct)
 quitbtn = Button(settings,width=40, height=2, font="Times",fg="darkblue",text="exit",command=quitset,bg="lightgray",borderwidth=2)
 testfunkce = Button(settings,width=40,height=2,font="Times",fg="darkblue",text="check option",bg="lightgray",borderwidth=2)

 testfunkce.place(x=500,y=10)
 quitbtn.place(x=500,y=60)
 btnn.place(x=40, y=0)


def checkping():
    import socket
    class desing:
      f = ("Italic", 14)

    try:
        btn4 = Button(root, width=120, height=2, font="Italic", fg="darkgreen", text="online!")
        t = socket.gethostbyname(png.get())
        if "1" or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("9") or ("10") in t:  # ip detection
            iptype = Label(root, text="IPV4", font="Italic", fg="darkgreen")
            iptype.place(x=508, y=460)

        else:
            iptype = Label(root, text="IPV6", font="Italic", fg="darkgreen")
            iptype.place(x=508, y=460)

        btn.forget()
        try:
           btn.forget()
           btn4.place(x=40,y=0)
        except:
            pass


        u = Label(root, text=t, fg="darkgreen", font="Italic")
        rq = Label(root, text="from: ", fg="darkgreen")
        rq.place(x=510, y=440)
        u.place(x=560, y=440)

    except:
        btn.forget()
        btn2 = Button(root, width=120, height=2, font="Italic", fg="darkred", text="offline!")
        btn2.place(x=40, y=0)
        if conf.dom == "yes":
            try:
                knc = socket.gethostbyname(png.get() + ".xyz")
                inf = Label(root, text="[info] available with .xyz", fg="darkred", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=360)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".sk")
                inf = Label(root, text="[info] available with .sk", fg="darkblue", font="Intalic")
                inf.config(font=desing.f)
                inf.place(x=560, y=380)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".eu")
                inf = Label(root, text="[info] available with .eu", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=400)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".cz")
                inf = Label(root, text="[info] available with .cz", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=420)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".gg")
                inf = Label(root, text="[info] available with .gg", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=440)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".net")
                inf = Label(root, text="[info] available with .net", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=460)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".pl")
                inf = Label(root, text="[info] available with .pl", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=480)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".tk")
                inf = Label(root, text="[info] available with .tk", fg="darkblue", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=500)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".com")
                inf = Label(root, text="[info] available with .com", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=520)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".online")
                inf = Label(root, text="[info] available with .online", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=540)
            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".org")
                inf = Label(root, text="[info] available with .org", fg="darkgreen", font="Italic")
                inf.config(font=desing.f)
                inf.place(x=560, y=560)
            except:
                pass


btn2 = Button(root, width=120, height=2, font="Italic", fg="darkgreen", text="online!")
btn2.place(x=50, y=0)

btn = Button(root, width=120, height=2, font="Italic", fg="red", text="waiting...",command=settingsfunct)
help = Button(root,width=2,height=1,fg="blue",text="?",command=helpfunct)
check = Button(root, width=40, height=2, font="Italic", text="check", command=checkping)
cf = ("Italic", 14)
ch = ("Italic", 9)

help.config(font=ch)
check.config(font=cf)
settings = Button(root, width=40, height=2, text="settings")

btn.place(x=40, y=0)
kn.place(x=590, y=200)
png.place(x=500, y=200)
check.place(x=420, y=600)
help.place(x=905,y=200)
# settings.place(x=510,y=200)

root.mainloop()