from tkinter import *
import config as conf
import os


if conf.wiewthk == "yes":
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


  def noshowfunct():
   f = open("config.py", "a")
   f.write('wiewthk = "no"' + "\n")
   f.close()


  thkt = Label(teamthanks, text="THANKS FOR DOWNLOADING BY PINGER DEVELOPERS TEAM", font="Italic", bg="lightgray")
  dev1 = Button(teamthanks, text="ZuraxCraft", font="Italic", fg="green", image=zuraximg, bg="white", command=zuraxfunct,
              borderwidth=2)
  dev2 = Button(teamthanks, font="Italic", fg="green", image=dominikimg, bg="white", command=dominikfunct, borderwidth=2)
  dev3 = Button(teamthanks, fg="green", image=wowfilip999img, bg="white", command=filipfunct, borderwidth=2)
  dev1text = Label(teamthanks, text="ZuraxCraft", font="Italic", fg="black", bg="gray")
  dev2text = Label(teamthanks, text="DominikSLK", font="Italic", fg="black", bg="gray")
  dev3text = Label(teamthanks, text="wowfilip999", font="Italic", fg="black", bg="gray")
  thk = Button(teamthanks, text="not show again", width=50, height=2, bg="lightgray", borderwidth=2, command=noshowfunct)
  tt = ("Italic", 17)
  thkt.config(font=tt)

  dev1text.place(x=500, y=100)
  dev1.place(x=470, y=140)
  dev2.place(x=640, y=140)
  dev3.place(x=810, y=140)
  dev3text.place(x=840, y=100)
  dev2text.place(x=670, y=100)
  thkt.place(x=410, y=20)
  thk.place(x=500, y=500)


else:
   pass


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


png = Entry(root, width=40, font="Sans", borderwidth=2, bg=thm.bg, fg=themefg)
png.insert(END, "")



def helpfunct():
 what = Label(root, text="here write url ->")
 what2 = Label(root, text="click waiting... for wiew settings ->")
 what3 = Label(root, text="after write url click here  ->")
 what.place(x=390, y=200)
 what2.place(x=390, y=100)
 what3.place(x=210, y=600)



def settingsfunct():
    try:
      btnn.forget()
    except:
        pass

    btn.forget()
    settings = Tk()
    settings.title("pinger > settings")
    settings.geometry("1400x700")


    def quit():
        settings.destroy()
        btn = Button(root, width=140, height=2, font="Italic", fg="red", text="waiting...", command=settingsfunct,borderwidth=2, bg=thm.bg)
        btn.place(x=20, y=0)
        btnn.forget()

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

        onpress = Label(settings, text="changes wiew on restart!", bg="darkgray", fg="darkred")
        black = Button(settings, text="black", width=20, height=2, borderwidth=2, command=setblack, fg="darkblue",bg="black", font="Italic")
        gray = Button(settings, text="gray", width=20, height=2, borderwidth=2, command=setgray, fg="darkblue",bg="gray", font="Italic")
        white = Button(settings, text="white", width=20, height=2, borderwidth=2, command=setwhite, fg="darkblue",bg="white", font="Italic")
        reset = Button(settings, text="reset", width=20, height=2, borderwidth=2, command=resetfunct, fg="darkblue",bg="lightgray", font="Italic")

        fntheme = ("Italic", 17)
        pr = ("Italic", 15)
        themetext.config(font=fntheme)

        onpress.config(font=pr)

        themetext.place(x=200, y=50)

        black.place(x=200, y=100)
        gray.place(x=200, y=200)
        white.place(x=200, y=150)
        reset.place(x=200, y=250)


    btnn = Button(root, width=140, height=2, font="Italic", fg="darkgreen", text="opened settings...",command=settingsfunct, bg=thm.bg)
    quitbtn = Button(settings, width=40, height=2, font="Times", fg="darkblue", text="exit", command=quit,bg="lightgray", borderwidth=2)
    theme = Button(settings, width=40, height=2, font="Times", command=setcolor, fg="darkblue", text="theme",bg="lightgray", borderwidth=2)

    theme.place(x=500, y=0)
    quitbtn.place(x=500, y=50)
    btnn.pack(side =TOP)


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
                btnn.forget()
                btn4.place(side = TOP)
            except:
                pass


        u = Label(root, text=t, fg="darkgreen", font="Italic")
        rq = Label(root, text="from: ", fg="darkgreen")
        rq.place(x=510, y=440)
        u.place(x=560, y=440)

    except:
        if png.get() == "":
            btn.forget()
            btn2 = Button(root, width=140, height=2, font="Italic", fg="darkred", text="You must write something!",bg=thm.bg)
            helpfunct()
            btn2.pack(side= TOP)
        else:
            btn.forget()
            btn2 = Button(root, width=140, height=2, font="Italic", fg="darkred", text="offline!", bg=thm.bg)
            btn2.place(x=40, y=0)
        if conf.dom == "yes":
            try:
                knc = socket.gethostbyname(png.get() + ".xyz")
                xyzav = Label(root, text="[info] available with .xyz", fg="darkred", font="Italic", bg=thm.bg)
                xyzav.config(font=desing.f)
                xyzav.place(x=560, y=360)

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
                inf.place(x=560, y=390)
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




btn2 = Button(root, width=140, height=2, font="Italic", fg="darkgreen", text="online!", bg=thm.bg)
btn2.place(x=0,y=0)

btn = Button(root, width=140, height=2, font="Italic", fg="red", text="waiting...", command=settingsfunct,borderwidth=2, bg=thm.bg)
help = Button(root, width=2, height=1, fg="blue", text="?", command=helpfunct, borderwidth=2, bg=thm.bg)
check = Button(root, width=40, height=2, font="Italic", fg=themefg, text="check", command=checkping, bg=thm.bg)

cf = ("Italic", 14)
ch = ("Italic", 9)

help.config(font=ch)
check.config(font=cf)
devsettings = Button(root, width=40, height=2, text="settings")

btn.pack(side= TOP)
png.place(x=500, y=200)
check.place(x=420, y=595)
help.place(x=905, y=200)


root.mainloop()