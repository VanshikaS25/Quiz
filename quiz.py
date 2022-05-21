#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="form")
cursor = db.cursor()

back = 'light blue'

root = Tk()
root.title("Form")
root.geometry("800x500")
root.config(bg= back)


desired_font =("Comic Sans MS", 20)
lblheader = Label(root, text="Python Examination", font=desired_font,justify="center", bg=back)
lblheader.pack()

font_for_label=("Comic Sans MS",12) 
lblname = Label(root, text="Name: ",font =font_for_label,bg=back)
lblname.place(x=10,y=80)
txtname = Entry(root,width=70,font=("Comic Sans MS",10))
txtname.place(x=150,y=85)

lblfather = Label(root, text="Father's Name: ",font =font_for_label,bg=back)
lblfather.place(x=10,y=120)
txtfather = Entry(root,width=70,font=("Comic Sans MS",10))
txtfather.place(x=150,y=123)


lblroll = Label(root, text="Roll No.",font=font_for_label,bg=back)
lblroll.place(x=10,y=160)
txtroll = Entry(root,width=70,font=("Comic Sans MS",10))
txtroll.place(x=150,y=163)

lblemail = Label(root, text="Email ID",font=font_for_label,bg=back)
lblemail.place(x=10,y=200)
txtemail = Entry(root,width=70,font=("Comic Sans MS",10))
txtemail.place(x=150,y=203)

lblmobile = Label(root, text="Mobile",font=font_for_label,bg=back)
lblmobile.place(x=10,y=240)
txtmobile = Entry(root,width=70,font=("Comic Sans MS",10))
txtmobile.place(x=150,y=243)

def cmd():
    name = txtname.get()
    roll = txtroll.get()
    fname = txtfather.get()
    email = txtemail.get()
    mobile = txtmobile.get()
    
    lblheader.destroy()
    lblname.destroy()
    txtname.destroy()
    lblfather.destroy()
    txtfather.destroy()
    lblroll.destroy()
    txtroll.destroy()
    lblmobile.destroy()
    txtmobile.destroy()
    lblemail.destroy()
    txtemail.destroy()
    btn_next.destroy()
    
    arr= ["Q1 What is the full form of SQL?",
          "Q2 Which of the following is not a valid SQL type?",
          "Q3 Which of the following is not a DDL command?",
          "Q4 Which of the following are TCL commands?",
          "Q5 Which statement is used to delete all rows in a table without having the action logged?"]
        
    option1 = ["Structured Query List","FLOAT","TRUNCATE","COMMIT and ROLLBACK","DELETE"]
    option2 = ["Structure Query Language","NUMERIC","ALTER","UPDATE and TRUNCATE","REMOVE"]
    option3 = ["Sample Query Language","DECIMAL","CREATE","SELECT and INSERT","DROP"]
    option4 = ["None of these.","CHARACTER","UPDATE","GRANT and REVOKE","TRUNCATE"]
    
    answers = [2,3,1,2,4]
    global i,var1,ans,btn_submit,btn
    ans = []
    i=0
    global q1,a1,a2,a3,a4
    def des():
        global q1,a1,a2,a3,a4,ans,btn
        b = var1.get()
        ans.append(b)
        q1.destroy()
        a1.destroy()
        a2.destroy()
        a3.destroy()
        a4.destroy()
        btn.destroy()
        next_ques()
            
            
    def next_ques():
        global i,q1,a1,a2,a3,a4,ans,btn_submit,btn
        def show():
            b = var1.get()
            ans.append(b)
            print(ans)
            score=0
            x=0
            j=0
            for j in range(len(answers)):
                if(ans[x] == answers[j]):
                    score = score+1
                x=x+1
            sql = "INSERT INTO paper(name,roll,fname,email,mobile,marks) VALUES ('%s','%s','%s','%s','%s','%d')" % (name,roll,fname,email,mobile,score)
            r = cursor.execute(sql)
            db.commit()
            if r: 
                messagebox.showinfo("Message","Your response is submitted.")
            else:
                messagebox.showinfo("Meassage","You have responded earlier.")
                
            score = str(score)
            q1.destroy()
            a1.destroy()
            a2.destroy()
            a3.destroy()
            a4.destroy()
            btn.destroy()
            btn_submit.destroy()
            a = Label(root,text="Your Score is: " + score + "/5", font = (font_for_label,15), bg=back).place(x=300,y=200)
                
        global var1
        var1 = IntVar()
        
        q1 = Label(root,text=arr[i],font=('Helvetica',15),bg=back)
        q1.place(x=50,y=100)
        a1 = Radiobutton(root, text = option1[i],font=('Helvetica',12),variable=var1,value=1,bg=back)
        a1.place(x=60,y=150)
        a2 = Radiobutton(root, text = option2[i],font=('Helvetica',12),variable=var1,value=2,bg=back)
        a2.place(x=60,y=180)
        a3 = Radiobutton(root, text = option3[i],font=('Helvetica',12),variable=var1,value=3,bg=back)
        a3.place(x=60,y=210)
        a4 = Radiobutton(root, text = option4[i],font=('Helvetica',12),variable=var1,value=4,bg=back)
        a4.place(x=60,y=240)
        btn = Button(root, text="Next",padx=35,pady=5,command = des)
        btn.place(x=400,y=350)
            
        if(i==4):
            btn.destroy()
            btn_submit = Button(root, text="Submit",padx=35,pady=5,command = show)
            btn_submit.place(x=400,y=350)
            
                 
        i=i+1
        
    next_ques()

btn_next = Button(root, text="Next", bg='brown',padx=35, pady=5,font=("Comic Sans MS",15) , command=cmd)
btn_next.place(x=580,y=400)

root.mainloop()
