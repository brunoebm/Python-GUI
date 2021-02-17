from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#criar janela:
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.95)
jan.iconbitmap(default="C:/Users/marti/OneDrive/Documents/GitHub/Python-GUI/icons/LogoIcon.ico")

#carregando imagens:
logo = PhotoImage(file="C:/Users/marti/OneDrive/Documents/GitHub/Python-GUI/icons/logo.png")


#widgets:
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#entradas de login e password:
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic",20), bg="MIDNIGHTBLUE",fg="white")
UserLabel.place(x=15, y=110)

UserEntry = ttk.Entry(RightFrame,width=32)
UserEntry.place(x=160, y=125)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic",20), bg="MIDNIGHTBLUE",fg="white")
PassLabel.place(x=15, y=160)

PassEntry = ttk.Entry(RightFrame,width=32, show="*")
PassEntry.place(x=160, y=175)

#Botoes:
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
    #removendo widgets de login
    LoginButton.place(x=7000)
    RegisterButton.place(x=7000)
    #inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=15, y=15)

    NomeEntry = Entry(RightFrame, width=40)
    NomeEntry.place(x=115, y=30)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=15, y=65)

    EmailEntry = Entry(RightFrame, width=40)
    EmailEntry.place(x=115, y=80)

    def BackToLogin():
        #Removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Back.place(x=5000)
        RegisterData.place(x=5000)
        #trazendo de volta os widgets de login
        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=125, y=260)

    RegisterData = ttk.Button(RightFrame, text="Register", width=30, command=Register)
    RegisterData.place(x=100, y=225)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)



jan.mainloop()
