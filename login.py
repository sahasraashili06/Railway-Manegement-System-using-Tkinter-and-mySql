from tkinter import *
from tkinter import messagebox
import random
import mysql.connector

root = Tk()

train_sourse = StringVar()
train_destination = StringVar()
no_of_passanger = IntVar()
ticket_no = StringVar()
price = StringVar()
clas = StringVar()
payment = StringVar()




def add2():
   # if train_sourse.get() == "" or train_destination.get() == "" or no_of_passanger.get() or clas.get() == "" or payment.get() == "":
      #  messagebox.showerror("Error", "All fields are required")
   # else:
        trs=train_sourse.get()
        trd=train_destination.get()
        cl=clas.get()
        nop=no_of_passanger.get()
        pay=payment.get()


        mycon = mysql.connector.connect(host="localhost", user="root", password="", database="rail")
        cur = mycon.cursor()
        try:
            sql="insert into data2(trs1,trd1,cl1,nop1,pay1)values(%s,%s,%s,%s,%s)"
            val=(trs,trd,cl,nop,pay)
            cur.execute(sql,val)
            mycon.commit()
            messagebox.showinfo("Information","Record saved Successfully")
        except:
            mycon.rollback()
            mycon.close()


def home_page():
    home_frame = Frame(main_frame, height=650, width=700, bg="#00599F")

    train_name = StringVar()
    Label(home_frame, text="Welcome To Indian Railways", padx=20, pady=20, font=("Microsoft", 16, "bold"),
          bg="khaki", borderwidth=3, relief=RIDGE).place(x=200, y=10)
    Label(home_frame, text="All Railway services in oneplace.An initiative by National e-Governance Division (NeGD), Ministry of Electronics\n and Information Technology (MeitY). UMANG strives to be the one stop gateway to all government schemes\nand services through different channels like Mobile Application(iOS, Android), Chatbot, Voice Bot and Website.", padx=20, pady=20, font=("Microsoft", 10),
          bg="#00599F", borderwidth=0, fg="white").place(x=2, y=100)
    Label(home_frame, text="History", font=("Microsoft", 11, "bold"),
          bg="khaki", borderwidth=3, relief=RIDGE).place(x=10, y=190)
    Label(home_frame, text="All Railway services in oneplace.An initiative by National e-Governance Division (NeGD), Ministry of Electronics\n and Information Technology (MeitY). UMANG strives to be the one stop gateway to all government schemes\nand services through different channels like Mobile Application(iOS, Android), Chatbot, Voice Bot and Website.", padx=10, font=("Microsoft", 10),
          bg="#00599F", borderwidth=0, fg="white").place(x=2, y=230)
    Label(home_frame, text="Popular Services", font=("Microsoft", 11, "bold"),
          bg="khaki", borderwidth=3, relief=RIDGE).place(x=10, y=300)
    Label(home_frame, text="1. Season Ticket", font=("Microsoft", 9, "bold"),
          bg="white", borderwidth=3, relief=RIDGE).place(x=10, y=350)
    Label(home_frame, text="2. Raise Claim", font=("Microsoft", 9, "bold"),
          bg="white", borderwidth=3, relief=RIDGE).place(x=10, y=400)
    Label(home_frame, text="3. Public Grievance", font=("Microsoft", 9, "bold"),
          bg="white", borderwidth=3, relief=RIDGE).place(x=10, y=450)
    Label(home_frame, text="Services by States", font=("Microsoft", 11, "bold"),
          bg="khaki", borderwidth=3, relief=RIDGE).place(x=460, y=350)
    Label(home_frame, text="Explore services offered by different States and\nUnion Territories of India!", font=("Microsoft", 9),
          bg="#00599F", border=0, fg="white").place(x=400, y=400)
    Button(home_frame, text="Explore 30+ states").place(x=475, y=450)
    downbar = Frame(home_frame, height=50, width=700,
                    bg="lightblue").place(x=0, y=530)
    Label(downbar, text="User Manual", bg="lightblue",
          bd=0, fg="black").place(x=30, y=570)
    Label(downbar, text="Privacy Police", bg="lightblue",
          bd=0, fg="black").place(x=110, y=570)
    Label(downbar, text="FAQ", bg="lightblue",
          bd=0, fg="black").place(x=550, y=570)
    Label(downbar, text="FeedBack", bg="lightblue",
          bd=0, fg="black").place(x=600, y=570)
    home_frame.place(x=0, y=30)


