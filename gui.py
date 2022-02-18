from tkinter import *
GUI = Tk()
from tkinter import ttk, messagebox

friend ={'card':'กฤษณะ สุริยารังสรรค์',
        'new':'ไอ้นิว',
        'cream':'ณุทยา หงส์ทอง'}

GUI.title("Card's program")
GUI.geometry('500x300')

L= Label(GUI,text='Nickname?').pack(pady=20)
v_text=StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text,font=('Angsana New',20))
E1.pack()

def Click():
    text=v_text.get() #ดึงข้อความที่userพิมพ์
    print('Nickname :', text)
    if text.lower() =='Cream':
        result = friend[text]
        messagebox.showinfo('Result','ชื่อเล่น{} เป็นแฟนของCard'.format(text))
        print('Name :', friend[text])
    elif text.lower() in friend.keys():
        result = friend[text]
        messagebox.showinfo('Result','ชื่อเล่น{} เป็นชื่อของ{}'.format(text,result))
        print('Name :', friend[text])
    else:
        print('No data')
        messagebox.showinfo('Result:Error','No data')

B1=ttk.Button(GUI,text='Yes',command=Click)
B1.pack(ipadx=20,ipady=10,pady=30,padx=30)
GUI.mainloop()
























