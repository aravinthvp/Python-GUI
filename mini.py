from tkinter import*
import random
import time;
#==================================Root==============================================================
root = Tk()
root.geometry("1600x800+0+0")
root.title("shoes Management System")
#=================================Frame==============================================================
text_Input = StringVar()
operator =""

Tops =Frame(root, width=1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height =700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height =700,relief=SUNKEN)
f2.pack(side=RIGHT)

#================================Time================================================================
localtime=time.asctime(time.localtime(time.time()))
#================================Info================================================================
lblInfo = Label(Tops,font=('arial',50,'bold'),text="shoes Management System",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops,font=('arial',50,'bold'),text=localtime,fg="Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#================================calculator==========================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(12908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoR =float(Nike.get())
    CoI =float(Tommy.get())
    CoD =float(Woodland.get())
    CoP =float(AllStars.get())
    CoC =float(Puma.get())
    CoM =float(Adidas.get())

    CostofNike = CoR * 30
    CostofTommy = CoI * 5
    CostofWoodland = CoD * 10
    CostofAllStars = CoP * 10
    CostofPuma = CoC * 10
    CostofAdidas = CoM * 20



    CostofMeal = "र", str('%.2f' %(CostofNike + CostofTommy + CostofWoodland + CostofAllStars + CostofPuma +
                                  CostofAdidas))

    PayTax =((CostofNike + CostofTommy + CostofWoodland + CostofAllStars + CostofPuma +
                                  CostofAdidas) * 0.2)
    TotalCost = (CostofNike + CostofTommy + CostofWoodland + CostofAllStars + CostofPuma +
                                  CostofAdidas)
    Ser_Charge = ((CostofNike + CostofTommy + CostofWoodland + CostofAllStars + CostofPuma +
                                  CostofAdidas)/99)
    Services = "र", str('%.2f' % Ser_Charge)

    OverAllCost =  "र", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    
    PaidTax = "र", str('%.2f' % PayTax)


    Service.set(Services)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(Ser_Charge)
    Total.set(OverAllCost)
    
    
def qExit():
    root.destroy()
    
def Reset():
    rand.set("")
    Nike.set("")
    Tommy.set("")
    Woodland.set("")
    AllStars.set("")
    Puma.set("")
    Adidas.set("")
    Service.set("")
    Cost.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")

#================================================================================================================
txtDisplay =Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,
                  bg="light green",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="7", bg="light green", command=lambda: btnClick(7)).grid(row=2,column=0)
btn8 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="8", bg="light green", command=lambda: btnClick(8)).grid(row=2,column=1)
btn9 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="9", bg="light green", command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
                text="+", bg="light green", command=lambda: btnClick("+")).grid(row=2,column=3)
#-----------------------------------------------------------------------------------------------------------
btn4 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="4", bg="light green", command=lambda: btnClick(4)).grid(row=3,column=0)
btn5 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="5", bg="light green", command=lambda: btnClick(5)).grid(row=3,column=1)
btn6 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="6", bg="light green",
             command=lambda: btnClick(6)).grid(row=3,column=2)
Subraction=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="-", bg="light green", command=lambda: btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------
btn1 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="1", bg="light green", command=lambda: btnClick(1)).grid(row=4,column=0)
btn2 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="2", bg="light green", command=lambda: btnClick(2)).grid(row=4,column=1)
btn3 =Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="3", bg="light green", command=lambda: btnClick(3)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="*", bg="light green", command=lambda: btnClick("*")).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------------------
btn0= Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="0", bg="light green", command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
                text="C", bg ="light green",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
                 text="=", bg="light green",comman=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
             text="/", bg="light green", command=lambda: btnClick("/")).grid(row=5,column=3)
