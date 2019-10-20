#=============================================================================================Project 3=============================================================================================
from tkinter import*
import random
import time;

root = Tk()
root.geometry('1603x630+0+0')
root.title('Cafe Management Systems')

text_Input = StringVar()
operator=''

Tops = Frame(root,width = 1600,height = 50,bg="gold",relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height = 700,relief=RAISED)
f1.pack(side=LEFT)


f2 = Frame(root,width = 300,height = 700,relief=RAISED)
f2.pack(side=RIGHT)
#================================================================================================Time===============================================================================================
localtime=time.asctime(time.localtime(time.time()))
#=================================================================================================Info==============================================================================================
lblInfo = Label(Tops , font=('arial',50,"bold"),text="Cafe Management Systems",fg="peru",bd=10,anchor="w")
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops , font=('arial',20,"bold"),text=localtime,fg="peru",bd=10,anchor="w")
lblInfo.grid(row=1,column=0)
#==============================================================================================Calculator===========================================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(1000,9999)
    randomRef = str(x)
    rand.set(randomRef)

    CoHe = float(He.get())
    CoFe = float(Fe.get())
    CoFc = float(Fc.get())
    CoHc = float(Hc.get())
    CoHch = float(Hch.get())
    CoCc = float(Cc.get())
    
    CostofHe = CoHe * 1.00
    CostofFe = CoFe * 2.50
    CostofFc = CoFc * 3.00
    CostofHc = CoHc * 2.00
    CostofHch = CoHch * 3.50
    CostofCc = CoCc * 2.00

    OrderCost = str('%.2f' % (CostofHe+CostofFe+CostofFc+CostofHc+CostofHch+CostofCc)),"€"

    PayTax = ((CostofHe+CostofFe+CostofFc+CostofHc+CostofHch+CostofCc)*0.2)

    TotalCost = (CostofHe+CostofFe+CostofFc+CostofHc+CostofHch+CostofCc)

    Ser_Charge = ((CostofHe+CostofFe+CostofFc+CostofHc+CostofHch+CostofCc)/99)

    Service = str('%.2f' % Ser_Charge),"€"

    OverAllCost = str('%.2f' % (PayTax + TotalCost + Ser_Charge)),"€"

    PaidTax =  str('%.2f' % PayTax),"€"

    Service_Charge.set(Service)
    Cost.set(OrderCost)
    Tax.set(PaidTax)
    SubTotal.set(OrderCost)
    Total.set(OverAllCost)
    



    
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    He.set("")
    Hc.set("")
    Fc.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Fe.set("")
    Tax.set("")
    Cost.set("")
    Hch.set("")
    Cc.set("")

txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=20,insertwidth=4,bg="antiquewhite",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="greenyellow", command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="greenyellow", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="greenyellow", command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="grey", command=lambda: btnClick("+")).grid(row=2,column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="greenyellow", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="greenyellow", command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="greenyellow", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="grey", command=lambda: btnClick("-")).grid(row=3,column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="greenyellow", command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="greenyellow", command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="greenyellow", command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="grey", command=lambda: btnClick("*")).grid(row=4,column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="greenyellow", command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="coral",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="gold",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="grey", command=lambda: btnClick("/")).grid(row=5,column=3)
#---------------------------------------------------------------------------------------Restaurant Info 1-------------------------------------------------------------------------------------------
rand=StringVar()
He = StringVar()
Hc = StringVar()
Fc = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Fe = StringVar()
Tax = StringVar()
Cost = StringVar()
Hch = StringVar()
Cc = StringVar()

lblOrderCode = Label(f1,font=('arial',16,'bold'),text="Order Code",bd=16,anchor="w")
lblOrderCode.grid(row=0,column=2)
txtOrderCode=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="snow",justify="right")
txtOrderCode.grid(row=0,column=3)

lblHe = Label(f1,font=('arial',16,'bold'),text="Hot Espresso",bd=16,anchor="w")
lblHe.grid(row=0,column=0)
txtHe=Entry(f1,font=('arial',16,'bold'),textvariable=He,bd=10,insertwidth=4,bg="snow",justify="right")
txtHe.grid(row=0,column=1)

lblHc = Label(f1,font=('arial',16,'bold'),text="Hot Cappuccino ",bd=16,anchor="w")
lblHc.grid(row=2,column=0)
txtHc=Entry(f1,font=('arial',16,'bold'),textvariable=Hc,bd=10,insertwidth=4,bg="snow",justify="right")
txtHc.grid(row=2,column=1)

lblFc = Label(f1,font=('arial',16,'bold'),text="Freddo Cappuccino",bd=16,anchor="w")
lblFc.grid(row=3,column=0)
txtFc=Entry(f1,font=('arial',16,'bold'),textvariable=Fc,bd=10,insertwidth=4,bg="snow",justify="right")
txtFc.grid(row=3,column=1)

lblHch = Label(f1,font=('arial',16,'bold'),text="Hot Chocolate",bd=16,anchor="w")
lblHch.grid(row=4,column=0)
txtHch=Entry(f1,font=('arial',16,'bold'),textvariable=Hch,bd=10,insertwidth=4,bg="snow",justify="right")
txtHch.grid(row=4,column=1)

lblCc = Label(f1,font=('arial',16,'bold'),text="Cold Chocolate",bd=16,anchor="w")
lblCc.grid(row=5,column=0)
txtCc=Entry(f1,font=('arial',16,'bold'),textvariable=Cc,bd=10,insertwidth=4,bg="snow",justify="right")
txtCc.grid(row=5,column=1)

#---------------------------------------------------------------------------------------Restaurant Info 2-------------------------------------------------------------------------------------------
lblFe = Label(f1,font=('arial',16,'bold'),text="Freddo Espresso",bd=16,anchor="w")
lblFe.grid(row=1,column=0)
txtFe=Entry(f1,font=('arial',16,'bold'),textvariable=Fe,bd=10,insertwidth=4,bg="snow",justify="right")
txtFe.grid(row=1,column=1)

lblCost = Label(f1,font=('arial',16,'bold'),text="Order Cost",bd=16,anchor="w")
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="snow",justify="right")
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="snow",justify="right")
txtService.grid(row=2,column=3)

lblStateTax = Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="snow",justify="right")
txtStateTax.grid(row=3,column=3)

lblsubTotal = Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor="w")
lblsubTotal.grid(row=4,column=2)
txtsubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="snow",justify="right")
txtsubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total
                   ,bd=10,insertwidth=4,bg="snow",justify="right")
txtTotalCost.grid(row=5,column=3)

#==============================================================================================Buttons===========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",16,"bold"),width=10,text="Total",bg="powder blue",command = Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",16,"bold"),width=10,text="Reset",bg="green",command = Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("arial",16,"bold"),width=10,text="Exit",bg="red",command = qExit).grid(row=7,column=3)


root.mainloop()
