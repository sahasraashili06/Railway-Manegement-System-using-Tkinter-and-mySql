from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector


root = Tk()

'''''
def takedata():
    with open("record.txt", "a") as f:
        f.write(
            f"{name.get(),email.get(), contact_number.get(),gender.get(),password.get()}\n")
    Label(f1, text="successfully Registered!!",
          bg="lightgray", font=("Algerian", 16)).place(x=200, y=400)
    root.after(3000, root.destroy())
   #import login'''''



def add1():
    if name.get()=="" or email.get()==""or contact_number.get()==""or password.get()==""or re_entered_passwword.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif password.get()!=re_entered_passwword.get():
        messagebox.showerror("Error", "password and confirm password must be same")

    else:
        nm=name.get()
        cont=contact_number.get()
        gen=gender.get()
        em1=email.get()
        pw=password.get()
        pw1=re_entered_passwword.get()
        mycon = mysql.connector.connect(host="localhost", user="root", password="", database="railway")
        cur = mycon.cursor()
        try:
            sql="insert into register(nm1,cont1,gen1,em2,pwd,pwd1)values(%s,%s,%s,%s,%s,%s)"
            val=(nm,cont,gen,em1,pw,pw1)
            cur.execute(sql,val)
            mycon.commit()
            lastid=cur.lastrowid
            messagebox.showinfo("Information","Record inserted successfully")
            '''name.delete(0,END)
            contact_number.delete(0, END)
            email.delete(0,END)
            password.delete(0,END)
            re_entered_passwword.delete(0,END)
            name.focus_set()'''
            root.destroy()
            import main
        except:
            mycon.rollback()
            mycon.close()


root.geometry("700x600")
root.title("registration form")
t=Label(root,text="WELCOME TO IRCTC",bd=10,relief=GROOVE,font=("Monotype Corsiva",35,"bold"),fg="blue",bg="cyan")
t.pack(side=TOP,fill=X)
f1 = Frame(root, width=650, height=550, bg="lightgray").pack(pady=20)

name = StringVar()
email = StringVar()
contact_number = StringVar()
gender = StringVar()
password = StringVar()
re_entered_passwword = StringVar()

label1 = Label(f1, text="Enter Name: ", width=10,
               font=("arial", 12), bg="lightgray")
label1.place(x=200, y=100)
entry1 = Entry(f1, textvariable=name)
entry1.place(x=350, y=100)

label2 = Label(f1, text="Enter Email: ", width=10,
               font=("arial", 12), bg="lightgray")
label2.place(x=200, y=130)
entry2 = Entry(f1, textvariable=email)
entry2.place(x=350, y=130)

label3 = Label(f1, text="Contact Number:", width=13,
               font=("arial", 12), bg="lightgray")
label3.place(x=200, y=170)
entry3 = Entry(f1, textvariable=contact_number)
entry3.place(x=350, y=170)

label4 = Label(f1, text="Select Gender", width=15,
               font=("arial", 12), bg="lightgray")
label4.place(x=200, y=210)
gender = StringVar()
gender.set("radio")
radio = Radiobutton(f1, text="Male", padx=5, variable=gender,
                    value="Male", bg="lightgray").place(x=350, y=210)
radio = Radiobutton(f1, text="Female", padx=10,
                    variable=gender, value="Female", bg="lightgray").place(x=410, y=210)
radio = Radiobutton(f1, text="others", padx=15,
                    variable=gender, value="others", bg="lightgray").place(x=490, y=210)


label5 = Label(f1, text="Enter Password", width=13,
               font=("arial", 12), bg="lightgray")
label5.place(x=200, y=250)
entry5 = Entry(f1, show='*', textvariable=password)
entry5.place(x=350, y=250)

label6 = Label(f1, text="Re-Enter Password", width=15,
               font=("arial", 12), bg="lightgray")
label6.place(x=200, y=280)
entry6 = Entry(f1, show='*', textvariable=re_entered_passwword)
entry6.place(x=350, y=280)

Button(f1, text="Register", width=10, command=add1).place(x=300, y=350)
root.mainloop()