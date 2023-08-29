from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import mysql.connector




def register_page():
    root.destroy()
    import register


def sel():
    if user.get()=="" or pas.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        usr=user.get()
        pswrd=pas.get()
    try:
        mycon = mysql.connector.connect(host="localhost", user="root", password="", database="railway")
        cur = mycon.cursor()
        cur.execute("select * from register where em2=%s and pwd=%s", (usr, pswrd))
        row = cur.fetchone()
        if row==None:
            messagebox.showerror('Error',"Invalid user name and password")
            user.delete(0, END)
            pas.delete(0, END)
            user.focus_set()
        else:
            messagebox.showinfo("Success","Welcome user")
            user.delete(0, END)
            pas.delete(0, END)
            root.destroy()
            import login
    except:
        mycon.rollback()
        mycon.close()




root = Tk()
root.title("Login")
root.geometry("700x500")

photo = Image.open("dn.png")
resize_image = photo.resize((300, 300))
img = ImageTk.PhotoImage(resize_image)
var1 = Label(root, image=img, bg="white")
var1.place(x=50, y=100)

frame = Frame(root, width=300, height=300, bg="white")
frame.place(x=370, y=100)

heading = Label(frame, text="Log-in", fg="#57a1f8",
                bg="white", font=("Microsoft", 23, "bold"))
heading.place(x=100, y=5)

username =StringVar()
password = StringVar()


user = Entry(frame, width=25, fg="black", border=0,
             bg="white", font=("Microsoft YaHei UI Light", 11), textvariable=username)
user.place(x=30, y=80)
user.insert(0, "Username")
Frame(frame, width=250, height=2, bg="black").place(x=30, y=107)

pas = Entry(frame, width=25, fg="black", border=0,
            bg="white", font=("Microsoft YaHei UI Light", 11), textvariable=password)
pas.place(x=30, y=120)
pas.insert(INSERT, "Password")
Frame(frame, width=250, height=2, bg="black").place(x=30, y=147)

Button(frame, width=30, pady=7, text="login", bg="#57a1f8",
       fg="white", border=0, command=sel).place(x=35, y=187)

Label(frame, text="Not a user then ", bg="white",
      font=("Microsoft", 8)).place(x=30, y=250)

reg = Button(frame, text="Register now", bg="white", fg="#57a1f8", bd=0,
             command=register_page).place(x=120, y=250)

root.mainloop()