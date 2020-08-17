#Schedule Maker plus BMI calculator!

#Importing tkinter.
from tkinter import *

# Class named Application which inherits from Frame.
class Application(Frame):

    def __init__(self,master):

        # calling super class inorder to set master to it.
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()
        #Class variables.
        self.tim=""  
        self.hlt=""
        self.name="Emplty field!"
        self.age="Empty field!"
        self.height="45"
        self.weight="45"
        self.bmi="Height or weight not recieved!"
        self.gend="Not selected!"
        self.cnt=0
        self.agg=False
        self.schedule=""
        self.r=0
        self.c1=0
        self.c2=0
        self.c3=0
        self.c4=0
        self.c5=0
        self.alph=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","!","#","$","@","%","^","&","*","(",")","'",'"',"<",">","?","/","}","{","[","]","\",","|","_","-",":",";","=","+"]

    #Function which will craeate all the widgets.
    #row=0
    def create_widget(self):
        self.r=0
        self.lbl1=Label(self,text="\t\t\tGet your daily workout plan!\n")
        self.lbl1.grid(row=self.r, column=0, columnspan=2, sticky='w')

        #Name with Entry box.
        #row=2
        self.r+=2
        self.lbl2=Label(self,text="Name : ")
        self.lbl2.grid(row=self.r,column=0,columnspan=1,sticky='w')
        self.nm_txt=Entry(self)
        self.nm_txt.grid(row=self.r, column=1,columnspan=4,sticky='w')

        #Age with Entry box.
        #row=3
        self.r+=1
        self.lbl3=Label(self,text="Age : ")
        self.lbl3.grid(row=self.r,column=0,columnspan=1,sticky='w')
        self.ag_txt=Entry(self)
        self.ag_txt.grid(row=self.r, column=1,columnspan=4,sticky='w')
        self.lbl13=Label(self,text="(yrs)")
        self.lbl13.grid(row=self.r,column=2,sticky='w')

        #Gender with radio buttons.
        #row=4
        self.r+=1
        self.lbl3=Label(self,text="Gender : ")
        self.lbl3.grid(row=self.r,column=0,columnspan=1,sticky='w')
        #Variable to store radio button's value.
        self.gn=StringVar()
        self.gn.set("Not selected!")
        Radiobutton(self,text="Male",value="Male",variable=self.gn).grid(row=self.r,column=1,sticky='w')
        Radiobutton(self,text="Female",value="Female",variable=self.gn).grid(row=self.r,column=2,sticky='w')

        #Height with Entry box.
        #row=5
        self.r+=1
        self.lbl8=Label(self,text="Height : ")
        self.lbl8.grid(row=self.r,column=0,columnspan=1,sticky='w')
        self.hg_txt=Entry(self)
        self.hg_txt.grid(row=self.r,column=1,columnspan=4,sticky='w')
        self.lbl11=Label(self,text="(cm)")
        self.lbl11.grid(row=self.r,column=2,sticky='w')

        #Weight with Entry box.
        #row=6
        self.r+=1
        self.lbl9=Label(self,text="Weight : ")
        self.lbl9.grid(row=self.r,column=0,columnspan=1,sticky='w')
        self.wg_txt=Entry(self)
        self.wg_txt.grid(row=self.r,column=1,columnspan=4,sticky='w')
        self.lbl12=Label(self,text="(Kg)")
        self.lbl12.grid(row=self.r,column=2,sticky='w')
        
        #row=7
        self.r+=1
        self.lbl5=Label(self,text="Select exercises:")
        self.lbl5.grid(row=self.r, column=0,sticky='w')

        #Check button for cycling.
        #row=9
        self.r+=2
        self.c1=self.r
        self.cycl=BooleanVar()
        Checkbutton(self,text="Cycling  ",variable=self.cycl).grid(row=self.c1,column=0,sticky='w')

        #Check button for running.
        #row=10
        self.r+=1
        self.c2=self.r
        self.run=BooleanVar()
        Checkbutton(self,text="Running  ",variable=self.run).grid(row=self.c2,column=0,sticky='w')

        #Check button for swimming.
        #row=11
        self.r+=1
        self.c3=self.r
        self.swim=BooleanVar()
        Checkbutton(self,text="Swimming ",variable=self.swim).grid(row=self.c3,column=0,sticky='w')

        #Check button for jumping.
        #row=12
        self.r+=1
        self.c4=self.r
        self.jump=BooleanVar()
        Checkbutton(self,text="Jumping  ",variable=self.jump).grid(row=self.c4,column=0,sticky='w')

        #Check button for skipping.
        #row=13
        self.r+=1
        self.c5=self.r
        self.skip=BooleanVar()
        Checkbutton(self,text="Skipping  ",variable=self.skip).grid(row=self.c5,column=0,sticky='w')

        #row=14
        self.r+=1
        self.lbl6=Label(self,text="Select time for each exercise :")
        self.lbl6.grid(row=self.r, column=0,sticky='w')

        #Variable to store radio button's value.
        self.time=StringVar()
        self.time.set(None)

        #Radiobuttons for time.
        Radiobutton(self,text="1hr ",variable=self.time,value="1hr ").grid(row=self.r, column=1,sticky='e')
        Radiobutton(self,text="1.5hrs ",variable=self.time,value="1.5hrs ").grid(row=self.r, column=2,sticky='e')
        Radiobutton(self,text="2hrs ",variable=self.time,value="2hrs ").grid(row=self.r, column=3,sticky='e')
        Radiobutton(self,text="2.5hrs ",variable=self.time,value="2.5hrs ").grid(row=self.r, column=4,sticky='e')

        #Submit and reset button.
        #row=16
        self.r+=2
        Button(self,text="Submit",command=self.sch).grid(row=self.r,column=1,sticky='w')
        Button(self,text="Reset",command=self.res).grid(row=self.r,column=1,sticky='e')

        #Text box for all the output.
        #row=17
        self.r+=1
        self.txt=Text(self,width=60,height=25,wrap=WORD)
        self.txt.grid(row=self.r,column=0,columnspan=12)

    #Function for Reset button.
    def res(self):

        #Setting back everything to its first(originally assigned) value.
        #Text box-
        self.txt.delete(0.0,END)

        #Entry boxes-
        self.nm_txt.delete(0,20)
        self.ag_txt.delete(0,20)
        self.hg_txt.delete(0,20)
        self.wg_txt.delete(0,20)
        
        #Radio buttons-
        self.time.set(None)
        self.gn.set(None)
        
        #Check buttons-
        self.cycl=BooleanVar()
        Checkbutton(self,text="Cycling  ",variable=self.cycl).grid(row=self.c1,column=0,sticky='w')
        self.run=BooleanVar()
        Checkbutton(self,text="Running  ",variable=self.run).grid(row=self.c2,column=0,sticky='w')
        self.swim=BooleanVar()
        Checkbutton(self,text="Swimming ",variable=self.swim).grid(row=self.c3,column=0,sticky='w')
        self.jump=BooleanVar()
        Checkbutton(self,text="Jumping  ",variable=self.jump).grid(row=self.c4,column=0,sticky='w')
        self.skip=BooleanVar()
        Checkbutton(self,text="Skipping  ",variable=self.skip).grid(row=self.c5,column=0,sticky='w')

        

        #Class variables-
        self.hlt=""
        self.row=0
        self.c1=0
        self.c2=0
        self.c3=0
        self.c4=0
        self.c5=0
        self.create_widget()
        self.name="Emplty field!"
        self.age="Empty field!"
        self.height="45"
        self.weight="45"
        self.bmi="Height or weight not recieved!"
        self.gend="Not selected!"
        self.cnt=0
        self.schedule=""
        self.tim=""
        self.alph=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","!","#","$","@","%","^","&","*","(",")","'",'"',"<",">","?","/","}","{","[","]","\",","|","_","-",":",";","=","+"]
        self.agg=False
        
    #Function for submit button.
    def sch(self):
        
        self.gend=self.gn.get()
        if self.time.get()!=None:
            self.tim=self.time.get()

        #Checking if name value is correct.
        if self.nm_txt.get()!="":
            self.name=str(self.name)
            self.name=self.nm_txt.get()
            self.name=str(self.name)

        #Checking if age value is correct.
        if self.ag_txt.get()!="":
            self.age=str(self.age)
            self.age=self.ag_txt.get()
            self.age=str(self.age)
        if self.age=="0":
            self.age="Age cannot be 0!"
        self.age=str(self.age)
        for i in self.alph:
            if i in self.age:
                self.agg=True
                self.age="Age cannot be 0 and cannot have alphabets!"
                break

        if not(self.agg):
            self.age=int(self.age)
            if self.age<0:
                self.age="Age canot be negative!"
        self.age=str(self.age)
        

        #Checking if height and weight value is correct and handelling different exceptions.
        try: 
            
            if self.hg_txt.get()!="" and self.wg_txt.get()!="":
                self.height=self.hg_txt.get()
                self.height=float(self.height)
                self.weight=self.wg_txt.get()
                self.weight=float(self.weight)
                try:
                    self.bmi=(self.weight/(self.height**2))*10000
                except ZeroDivisionError:
                    self.bmi="Division by zero is not possible!"
                if self.height==0:
                    self.bmi=0
                if self.bmi<20 and self.bmi>10:
                    self.hlt="You are Underweight!!!"
                elif self.bmi>=20 and self.bmi<25:
                    self.hlt="You are Healthy :)"
                elif self.bmi>=25 and self.bmi<30:
                    self.hlt="You are Overweight!"
                elif self.bmi>=30:
                    self.hlt="You are Obese!!!"
                if self.height==0:
                    self.bmi="Division by zero is not possible!"
                if self.height<0 or self.weight<0:
                    self.bmi="Height or weight cannot be negative!"
        except ValueError:
            self.bmi="You didn't enter a number!"

        #Checking Checkbuttons.
        if self.cycl.get():
            self.cnt+=1
            self.schedule+=str(self.cnt)+". Cycling - "+self.tim+"\n"
        if self.run.get():
            self.cnt+=1
            self.schedule+=str(self.cnt)+". Running - "+self.tim+"\n"
        if self.swim.get():
            self.cnt+=1
            self.schedule+=str(self.cnt)+". Swimming - "+self.tim+"\n"
        if self.jump.get():
            self.cnt+=1
            self.schedule+=str(self.cnt)+". Jumping - "+self.tim+"\n"
        if self.skip.get():
            self.cnt+=1
            self.schedule+=str(self.cnt)+". Skipping - "+self.tim+"\n"
        
        #Deleting anything before in the text box.
        self.txt.delete(0.0,END)
        
        #Inserting text in text box
        self.txt.insert(0.0,"\t\t\tDaily schedule\n\n")
        self.txt.insert(3.0,"Name : "+self.name+"\n\n")
        self.txt.insert(4.0,"Gender : "+self.gend+"\n")
        self.txt.insert(5.0,"Age : "+self.age+"\n\n")
        self.txt.insert(6.0,"BMI : "+str(self.bmi)+"\n")
        self.txt.insert(7.0,self.hlt+"\n")
        self.txt.insert(9.0,"Here is your daily schedule:\n\n")
        if not(self.cycl.get()) and not(self.run.get()) and not(self.swim.get()) and not(self.jump.get()) and not(self.skip.get()):
            self.txt.insert(11.0,"You didn't select anything!")
        self.txt.insert(11.0,self.schedule)
        

#Main Loop
root=Tk()
root.title("Exercise schedule maker")
root.geometry("485x650")

#Object of Application class.
app=Application(root)

#Starting the application.
root.mainloop()
