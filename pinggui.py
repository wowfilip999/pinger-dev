from tkinter import *
import config as conf
import platform
import os

to = platform.system()

p = platform.system()

teamthanks = Tk()
teamthanks.title("pinger-dev /development version/ for wiew app window close this window")
teamthanks.geometry("1400x700")

zuraximg = PhotoImage(file="zurax.png")
dominikimg = PhotoImage(file="dominik.png")
wowfilip999img = PhotoImage(file="wowfilip999.png")

import webbrowser


def zuraxfunct():
    webbrowser.open("https://github.com/ZuraxCraft")


def dominikfunct():
    webbrowser.open("https://github.com/DominikSLK")


def filipfunct():
    webbrowser.open("https://github.com/wowfilip999")


def aboutfunct():
    about = Tk()
    about.title("about")
    about.geometry("1400x700")
    about.resizable(0, 0)

    whypinger = Label(about, text="why pinger?", bg="lightgray", fg="darkblue")
    about1 = Label(about, text="open source", bg="lightgray", fg="darkblue")
    af = ("Italic", 20)
    wf = ("Italic", 22)

    about1.config(font=af)
    whypinger.config(font=wf)
    whypinger.place(x=520, y=10)
    freet.place(x=100, y=200)
    about1.place(x=100, y=100)


thkt = Label(teamthanks, text="THANKS FOR DOWNLOADING BY PINGER DEVELOPERS TEAM", font="Italic", bg="lightgray")
dev1 = Button(teamthanks, text="ZuraxCraft", font="Italic", fg="green", image=zuraximg, bg="white", command=zuraxfunct,
              borderwidth=2)
dev2 = Button(teamthanks, font="Italic", fg="green", image=dominikimg, bg="white", command=dominikfunct, borderwidth=2)
dev3 = Button(teamthanks, fg="green", image=wowfilip999img, bg="white", command=filipfunct, borderwidth=2)
dev1text = Label(teamthanks, text="ZuraxCraft", font="Italic", fg="black", bg="gray")
dev2text = Label(teamthanks, text="DominikSLK", font="Italic", fg="black", bg="gray")
dev3text = Label(teamthanks, text="wowfilip999", font="Italic", fg="black", bg="gray")
thk = Button(teamthanks, text="about pinger", width=50, height=2, bg="lightgray", borderwidth=2, command=aboutfunct)
tt = ("Italic", 17)
thkt.config(font=tt)

dev1text.place(x=500, y=100)
dev1.place(x=470, y=140)
dev2.place(x=640, y=140)
dev3.place(x=810, y=140)
dev3text.place(x=840, y=100)
dev2text.place(x=670, y=100)
# zuraximg.place(x=500,y=200)
thkt.place(x=410, y=20)
thk.place(x=500, y=500)

root = Tk()

root.title("pinger-dev")

import theme as thm

if thm.bg == "black":
    themefg = "white"
else:
    themefg = "black"


root.geometry("1400x700")
root.configure(background=thm.bg)
root.resizable(0, 0)


kn = Entry(root, width=30, font="Italic", bg="red")
png = Entry(root, width=40, font="Sans", borderwidth=2, bg=thm.bg, fg=themefg)
png.insert(END, "")
kn.insert(END, "")



def helpfunct():
 try:
   if enable == "yes":
     print("f")
 except:
     pass

 what = Label(root, text="here write url ->")
 what2 = Label(root, text="click waiting... for wiew settings ->")
 what3 = Label(root, text="after write url click here  ->")
 what.place(x=390, y=200)
 what2.place(x=390, y=100)
 what3.place(x=210, y=600)
 enable ="yes"