def ticket_page():
    ticket_frame = Frame(main_frame, height=650, width=700, bg="lightblue")

    f1 = Frame(ticket_frame, width=600, height=500,
               bg="lightgrey", borderwidth=3, relief=RIDGE).place(x=50, y=30)
    Label(f1, text="Enter the following Details", font=30,
          borderwidth=3, relief=RIDGE).place(x=55, y=64)
    Label(f1, text="Enter source: ", bg="lightgray").place(x=55, y=100)
    train_list = ['Andhra Pradesh', 'Assam', 'Arunachal Pradesh',
                  'Bihar', 'Goa', 'Madhya Pradesh', 'Punjab', 'Uttar Pradesh', 'West Bengal']
    dict = {'Andhra Pradesh-Assam': 2646,
            'Andhra Pradesh-Arunachal Pradesh': 1962.5,
            'Andhra Pradesh-Bihar': 1146.3,
            'Andhra Pradesh-Goa': 744.5,
            'Andhra Pradesh-Madhya Pradesh': 930.9,
            'Andhra Pradesh-Uttar Pradesh': 1250.5,
            'Andhra Pradesh-Punjab': 692,
            'Assam-Arunachal Pradesh': 2858.55,
            'Assam-Bihar': 2962.85,
            'Assam-Goa': 3297.28,
            'Assam-Madhya Pradesh': 3362.56,
            'Assam-Punjab': 3257.72,
            'Assam-Uttar Pradesh': 3426.26,
            'Arunachal Pradesh-Bihar': 950.47,
            'Arunachal Pradesh-Goa': 2550.35,
            'Arunachal Pradesh-Madhya Pradesh': 1669.42,
            'Arunachal Pradesh-Punjab': 1874.61,
            'Arunachal Pradesh-Uttar Pradesh': 1345.14,
            'Bihar-Goa': 1626.69,
            'Bihar-Madhya Pradesh': 729.69,
            'Bihar-Punjab': 925.28,
            'Bihar-Uttar Pradesh': 511.01,
            'Goa-Madhya Pradesh': 1058.98,
            'Goa-Punjab': 1486.42,
            'Goa-Uttar Pradesh': 754.2,
            'Madhya Pradesh-Punjab': 429.42,
            'Madhya Pradesh-Uttar Pradesh': 311.66,
            'Punjab-Uttar Pradesh': 733.44,
            'Andhra Pradesh-West Bengal': 2345,
            'Assam-West Bengal': 1234,
            'Arunachal Pradesh-West Bengal': 6478,
            'Bihar-West Bengal': 2456,
            'Goa-West Bengal': 2245,
            'Madhya Pradesh-West Bengal': 1232,
            'Punjab-West Bengal': 2234,
            'Uttar Pradesh-West Bengal': 2253,
            'West Bengal-Andhra Pradesh': 2345,
            'West Bengal-Assam': 1234,
            'West Bengal-Arunachal Pradesh': 6478,
            'West Bengal-Bihar': 2456,
            'West Bengal-Goa': 2245,
            'West Bengal-Madhya Pradesh': 1232,
            'West Bengal-Punjab': 2234,
            'West Bengal-Uttar Pradesh': 2253
            }

    train_sourse.set("Select source")
    OptionMenu(f1, train_sourse, *train_list).place(x=140, y=95)
    Label(f1, text="Enter destination: ", bg="lightgray").place(x=55, y=150)
    train_destination.set("select destination")
    OptionMenu(f1, train_destination, *train_list).place(x=155, y=145)
    Label(f1, text="Enter Class: ", bg="lightgray").place(x=55, y=200)

    def getticket():
        try:
            x = random.randint(1000, 9999)
            ticket_no.set(str(x))
            textarea.delete(1.0, END)
            textarea.insert(END, "\t\tHappy journey")
            textarea.insert(
                END, f"\n\nTicket Number:\t\t {    ticket_no.get()}")
            p = no_of_passanger.get()
            textarea.insert(END, f"\nNo of passanger: {p} ")
            textarea.insert(
                END, f"\nTravel : from {train_sourse.get()} to {train_destination.get()}")
            textarea.insert(END, f"\nTotal distance :\t\t{dis}")
            textarea.insert(END, f"\nAmount :\t\t{price}")
            save_ticket()
        except:
            messagebox.showwarning(
                'Warning', 'Please verify the details first')

    def save_ticket():
        op = messagebox.askyesno(
            "Save ticket", "Do you want to download ticket ?")
        if op > 0:
            ticket_details = textarea.get('1.0', END)
            f1 = open(str(ticket_no.get())+".txt", "w")
            f1.write(ticket_details)
            f1.close()
            messagebox.showinfo(
                "Saved", f"Ticket no, :{ticket_no.get()} Saved Successfully")
        else:
            return

    def book_ticket():
        global dis
        a = train_sourse.get()
        b = train_destination.get()
        d = a+'-'+b
        c = b+'-'+a
        if a != b:
            if d in dict:
                dis = dict[d]
            elif c in dict:
                dis = dict[c]
        else:
            messagebox.showwarning('Warning ', 'Please select right root')
            return
        messagebox.showinfo('Verified', 'Successfully Verified')
        getticket()

    def fare(cla, myscale):
        if (cla.get() == "AC 1st"):
            price = 60*myscale.get()
            Label(f1, text=f"Rs: {price}/-",
                  bg="lightgray").place(x=170, y=320)
        elif (cla.get() == "AC 2 Tier"):
            price = 50*myscale.get()
            Label(f1, text=f"Rs: {price}/-",
                  bg="lightgray").place(x=170, y=320)
        elif (cla.get() == "AC Chair car"):
            price = 50*myscale.get()
            Label(f1, text=f"Rs: {price}/-",
                  bg="lightgray").place(x=170, y=320)
        elif (cla.get() == "Sleeper"):
            price = 30*myscale.get()
            Label(f1, text=f"Rs: {price}/-",
                  bg="lightgray").place(x=170, y=320)
        else:
            price = 20*myscale.get()
            Label(f1, text=f"Rs: {price}/-",
                  bg="lightgray").place(x=170, y=320)

    #clas = StringVar()
    clas.set("Choose class")
    classlist = ["AC 1st", "AC 2 Tier", "AC Chair car",
                 "Sleeper", "Second string(ordinary)"]
    OptionMenu(f1, clas, *classlist).place(x=155, y=195)

    Label(f1, text="No. of passanger: ",
          bg="lightgray").place(x=55, y=240)

    myscale = Entry(f1, textvariable=no_of_passanger).place(x=170, y=240)

    #payment = StringVar()
    payment.set("Payments")
    payment_list = ["Pytem", "G-pay", "PhonePay", "Card"]
    Label(f1, text="Payment method: ", bg="lightgray").place(x=55, y=280)
    OptionMenu(f1, payment, *payment_list).place(x=170, y=275)

    Label(f1, text="Fare: ", bg="lightgray").place(x=55, y=320)
    faree = Button(f1, text="get fare", bg="white", borderwidth=2, relief=RIDGE,
                   command=lambda: fare(clas, no_of_passanger)).place(x=220, y=320)
    Button(f1, text="Book Ticket", fg="black", bg="white",
           command=book_ticket).place(x=130, y=400)
    Button(f1, text="Save", fg="black", bg="white",
           command=add2).place(x=130, y=360)

    f2 = Frame(f1, width=300, height=300, background="white",
               borderwidth=3, relief=RIDGE).place(x=320, y=90)
    Label(f2, text="Ticket", font=14).place(x=440, y=100)
    textarea = Text(f2, width=45, height=17, bd=0, font='arial 8 bold')
    textarea.place(x=333, y=125)

    ticket_frame.place(x=0, y=30)


