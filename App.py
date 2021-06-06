import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("img4.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text = 'login', bg='ivory', bd = 10, font =("Arial", 20))
        border.pack(fill="both", expand = "yes", padx = 150, pady = 150)

        L1 = tk.Label(border, text = "Username", font = ("Arial Bold", 15), bg = "ivory")
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg = "ivory")
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show = "*", bd=5)
        T2.place(x=180, y=80)

        def verify():
            with open("paramconx.txt", "r") as f:
                info = f.readlines()
                i=0
                for e in info:
                    u, p=e.split(",")
                    if u.strip() == T1.get() and p.strip() == T2.get():
                        controller.show_frame(Secondpage)
                        i = 1
                        break
                if i == 0:
                    messagebox.showinfo("Erreur", "Nom d'utilisateur et mot de passe incorrect")

        B1 = tk.Button(border, text="SUBMIT ", font=("Arial", 15), bg = "ivory", command = verify)
        B1.place(x=320, y=115)

        def register():
            window = tk.Tk()
            window.configure(bg='ivory')
            window.title("Inscription")

            l1=tk.Label(window, text="Usernanme", font = ("Arial", 15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1=tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="+", bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password ", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="+", bd=5)
            t3.place(x=200, y=110)

            def check():
                if t1.get() !="" or t2.get() !="" or t3.get() != "":
                    if t2.get() == t3.get():
                        with open("paramconx.txt", "a") as f :
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("bienvenue", "Inscription reussie!!")
                    else:
                        messagebox.showinfo("Erreur", "vos mots de passe ne correspondent pas!!")
                else:
                    messagebox.showinfo("Erreur", "Veuillez renseigner tous les champs")
            b1=tk.Button(window, text="S'inscrire", font=("Arial", 15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)

            window.geometry("470x220")
            window.mainloop()

        B2 = tk.Button(self, text = "Register", bg = "dark orange", font=("Arial", 15), command = register)
        B2.place(x=650, y=20)


class Secondpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("img1.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="File Downloader", font=("Arial", 15))
        Button.place(x=350, y=250)

        Button = tk.Button(self, text="NEXT", font=("Arial", 15), command=lambda: controller.show_frame(Thirdpage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="BACK", font=("Arial", 15), command=lambda: controller.show_frame(Firstpage))
        Button.place(x=100, y=450)


class Thirdpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("img1.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        def loadmap():
            load = Image.open("carte3.png")
            photo = ImageTk.PhotoImage(load)
            label = tk.Label(self, image=photo)
            label.image = photo
            label.place(x=5, y=5)

        Button = tk.Button(self, text="Charger la carte", font=("Arial", 15), command=loadmap)
        Button.place(x=350, y=250)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Firstpage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="BACK", font=("Arial", 15), command=lambda: controller.show_frame(Secondpage))
        Button.place(x=100, y=450)
#lier les differentes pages
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #creation d' une fenetre
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        #Dictionnaire pour iterer a travers les pages
        self.frames = {}
        for F in(Firstpage, Secondpage, Thirdpage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.maxsize(1200, 800)
app.mainloop()
