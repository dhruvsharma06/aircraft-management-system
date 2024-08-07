#Importing all the necessary modules
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import threading
from random import randint
from time import sleep
import webbrowser
import mysql.connector as mc

def fnd():
    ast=Tk()
    ast.title('ENTRY PAGE')
    def sh():
        e1.delete(0,'end')
    b=Button(ast,text='RESET',command=sh,bd=5,bg='Lemonchiffon')
    b.place(x=350,y=105)
    label3=Label(ast,text="ENTRY PASSWORD",font=['Algerian','30','underline','bold'],bg='gold')
    label3.place(x=80,y=0)
    e1=Entry(ast,text = "",show = '*',font='20')
    e1.place(x=150,y=110)
    print()
    print()
    
    def bos():
        if e1.get()=='vishal1234':
            ast.destroy()
            
            '''str3='Start your work sir!!!!'
            ast.destroy()'''

o=Tk()

lb1_label=Label(o,text='AIRCRAFT MANAGEMENT SYSTEM',font=['Algerian','28'],bg='lemonchiffon')
lb1_label.place(x=8,y=20)

def star():
    o.destroy()
    #ESTABLISHING CONNECTION**
    con=mc.connect(host="localhost",user="root",passwd="vishal1234",database="vishal")
    cur=con.cursor()
    #*Creating firstWindow**
    wind=Tk()
    def pilot():
        wind.destroy()
        windo=Tk()
        def login():
            if (((name_entry.get())=="Pilot" or (name_entry.get())=="PILOT" or (name_entry.get())=="pilot")):
                messagebox.showinfo("Information","Welcome"+'  '+''+name_entry.get()+'  '+''"Connected to database successfully")
                windo.destroy()
                a=Tk()
                #*INSERT FUNCTION*
                def insert():
                    b=Tk()
                    def reset():
                        i.delete(0,END)
                        j.delete(0,END)
                        k.delete(0,END)
                        l.delete(0,END)
                        m.delete(0,END)
                        n.delete(0,END)
                        p.delete(0,END)
                        q.delete(0,END)
                    def back():
                        b.destroy()
                    def submit():
                        sql="insert into project values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        values=i.get(),j.get(),k.get(),l.get(),m.get(),n.get(),p.get(),q.get()
                        cur.execute(sql,values)
                        con.commit()
                        messagebox.showinfo("Information","Successfully inserted flight details sir")
                    
                    lbl_label=Label(b,text='DATE',font=['Algerian','10'])
                    lbl_label.place(x=100,y=50)
                    lbl_label=Label(b,text='REGISTRATION_NO',font=['Algerian','10'])
                    lbl_label.place(x=100,y=80)
                    lbl_label=Label(b,text='PILOT_NAME',font=['Algerian','10'])
                    lbl_label.place(x=100,y=110)
                    lbl_label=Label(b,text='AIRCRAFT_TYPE',font=['Algerian','10'])
                    lbl_label.place(x=100,y=140)
                    lbl_label=Label(b,text='AIRCRAFT_IDENT',font=['Algerian','10'])
                    lbl_label.place(x=100,y=170)
                    lbl_label=Label(b,text='FLIGHT_FROM',font=['Algerian','10'])
                    lbl_label.place(x=100,y=200)
                    lbl_label=Label(b,text='FLIGHT_TO',font=['Algerian','10'])
                    lbl_label.place(x=100,y=230)
                    lbl_label=Label(b,text='REMARKS_AND_ENDORSEMENTS',font=['Algerian','10'])
                    lbl_label.place(x=100,y=260)
                    i = Entry(b,text = "",font='16')
                    i.place(x=350,y=50)
                    j = Entry(b,text = "",font='16')
                    j.place(x=350,y=80)
                    k = Entry(b,text = "",font='16')
                    k.place(x=350,y=110)
                    l = Entry(b,text = "",font='16')
                    l.place(x=350,y=140)
                    m= Entry(b,text = "",font='16')
                    m.place(x=350,y=170)
                    n = Entry(b,text = "",font='16')
                    n.place(x=350,y=200)
                    p= Entry(b,text = "",font='16')
                    p.place(x=350,y=230)
                    q= Entry(b,text = "",font='16')
                    q.place(x=350,y=260)
                    login_btn=Button(b,text = 'SUBMIT',command=submit,bd=1)
                    login_btn.place(x=500,y=435)
                    u=Button(b,text = 'BACK',command=back,bd=1)
                    u.place(x=200,y=380)
                    py=Button(b,text = 'RESET',command=reset,bd=1)
                    py.place(x=100,y=380)
                    
                    b.title("INSERT NEW FLIGHT DETAILS")
                    b.geometry('600x500+300+50')
                    b.config(bg="black")
                    b.mainloop()
                
                #UPDATE FUNCTION**
                def update():
                    root=Tk()
                    def back():
                        root.destroy()
                    def fetch():
                        sql="select * from project where Registration_no='%s'"%(e2.get())
                        cur.execute(sql)
                        rows=cur.fetchall()
                        if len(rows)!=0:
                            for row in rows:
                                e1.insert('end',row[0])
                                e3.insert('end',row[2])
                                e4.insert('end',row[3])
                                e5.insert('end',row[4])
                                e6.insert('end',row[5])
                                e7.insert('end',row[6])
                                e8.insert('end',row[7])
                        else:
                            messagebox.showerror(parent=root,title="Error",message="No records found with Billing ID you entered")
                    
                    def submit():
                        sql='update project set Date="%s",Pilot_name="%s",Aircraft_type="%s",Aircraft_ident="%s",Flight_from="%s",Flight_to="%s",Remarks_and_endorsements="%s" where Registration_no="%s"'%(e1.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e2.get())
                        cur.execute(sql)
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)
                        e6.delete(0,END)
                        e7.delete(0,END)
                        e8.delete(0,END)
                        messagebox.showinfo(parent=root,title="SUCCESS",message="Record updated successfully")
                        con.commit()

                    label1=Label(root,text="UPDATING FLIGHT DETAILS")
                    label1.place(x=100,y=50)
                    label2=Label(root,text="DATE",font=['Algerian','10'])
                    label2.place(x=100,y=110)
                    label3=Label(root,text="REGISTRATION_NO",font=['Algerian','10'])
                    label3.place(x=100,y=80)
                    label4=Label(root,text="PILOT_NAME",font=['Algerian','10'])
                    label4.place(x=100,y=140)
                    label5=Label(root,text="AIRCRAFT_TYPE",font=['Algerian','10'])
                    label5.place(x=100,y=170)
                    label6=Label(root,text="AIRCRAFT_IDENT",font=['Algerian','10'])
                    label6.place(x=100,y=200)
                    label7=Label(root,text="FLIGHT_FROM",font=['Algerian','10'])
                    label7.place(x=100,y=230)
                    label12=Label(root,text="FLIGHT_TO",font=['Algerian','10'])
                    label12.place(x=100,y=260)
                    label13=Label(root,text="REMARKS_AND_ENDORSEMENTS",font=['Algerian','10'])
                    label13.place(x=100,y=290)

                    e1 = Entry(root,text = "",font='16')
                    e1.place(x=350,y=110)
                    e2 = Entry(root,text = "",font='16')
                    e2.place(x=350,y=80)
                    e3 = Entry(root,text = "",font='16')
                    e3.place(x=350,y=140)
                    e4 = Entry(root,text = "",font='16')
                    e4.place(x=350,y=170)
                    e5 = Entry(root,text = "",font='16')
                    e5.place(x=350,y=200)
                    e6 = Entry(root,text = "",font='16')
                    e6.place(x=350,y=230)
                    e7 = Entry(root,text = "",font='16')
                    e7.place(x=350,y=260)
                    e8 = Entry(root,text = "",font='16')
                    e8.place(x=350,y=290)
                    login_btn=Button(root,text = 'SUBMIT',command=submit,bd=1)
                    login_btn.place(x=500,y=435)
                    u=Button(root,text = 'BACK',command=back,bd=1)
                    u.place(x=200,y=380)
                    py=Button(root,text = 'FETCH',command=fetch,bd=1)
                    py.place(x=100,y=380)
                    
                    root.title("UPDATE FLIGHT DETAILS")
                    root.geometry('600x500+300+50')
                    root.config(bg="black")
                    root.mainloop()

                # Main menu buttons
                insert_btn = Button(a, text="Insert Flight Details", command=insert)
                insert_btn.pack()
                update_btn = Button(a, text="Update Flight Details", command=update)
                update_btn.pack()
                
                a.mainloop()

        # Login window
        name_label = Label(windo, text="Enter Username:")
        name_label.pack()
        name_entry = Entry(windo)
        name_entry.pack()
        login_btn = Button(windo, text="Login", command=login)
        login_btn.pack()
        
        windo.mainloop()

    # First window buttons
    pilot_btn = Button(wind, text="Pilot Login", command=pilot)
    pilot_btn.pack()
    
    wind.mainloop()

# Start the application
star()
o.mainloop()