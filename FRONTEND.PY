def addstudent():
    def submitadd():
        id= idval.get()
        name= nameval.get()
        mobile= mobileval.get()
        email=emailval.get()
        address=addressval.get()
        dob= dobval.get() 
        gender= genderval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        print('added')
        try:
            strr='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notifications','Id{} Name{} Added sucessfully.. and want to clear the form',parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                dobval.set('')
                genderval.set('')  
        except:
            messagebox.showerror('Notifications','Id already exist try another Id...',parent=addroot)
        strr='select* from studentdata1'
        mycursor.execute(strr)
        data=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='darkblue')
    addroot.resizable(False,False)


    ###################add student label
    idlabel=Label(addroot,text='Enter Id:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Enter Name:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Enter Mobile No.:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Enter Email:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Enter Address:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    doblabel=Label(addroot,text='Enter D.O.B :', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    doblabel.place(x=10,y=310)
 
    genderlabel=Label(addroot,text='Enter Gender:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    genderlabel.place(x=10,y=370)
####################3add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()
    genderval=StringVar()

    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
  
    addressentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    dobentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)
 
    genderentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=370)


    #########3##############add button
    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='white',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()
      

def searchstudent():
    def search():
        print('found')
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='darkblue')
    searchroot.resizable(False,False)


    ###################add student label
    idlabel=Label(searchroot,text='Enter Id:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(searchroot,text='Enter Name:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(searchroot,text='Enter Mobile No.:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(searchroot,text='Enter Email:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(searchroot,text='Enter Address:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    doblabel=Label(searchroot,text='Enter D.O.B :', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    doblabel.place(x=10,y=310)
 
    genderlabel=Label(searchroot,text='Enter Gender:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    genderlabel.place(x=10,y=370)

    datelabel=Label(searchroot,text='Enter Date:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    datelabel.place(x=10,y=430)
####################3add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()
    genderval=StringVar()
    dateval=StringVar()

    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
  
    addressentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)
 
    genderentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=370)

    dateentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)




    #########3##############add button
    searchbtn=Button(searchroot,text='Search',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='white',command=search)
    searchbtn.place(x=150,y=480)

    searchroot.mainloop
    

def deletestudent():
    print('student deleted')


def updatestudent():
    def update():
        print('found')
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='darkblue')
    updateroot.resizable(False,False)


    ###################add student label
    idlabel=Label(updateroot,text='Enter Id:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Enter Name:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Enter Mobile No.:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Enter Email:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Enter Address:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    doblabel=Label(updateroot,text='Enter D.O.B :', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    doblabel.place(x=10,y=310)
 
    genderlabel=Label(updateroot,text='Enter Gender:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    genderlabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Enter Date:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot,text='Enter Time:', bg='lightgray',font=('times',20,'bold'),borderwidth=3,relief=GROOVE,width=12,anchor='w')
    timelabel.place(x=10,y=490)
####################3add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()
    genderval=StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
  
    addressentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    dobentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)
 
    genderentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=370)

    dateentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
 
    timeentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)




    #########3##############add button
    updatebtn=Button(updateroot,text='Update',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='white',command=update)
    updatebtn.place(x=150,y=540)

    updateroot.mainloop
    


    
    
def showstudent():
    print('student show')

def exportstudent():
    print('student exported')

def exitstudent():
    result = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(result==True):
        root.destroy()
    



















#####################3databaseconnection
def connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        print(host,user,password)
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            strr='create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id in primary key '
            mycursor.execute(strr)
            strr='create table studentdata1.studentmanagementsystem1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            
        
        
        except:
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            #strr='create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'
            #mycursor.execute(strr)
            #strr='alter table studentdata1 modify column id int not null'
            #mycursor.execute(strr)
           # strr='alter table studentdata1 modify column id in primary key '
            #mycursor.execute(strr)
            messagebox.showinfo('Notification','You are connected to database')
        dbroot.destroy()
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='darkblue')
    ########################connectdb labels
    hostlabel=Label(dbroot,text="Enter host:",bg='lightgray',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel=Label(dbroot,text="Enter user:",bg='lightgray',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel=Label(dbroot,text="Enter password:",bg='lightgray',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10,y=130)

    ######################33connectdb entry
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()

    hostentry=Entry(dbroot,font=('romen',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=220,y=10)
    userentry=Entry(dbroot,font=('romen',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=220,y=70)
    passwordentry=Entry(dbroot,font=('romen',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=220,y=130)

##################submitbutton
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='darkviolet',command=submitdb)
    submitbutton.place(x= 150,y=190)



    dbroot.mainloop()









def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text='Date:' + date_string+'\n'+'Time:'+ time_string)
    clock.after(200,tick)   

###############  strftime  places the current time
####################intro sllider
import random
colors=['red','pink','green','purple','yellow','blue']
def introlabelcolortick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20,introlabelcolortick)





def IntroLabelTick():
     global count,text
     if(count>=len(ss)):
         count=0
         text= ''
         SliderLabel.config(text=text)
     else:
          text=text+ss[count]
          SliderLabel.config(text=text)
          count+= 1
################ after function to call this function again and again after a given time
     SliderLabel.after(200,IntroLabelTick)   
        

##############################

import random
    
from tkinter import*

from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root=Tk()
root.title('Student Management System')
root.config(bg='royalblue')
root.geometry('1174x700+200+50')
root.resizable(False,False)
######################################## frames
##################frame1
DataEntryFrame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel=Label(DataEntryFrame,text='------------WELCOME------------',width=30,font=('arial',22,'italic bold'),bg='yellow')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryFrame,text='5. Show All Student',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export data',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='aqua',relief=RIDGE,activebackground='blue',activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
#############frame2
DatabaseFrame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DatabaseFrame.place(x=550,y=80,width=620,height=600)


#####################-------showdataframe
style=ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='springgreen')

scroll_x=Scrollbar(DatabaseFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(DatabaseFrame,orient=VERTICAL)




studenttable=Treeview(DatabaseFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=150)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)

studenttable.pack(fill=BOTH,expand=1)










###################################################SLIDER
ss='Welcome To Student Management System'
count=0
text=''
#######################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,bg='cyan',width=35)
SliderLabel.place(x=260,y=0)
IntroLabelTick()
introlabelcolortick()
####################################CLOCK
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='springgreen')
clock.place(x=0,y=0)

tick()
#################################connectdatabasebutton
connectbutton=Button(root,text='Connect To Database',width=23,bg='white',activebackground='pink',command=connectdb)
connectbutton.place(x=930,y=0)

root.mainloop()