#-------------------------------------CAR INFO 1------------------------------------------------------------
rand=StringVar()
Nike=StringVar()
Tommy=StringVar()
Woodland=StringVar()
AllStars=StringVar()
Puma=StringVar()
Adidas=StringVar()
Service=StringVar()
Cost=StringVar()
Tax=StringVar()
SubTotal=StringVar()
Total=StringVar()
lblReference =Label(f1, font=('arial',16,'bold'), text="Reference", bd=16 ,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1, font=('arial',16,'bold'), textvariable=rand, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtReference.grid(row=0,column=1)
lblNike =Label(f1, font=('arial',16,'bold'), text=" Nike", bd=16 ,anchor='w')
lblNike.grid(row=1,column=0)
txtNike=Entry(f1, font=('arial',16,'bold'), textvariable=Nike, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtNike.grid(row=1,column=1)
lblTommy =Label(f1, font=('arial',16,'bold'), text="Tommy", bd=16 ,anchor='w')
lblTommy.grid(row=2,column=0)
txtTommy=Entry(f1, font=('arial',16,'bold'), textvariable=Tommy, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtTommy.grid(row=2,column=1)
lblWoodland =Label(f1, font=('arial',16,'bold'), text="Woodland", bd=16 ,anchor='w')
lblWoodland.grid(row=3,column=0)
txtWoodland=Entry(f1, font=('arial',16,'bold'), textvariable=Woodland, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtWoodland.grid(row=3,column=1)
lblAllStars =Label(f1, font=('arial',16,'bold'), text="AllStars", bd=16 ,anchor='w')
lblAllStars.grid(row=4,column=0)
txtAllStars=Entry(f1, font=('arial',16,'bold'), textvariable=AllStars, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtAllStars.grid(row=4,column=1)
lblPuma =Label(f1, font=('arial',16,'bold'), text="Puma", bd=16 ,anchor='w')
lblPuma.grid(row=5,column=0)
txtPuma=Entry(f1, font=('arial',16,'bold'), textvariable=Puma, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtPuma.grid(row=5,column=1)
#-------------------------------------CAR INFO 2------------------------------------------------------------
lblAdidas =Label(f1, font=('arial',16,'bold'), text="Adidas", bd=16 ,anchor='w')
lblAdidas.grid(row=0,column=2)
txtAdidas=Entry(f1, font=('arial',16,'bold'), textvariable=Adidas, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtAdidas.grid(row=0,column=3)
lblMilks =Label(f1, font=('arial',16,'bold'), text="Service", bd=16 ,anchor='w')
lblMilks.grid(row=1,column=2)
txtMilks=Entry(f1, font=('arial',16,'bold'), textvariable=Service, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtMilks.grid(row=1,column=3)
lblOnions =Label(f1, font=('arial',16,'bold'), text="Cost", bd=16 ,anchor='w')
lblOnions.grid(row=2,column=2)
txtOnions=Entry(f1, font=('arial',16,'bold'), textvariable=Cost, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtOnions.grid(row=2,column=3)
lblChicken =Label(f1, font=('arial',16,'bold'), text="Tax", bd=16 ,anchor='w')
lblChicken.grid(row=3,column=2)
txtChicken=Entry(f1, font=('arial',16,'bold'), textvariable=Tax, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtChicken.grid(row=3,column=3)
lblApple =Label(f1, font=('arial',16,'bold'), text="SubTotal", bd=16 ,anchor='w')
lblApple.grid(row=4,column=2)
txtApple=Entry(f1, font=('arial',16,'bold'), textvariable=SubTotal, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtApple.grid(row=4,column=3)
lblOrange =Label(f1, font=('arial',16,'bold'), text="Total ", bd=16 ,anchor='w')
lblOrange.grid(row=5,column=2)
txtOrange=Entry(f1, font=('arial',16,'bold'), textvariable=Total, bd=10 ,insertwidth=4,
                    bg="light green",justify = 'right')
txtOrange.grid(row=5,column=3)
#-----------------------------------Button-----------------------------------------
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Total",bg="light green",command =Ref).grid(row=7,column=1)
btnqExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Exit",bg="light green",command =qExit).grid(row=7,column=2)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Reset",bg="light green",command =Reset).grid(row=7,column=3)
root.mainloop()
