from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector as  mys
import config
import pwd_hasher



def tglpwd(pin,pbtn):
    if pin.cget("show")=='':
        pin.config(show='*')
        image=PhotoImage(file="spwd_icon.png").subsample(15,15)
        pbtn.config(image=image)
        pbtn.image=image
    else:
        pin.config(show='')
        image=PhotoImage(file="hpwd.png").subsample(30,30)
        pbtn.config(image=image)
        pbtn.image=image
    
def signup():
    def store():
        name,pwd=uin.get(),pin.get()
        phash=pwd_hasher.pwd_hshr(pwd)
        con=config.dbconfig()
        cur=con.cursor()
        query="insert into user values('%s','%s')"%(name,phash)
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Account created")
        swin.destroy()
        
    #Sign-up window
    swin=Toplevel(root)
    swin.geometry("400x250")
    swin.title("Signup")
    swin.iconphoto(False,icon)
    ulbl=Label(swin,text="Username").place(x=50,y=60)
    
    uin=Entry(swin,width=30)
    uin.place(x=110,y=60)

    
    plbl=Label(swin,text="Pwd").place(x=50,y=90)
    pin=Entry(swin,show='*',width=30)
    pin.place(x=110,y=90)
    image=PhotoImage(file="spwd_icon.png").subsample(15,15)
    pbtn=Button(swin,image=image,command=lambda:tglpwd(pin,pbtn))
    pbtn.place(x=300,y=90)
    sbtn=Button(swin,text="Submit",command =store).place(x=110,y=120)
    swin.mainloop()

def addrcrd():
    ascr=Toplevel()
    ascr.geometry("400x250")
    ascr.title("Add Site")
    icon=PhotoImage(file="Lock.png")
    ascr.iconphoto(False,icon)
    site=
    

def uprcrd():
    pass

def delrcrd():
    pass

def logout(scr):
    scr.destroy()
    root.deiconify()

def end(scr):
    scr.destroy()
    root.destroy()

def pwd_screen():
    pscreen=Toplevel()
    s=Style()
    s.configure('fsty.TButton',font=("Arial",15))
    pscreen.geometry("800x600")
    root.title("Simple Password manager")
    icon=PhotoImage(file="Lock.png")
    root.iconphoto(False,icon)
    ptitle=Label(pscreen,text="Password Manager",font=("Helvetica",30))
    ptitle.place(x=275,y=50)
    addbtn=Button(pscreen,text="Add record",command=addrcrd,width=20,style="fsty.TButton")
    addbtn.place(x=0,y=30)
    upbtn=Button(pscreen,text="Update record",command=uprcrd,width=20,style="fsty.TButton")
    upbtn.place(x=0,y=75)
    delbtn=Button(pscreen,text="Delete",command=delrcrd,width=20,style="fsty.TButton")
    delbtn.place(x=0,y=120)
    lbtn=Button(pscreen,text="Logout",command=lambda: logout(pscreen),width=20,style="fsty.TButton")
    lbtn.place(x=0,y=525)
    qbtn=Button(pscreen,text="Exit",command=lambda: end(pscreen),width=20,style="fsty.TButton")
    qbtn.place(x=0,y=560)
    pscreen.mainloop()
    
def login():
    def verify():
        name,pwd=uin.get(),pin.get()
        con=config.dbconfig()
        cur=con.cursor()
        cur.execute("select * from user")
        data=cur.fetchall()
        for i in data:
            hash=i[1]
            chkr=pwd_hasher.check(hash,pwd)
            if name==i[0] and chkr==1:
                messagebox.showinfo("Login","Verification Success")
                lwin.destroy()
                root.withdraw()
                pwd_screen()
                break
            elif chkr==0:
                messagebox.showerror("Try again","wrong credentials")
                lwin.destroy()
                break
                           
    #login window
    lwin=Toplevel(root)
    lwin.geometry("400x250")
    lwin.title("Login")
    lwin.iconphoto(False,icon)
    ulbl=Label(lwin,text="Username").place(x=50,y=60)
    uin=Entry(lwin,width=30)
    uin.place(x=110,y=60)

    
    plbl=Label(lwin,text="Pwd").place(x=50,y=90)
    pin=Entry(lwin,show='*',width=30)
    pin.place(x=110,y=90)
    image=PhotoImage(file="spwd_icon.png").subsample(15,15)
    pbtn=Button(lwin,image=image,command=lambda:tglpwd(pin,pbtn))
    pbtn.place(x=300,y=90)
    wbtn=Button(lwin,text="login",command =verify).place(x=110,y=120)
    lwin.mainloop()
    
    
    
#main window    
root=Tk()
root.geometry("400x250")
root.title("Simple Password manager")
icon=PhotoImage(file="Lock.png")
root.iconphoto(False,icon)
lbl=Label(root,text="Simple Password manager").place(x=100,y=40)
"""ulbl=Label(root,text="Username").place(x=50,y=60)
uin=Entry(root,width=30).place(x=110,y=60)
plbl=Label(root,text="Pwd").place(x=50,y=90)
pin=Entry(root,show='*',width=30).place(x=110,y=90)"""

sbtn=Button(root,text="Sign-up",command =signup).place(x=110,y=60)
logbtn=Button(root,text="Log-in",command =login).place(x=110,y=90)
ebtn=Button(root,text="Exit",command =root.destroy).place(x=110,y=120)

root.mainloop()