def help_page():
    help_frame = Frame(main_frame, height=650, width=700, bg="khaki")
    Label(help_frame, text="Railway Management System",
          font="Algerian 12 bold", borderwidth=3, relief=RIDGE).place(x=20, y=20)
    Label(help_frame, text=f"Unreserved Ticketing System facilitates the ticketing needs of Unreserved journey passengers.This aims to provide a hassle\n free and convenient way of ticket issuance mechanism with added transparency and accountability.",
          bg="khaki", font="Algerian 8", bd=0).place(x=20, y=60)
    Label(help_frame, text="Contact us",
          font="Algerian 11 bold", borderwidth=3, relief=RIDGE).place(x=20, y=100)
    Label(help_frame, text="Telephone no : 011-24104525",
          font="Algerian 11 bold", borderwidth=0, relief=RIDGE, bg="khaki").place(x=20, y=140)
    Label(help_frame, text="Website : https://cris.org.in/",
          font="Algerian 11 bold", borderwidth=0, relief=RIDGE, bg="khaki").place(x=20, y=180)
    Label(help_frame, text="Location : None",
          font="Algerian 11 bold", borderwidth=0, relief=RIDGE, bg="khaki").place(x=20, y=215)
    Label(help_frame, text="Working Hours",
          font="Algerian 11 bold", borderwidth=3, relief=RIDGE).place(x=20, y=250)
    Label(help_frame, text="Monday-Friday (9:30 AM - 06:00 PM)",
          font="Algerian 8 bold", borderwidth=0, relief=RIDGE, bg="khaki").place(x=20, y=290)
    Label(help_frame, text="Address",
          font="Algerian 11 bold", borderwidth=3, relief=RIDGE).place(x=20, y=340)
    Label(help_frame, text="Centre For Railway Information Systems Chanakyapuri New Delhi - 110021",
          font="Algerian 8 bold", borderwidth=0, relief=RIDGE, bg="khaki").place(x=20, y=380)
    Label(help_frame, text="Services",
          font="Algerian 11 bold", borderwidth=3, relief=RIDGE).place(x=20, y=420)
    Label(help_frame, text="Fare Enquiry",
          font="Algerian 9 bold", borderwidth=3, relief=RIDGE).place(x=20, y=460)
    Label(help_frame, text="Season Ticket",
          font="Algerian 9 bold", borderwidth=3, relief=RIDGE).place(x=120, y=460)
    Label(help_frame, text="ATVM Availability",
          font="Algerian 9 bold", borderwidth=3, relief=RIDGE).place(x=230, y=460)
    help_frame.place(x=0, y=30)


def indicator(page):
    page()


root.geometry("700x600")
manubar_frame = Frame(root, width=700, height=30,
                      bg="lightgray").pack(side=TOP)
home_btn = Button(manubar_frame, bg="lightgray", text="Home",
                  background="lightgray", border=0, command=lambda: indicator(home_page)).place(x=5, y=3)
booking_btn = Button(manubar_frame, bg="lightgray", text="Book Ticket",
                     background="lightgray", border=0, command=lambda: indicator(ticket_page)).place(x=60, y=3)
help_btn = Button(manubar_frame, bg="lightgray", text="Help",
                  background="lightgray", border=0, command=lambda: indicator(help_page)).place(x=150, y=3)

main_frame = Frame(root, height=650, width=700, bg="white").pack()
home_page()

root.mainloop()