# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Uncle Engineer')
GUI.geometry('720x700+500+50')

'''
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [50, 20] },}})

style.theme_use("MyStyle")
'''
menubar = Menu(GUI)
GUI.config(menu=menubar)

################File menu###########
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='export to ...')

################help menu###########
def Abouts():
    messagebox.showinfo('About','เป็นโปรแกรมทดลอง\nจัดทำโดย\nมอส')

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='About',command=Abouts)

################help menu###########
donatemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate')
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

expenseicon = PhotoImage(file='expense.png')
listicon = PhotoImage(file='list.png')



'''
# f'{"tab short": ^50s}
# f'{"tab longgggggggggg": ^50s}'

https://stackoverflow.com/questions/8450472/how-to-print-a-string-at-a-fixed-width
https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
>>> f'{"HELLO": <{20}}'
'HELLO               '
>>> f'{"HELLO": >{20}}'
'               HELLO'
>>> f'{"HELLO": ^{20}}'
'       HELLO        '
'''

Tab.add(T1, text=f'{"Add Expense": ^50s}', image=expenseicon,compound='top')
Tab.add(T2, text=f'{"Expense List": ^50s}', image=listicon,compound='top')
#Tab.add(T2, text='Expense List', image=listicon,compound='top')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

F1 = Frame(T1)
F1.pack()

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    try:
        total = int(price) * int(quantity)
        # .get() คือดึงค่ามาจาก v_expense = StringVar()
        print('รายการ: {} ราคา: {}'.format(expense,price))
        print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
        v_result.set(text)
        # clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

        # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
        print(today)
        stamp =datetime.now()
        dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
        transactionid = stamp.strftime('%Y%m%d%H%M%f')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [transactionid,dt,expense,price,quantity,total]
            fw.writerow(data)

        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        update_table()
        E1.focus()

    except:
        print('ERROR')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'


centerimg = PhotoImage(file='wallet.png')
logo = ttk.Label(F1,image=centerimg)
logo.pack()


#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

saveicon = PhotoImage(file='save.png')

B2 = ttk.Button(F1,text='Save',command=Save,image=saveicon,compound='left')
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('-----ผลลัพธ์-----')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)

############TAB2########

def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
        #print(data)
        #print('--------')
        #print(data[1][0])
    return data

#table
header = ['รหัสรายการ','วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,column=header,show='headings',height=10)
resulttable.pack()
for hd in header:
    resulttable.heading(hd,text=hd)

headerwidth = [120,150,170,80,80,80]
for hd,w in zip (header,headerwidth):
    resulttable.column(hd,width=w)


alltransaction = {}

def UpdateCSV():
    with open('savedata.csv','w',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = list(alltransaction.values())
            fw.writerows(data)
            print('Table was updated')
            


def DeleteRecord(event=None):
    check = messagebox.askyesno('Confirm?','คุณต้องการลบข้อมูล?')
    if check == True:
        print('Record deleted')
        select = resulttable.selection()
        data = resulttable.item(select)
        data = data['values']
        transactionid = data[0]
        del alltransaction[str(transactionid)]
        UpdateCSV()
        update_table()
    else :
        print ('Cancel')

BDelete = ttk.Button(T2,text="Delete",command=DeleteRecord)
BDelete.place(x=50,y=550)


resulttable.bind('<Delete>',DeleteRecord)



def update_table():
    resulttable.delete(*resulttable.get_children())
    try:
        data = read_csv()
        for d in data:
            alltransaction[d[0]]=d
            resulttable.insert('',0,value=d)
    except:
        print('no file')

update_table()

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