def settingsfunct():
    btn.forget()
    settings = Tk()
    settings.title("pinger > settings")
    settings.geometry("1400x700")

    def chkset():
        chkoption = Entry(settings, width=20)
        chkoption.insert(END, "")

        if chkoption == "all":
            pass

        if chkotion == "basic":
            pass

    def quitset():
        settings.destroy()
        btn = Button(root, width=140, height=2, font="Italic", fg="red", text="waiting...", command=settingsfunct,
                     borderwidth=2, bg=thm.bg)
        btn.place(x=40, y=0)

    def setcolor():
        themetext = Label(settings, text="background color", bg="lightgray")

        def setblack():
            file = open("theme.py", "w")
            file.write('bg = "black" ')

            file.close()

            onpress.place(x=500, y=400)

        def setgray():
            file = open("theme.py", "w")
            file.write('bg = "gray" ')

            file.close()

            onpress.place(x=500, y=400)

        def setwhite():
            file = open("theme.py", "w")
            file.write('bg = "white" ')

            file.close()

            onpress.place(x=500, y=400)

        def resetfunct():
            file = open("theme.py", "w")
            file.write('bg = "lightgray" ')

            file.close()

            onpress.place(x=500, y=400)

        onpress = Label(settings, text="changens wiew on restart!", bg="darkgray", fg="darkred")
        black = Button(settings, text="black", width=20, height=2, borderwidth=2, command=setblack, fg="darkblue",
                       bg="black", font="Italic")
        gray = Button(settings, text="gray", width=20, height=2, borderwidth=2, command=setgray, fg="darkblue",
                      bg="gray", font="Italic")
        white = Button(settings, text="white", width=20, height=2, borderwidth=2, command=setwhite, fg="darkblue",
                       bg="white", font="Italic")
        reset = Button(settings, text="reset", width=20, height=2, borderwidth=2, command=resetfunct, fg="darkblue",
                       bg="lightgray", font="Italic")

        fntheme = ("Italic", 17)
        pr = ("Italic", 15)
        themetext.config(font=fntheme)

        onpress.config(font=pr)

        themetext.place(x=200, y=50)

        black.place(x=200, y=100)
        gray.place(x=200, y=200)
        white.place(x=200, y=150)
        reset.place(x=200, y=250)

    btnn = Button(root, width=140, height=2, font="Italic", fg="darkgreen", text="opened settings...",
                  command=settingsfunct, bg=thm.bg)
    quitbtn = Button(settings, width=40, height=2, font="Times", fg="darkblue", text="exit", command=quitset,
                     bg="lightgray", borderwidth=2)
    testfunkce = Button(settings, width=40, height=2, font="Times", fg="darkblue", text="check option", bg="lightgray",
                        borderwidth=2)
    theme = Button(settings, width=40, height=2, font="Times", command=setcolor, fg="darkblue", text="theme",
                   bg="lightgray", borderwidth=2)

    testfunkce.place(x=500, y=10)
    theme.place(x=500, y=110)
    quitbtn.place(x=500, y=60)
    btnn.place(side= TOP)


def checkping():
    import socket
    class desing:
        f = ("Italic", 14)

    try:
        btn4 = Button(root, width=140, height=2, font="Italic", fg="darkgreen", text="online!", bg=thm.bg)
        if png.get() == "":
            pass
        else:
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
                btn4.place(x=40, y=0)
            except:
                pass


        u = Label(root, text=t, fg="darkgreen", font="Italic")
        rq = Label(root, text="from: ", fg="darkgreen")
        rq.place(x=510, y=440)
        u.place(x=560, y=440)

    except:
        if png.get() == "":
            btn.forget()
            btn2 = Button(root, width=140, height=2, font="Italic", fg="darkred", text="You must write something!",
                          bg=thm.bg)
            helpfunct()
            btn2.place(x=40, y=0)
        else:
            btn.forget()
            btn2 = Button(root, width=140, height=2, font="Italic", fg="darkred", text="offline!", bg=thm.bg)
            btn2.place(x=40, y=0)
        if conf.dom == "yes":
            try:
                knc = socket.gethostbyname(png.get() + ".xyz")
                inf = Label(root, text="[info] available with .xyz", fg="darkred", font="Italic", bg=thm.bg)
                inf.config(font=desing.f)
                inf.place(x=560, y=360)

            except:
                pass

            try:
                knc = socket.gethostbyname(png.get() + ".sk")
                inf = Label(root, text="[info] available with .sk", fg="darkblue", font="Intalic")
                inf.config(font=desing.f)

                def skchk():
                    png.insert(END, "")
                    png.insert(END, png.get() + ".sk")

                checksk = Button(root, text="check .sk", width=12, fg="blue", bg="white", font="Italic", command=skchk)
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
                comonline = "yes"

                inf.place(x=560, y=520)
            except:
                comonline = "no"
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


btn2 = Button(root, width=140, height=2, font="Italic", fg="darkgreen", text="online!", bg=thm.bg)
btn2.place(x=40, y=0)

btn = Button(root, width=140, height=2, font="Italic", fg="red", text="waiting...", command=settingsfunct,borderwidth=2, bg=thm.bg)
help = Button(root, width=2, height=1, fg="blue", text="?", command=helpfunct, borderwidth=2, bg=thm.bg)
check = Button(root, width=40, height=2, font="Italic", fg=themefg, text="check", command=checkping, bg=thm.bg)
cf = ("Italic", 14)
ch = ("Italic", 9)

help.config(font=ch)
check.config(font=cf)
settings = Button(root, width=40, height=2, text="settings")

btn.pack(side= TOP)
kn.place(x=590, y=200)
png.place(x=500, y=200)
check.place(x=420, y=600)
help.place(x=905, y=200)


root.mainloop()
