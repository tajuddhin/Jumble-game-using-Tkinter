import tkinter as tk
import random
from tkinter import messagebox
class Application:
    def __init__(self):
        app = tk.Tk()
        mystring =tk.StringVar(app)
        app.title("Jumble Word Game")
        app.geometry('1080x1080')
        app.configure(bg='ROYALBLUE')
        def jum():
            word=['Apple','Watermelon','Orange','Pear','Cherry','Strawberry','Nectarine','Grape','Mango','Blueberry','Pomegranate','Plum','Banana','Raspberry','Mandarin','Jackfruit','Papaya','Pineapple','Lime','Lemon','Apricot','Grapefruit','Melon','Coconut','Avocado','Peach']
            w=random.choice(word)
            global c
            c=w
            l=list(w)
            random.shuffle(l)
            return ''.join(l)
        def check():
             data=mystring.get()
             if data==c:
                messagebox.showinfo("Congratulations","Correct Answer")
                t1.set(jum())
                
             else:
                messagebox.showinfo("Oops", "Wrong Answer")
            
        tk.Label(app,text="Jumble word Game",bg="white",font=('helvetica', 20,"bold"),fg="red").pack()
        tk.Label(app,text="                          Guess the below word                           ",bg="white",font=('arial', 20,"bold"),fg="#7FFF11").pack(padx=20,pady=50)
        nu = tk.StringVar()
        t1=tk.StringVar()
        t1.set(jum())
        t=tk.Label(app,textvariable=t1,bg='white',font=('arial',60),fg="#7FFF00").pack(pady=32)
        tk.Label(app,text="Enter answer",bg='white',font=('arial',20),fg="#7F2200").pack(side="top",pady=10)
        self.e=tk.Entry(app,textvariable=mystring,width=40).pack(side="top")
        tk.Button(app, text="submit",font=('arial',20),command=check).pack(pady=10)
        app.mainloop()


    

taj=Application()
	
