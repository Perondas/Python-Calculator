from sys import exit
import math
Numbers=["1","2","3","4","5","6","7","8","9","0"]
Functions=["*","/","^","§","(",")","-","!"]
def listint(list1):
        int1=0
        result=0
        comma=0
        int2=0
        
        for x in range(0,len(list1)):
                if list1[x]=="." or comma==1:
                    comma=1
                    if list1[x] != ".":
                        int2=(int(list1[x])*(0.1**(x-1)))
                        int1=int1+(int2)
                    else:
                        int1=int1/10**(len(list1)-x)
                else:
                    int1=int1+((int(list1[x])*(10**(len(list1)-x))))/10
        result=int1
        return(result)
def calc(list1):
    x=0
    pwr=0
    rad=0
    isdone=0
    answer=0
    while(isdone==0):
        if x <= (len(list1)-1):
            if list1[x]=="+":
                del(list1[x])
                x=0
            if list1[x]=="(":
                del(list1[x])
                x=0
            if list1[x]==")":
                del(list1[x])
                x=0
        else:
            isdone=1
        x=x+1
    isdone=0
    x=0
    while(isdone==0):
        if x <= (len(list1)-1):
            if list1[x]=="-" and list1[x+1]=="-":
                del(list1[x])
                del(list1[x])
                x=0
            elif list1[x]=="-":
                list1[x+1]=list1[x+1]*-1
                del(list1[x])
                x=0
        else:
            isdone=1
        x=x+1
    isdone=0
    x=0
    fact=0
    while(isdone==0):
        if x <= (len(list1)-1):
            if list1[x]=="!": 
                fact=math.factorial(int(list1[x-1]))
                list1[x-1]=fact
                del(list1[x])
                x=0
        else:
            isdone=1
        x=x+1     
    isdone=0
    x=0
    while(isdone==0):
        if x <= (len(list1)-1):
            if list1[x]=="^": 
                pwr=list1[x-1]**list1[x+1]
                list1[x-1]=pwr
                del(list1[x])
                del(list1[x])
                x=0

        if x <= (len(list1)-1):
            if list1[x]=="§":
                rad=list1[x+1]**(1/list1[x-1])
                list1[x-1]=rad
                del(list1[x])
                del(list1[x])
                x=0
        else:
            isdone=1
        x=x+1
    isdone=0
    x=0
    while(isdone==0):
        if x <= (len(list1)-1):
            if list1[x]=="*": 
                prod=list1[x-1]*list1[x+1]
                list1[x-1]=prod
                del(list1[x])
                del(list1[x])
                x=0

        if x <= (len(list1)-1):
            if list1[x]=="/":
                divis=list1[x-1]/list1[x+1]
                list1[x-1]=divis
                del(list1[x])
                del(list1[x])
                x=0
        else:
            isdone=1
        x=x+1   
    for x in range(0,len(list1)):
        answer=answer+list1[x]
    return(answer)
while(1==1):
    Curr=[]
    Calc=[]
    answer=0
    prod=0
    divis=0
    isdone=0
    b=0
    a=input("Please Enter the numbers to be calcualted! §=√ Enter stop to end the Programm!")
    if a=="stop":
        exit(0)
    for x in range(0,len(a)):
        if a[x] in Numbers:
            Curr.append(a[x])
            b=0
        else:
            if b==1:
                Calc.append(a[x])               
            elif a[x]==".":
                Curr.append(a[x])
            else:
                Calc.append(listint(Curr))
                Curr=[]
                Calc.append(a[x])
                b=1
    Calc.append(listint(Curr))
    Curr=[]
    
    for x in range (0,len(Calc)):
        if isinstance(Calc[x], int) or isinstance(Calc[x], float) == True:          
            if Calc[x-1] == "+":
                Curr.append(Calc[x])
            else:
                Curr.append(Calc[x])
        if Calc[x] in Functions:
            Curr.append(Calc[x])    
    isdone=0
    x=0
    while(isdone==0):
        if x <= (len(Curr)-1):   
            if Curr[x]=="(":
                d=x+1
                isdone2=0
                while(isdone2==0):
                    if x <= (len(Curr)-1):
                        if Curr[d]=="(":
                            isdone2=1
                            x=x+1
                        elif Curr[d]==")":
                            precalc=calc(Curr[x:d])
                            Curr[x]=precalc
                            del(Curr[x+1:d+1])
                            x=0
                            d=0
                            isdone2=1
                        else:
                            d=d+1
            else:
                    x=x+1
        else:
            isdone=1
    print(calc(Curr))