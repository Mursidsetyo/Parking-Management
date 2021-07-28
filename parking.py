from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    nomor = e_id.get()
    plat = Entryplat.get()

    if(nomor=="" or plat==""):
        MessageBox.showinfo("Insert status", "All fields are reqiuired")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="",database="parking")
        cursor1 = con.cursor()
        cursor1.execute("insert into data values('"+  nomor  +"','"+ plat +"')")
        cursor1.execute("commit")

        e_id.delete(0, 'end')
        Entryplat.delete(0, 'end')
        MessageBox.showinfo("Status ", "Masuk ")
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", passwd="",database="parking")
    cursor1 = con.cursor()
    cursor1.execute("select * from data")
    rows = cursor1.fetchall()

    for row in rows:
        insertData = str(row[0])+ '  '+ row[1]
        list.insert(list.size()+1, insertData)

    con.close()

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete status", "Deleted unsuccesful")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="",database="parking")
        cursor1 = con.cursor()
        cursor1.execute("delete from data where nomor='"+ e_id.get() +"'")
        cursor1.execute("commit")

        e_id.delete(0, 'end')
        Entryplat.delete(0, 'end')
        MessageBox.showinfo("Status ", "Keluar ")
        con.close()


root =Tk()
root.geometry("600x400")
root.title("Parking Management")
root.configure(background='black')
Tops = Frame(root,bg='black',bd=5,pady=2,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=('Times',23),text='Parking Management',bd=10,bg='white',justify=CENTER,width= 15)
lblTitle.grid(row=0)

var = StringVar()
label = Label( root, textvariable=var,font=('Times',10),bd=7,relief=FLAT )
var.set("No.Parkir")
label.place(x=20, y=100)

var = StringVar()
label = Label( root, textvariable=var,font=('Times',10),bd=7, relief=FLAT )
var.set("Plat Kendaraan")
label.place(x=20, y=140)

var = StringVar()
Entryplat = Entry( root, textvariable=var,font=('Times',10,'bold'),bd=7, width=30, relief=SUNKEN )
Entryplat.place(x=150, y=140)

var = StringVar()
e_id = Entry( root, textvariable=var,font=('Times',10,'bold'),bd=7, width=30, relief=SUNKEN )
e_id.place(x=150, y=100)

Masuk = Button(root, text="MASUK",font=('Times',8,),bd=4,relief=RAISED,command=insert)
Masuk.place(x=150,y=175)

kluar = Button(root, text="KELUAR",font=('Times',8,),bd=4,relief=RAISED,command=delete)
kluar.place(x=210,y=175)


list = Listbox(root, width=31,height=12) 
list.place(x=400, y=100)
show()



root.mainloop()