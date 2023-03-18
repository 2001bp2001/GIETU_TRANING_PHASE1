#function
'''def fun1():
    print("its a function")
fun1()'''
#parametre function
'''def fun2(num1,num2):
    print("num1",num1,"num2",num2)
    #print()__str__(inside print everthing is string num in covented to string by__str__ by implist type casting)
fun2(10,20)
def fun3(num1,num2):
    num3=num1+num2
    return num3
fun3(100,200)
print("value returned",fun3(100,200))
def fun4(num1,num2):
    num3=num1+num2
    return num3
fun4(100,200.5)
print("value returned",fun4(100,200.2))
def fun5(num1,num2):
    num3=float(num1)+num2
    return num3
fun5('100',200.5)
print("value returned",fun5('100',200.2))
def fun6(num1,num2):
    num3=num1+str(num2)
    return num3
fun5('20cse',102.)
print("value returned",fun6('b20cse',102))
'''#categories of function
#based on arguments
#positional arguments
'''def fun6(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun6(10,20,30,40)
fun6(10,20,30,400)
fun6(10,20,30,450)'''
#2 keyword arguments
'''def fun7(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun7(num4=10,num3=20,num1=30,num2=40)'''
#default arguments
'''def fun8(name,branch,rollno,clgname="clg"):
    print("name",name,"branch",branch,"rollno",rollno,"clgname",clgname)
fun8("bp","cse",102,"giet")
fun8("bpp","cst",12,"giet")
fun8("bppp","che",20,"giet")
fun8("bpppp","it",2,"giet")'''
#varibal number of arguments
'''def fun9(*var):#var is tuple
    for i in var:
        print(i,end='')
fun9(10,20)
print()
fun9(20,30,40,50)
print()
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return sum1
print(add(10,20))
print()
print(add(30,40,50))
print()
print(add(40,50,30,20))'''
#try the problem ststement should not have multiple  7

'''while(1):
    a=int(input())
    b=int(input())
    if(a==7 and b==7):
       break
    else:
      c=int(input())
      if((c==7 and b==7) or (c==7 and a==7)):
         break
      else:
        if a!=7 and b!=7 and c!=7:
         print(a*b*c)
        elif c==7:
         print(-1)
        elif(b==7):
         print(c)
        elif(a==7):
         print(b*c)'''
'''def fun(inr,currname):
    if(currname=="Euro"):
        print(inr*0.01417)
    elif(currname=="British Pounds"):
        print(inr*0.0100)
    elif(currname=="Australian Dollar"):
        print(inr*0.2140)
    elif(currname=="Candian Dollar"):
        print(inr*0.02027)
    else:
        print(-1)
fun(300,'Euro')
#question:
adult=int(input())
child=int(input())
c=(((adult*37550.0)+((child*37550.5)/3))*1.07)*0.90
print(c)'''
#question
def pay(c1,c5,tc):
    n5=tc//5
    print(n5)
    if n5>=c5:
        if tc-(5*n5)>c1:
          print(-1)
        else:
            print("1 coin",tc-(5*n5))
            print("5 coin",n5)
    elif n5<c5:
         print("1 coin",tc-(5*n5))
         print("5 coin",n5)
        

pay(2,4,21)
pay(11,2,11)
pay(3,3,19)
pay(2,4,1)
pay(2,4,5)

#list---->orderd--->default indexing
#element are of different type
list1=[]
print("list",list1,type(list1))
list2={10,20,30}
print(list2)
list3={20,"bp","khyati"}
print(list)
list4=list([100,200,300,400])
print(list)
list4.append(90)
print(list4)
list4.extend([60,70])
print(list4)
list4.insert(0,51)#index,value
list4.remove(300)
print(list4)
list4.pop(0)#index
print(list4)
del list4[3]#index
print(list4)

#question
def count(str1):
    lcount=0
    dcount=0
    for i in str1:
        if i.isalpha():
            lcount=lcount+1
        elif i.isdigit():
            dcount=dcount+1
        else:
            continue
    return [lcount,dcount]
print(count( "info 123"))

#question
def find_pair(l,n):
    count=0
    a=len(l)
    for i in range(0,len(l)-1):
        for j in range(i+1,a):
            if(l[i]+l[j]==n):
                count=count+1
                break
    return count
print(find_pair([1,2,7,4,5,6,0,3],6))

#question
def con(str1):
    if len(str1) < 2:
        return -1
    else:
       return str1[0:2]+str1[-2:]
       
print(con("w3resorce"))
print(con("a"))

#question 2nd approch
def con(str1):
    if len(str1) < 2:
        return -1
    else:
       str2= str1[0]+str1[1]+str1[-2]+str1[-1]
       return str2
print(con("w3resorce"))
print(con("a"))

#question
def conn(str1):
    if len(str1)>2:
        if str1[-3:]=="ing":
           str1=str1+'ly'
           return(str1)
        else:
         str1=str1+'ing'
        return(str1)
    else:
        return str1
print(conn("sleep"))
print(conn("sleeping"))
print(conn("sl"))

#question
def check(n):
   num1=str(n*2)
   a=str(n)
   count=0
   for x in a:
    if x in num1:
     count+=1
    else:
        return False
   if count==len(a):
       return True
print(check(245))
print(check(125874))

#question 1
def average(a):
     count=0
     avg=sum(a)//len(a)
     for i in a:
         if(i>avg):
             count+=1
     return (count*100)//len(a)       
print(average((12,18,25,24,2,5,18,20,20,21)))
#question 1b
def fre(a):
    list1=[]
    count=0
    for i in range(0,26):
        list1.append(a.count(i))    
    return list1
print(fre((12,18,25,24,2,5,18,20,20,21)))
#question 1c
def sort_marks(a):
    return sorted(a)   
print(sort_marks((12,18,25,24,2,5,18,20,20,21)))

#question
def tran(a,str1 ):
    list1=str1.split()
    list2=[]
    for i in list1:
               list2.append(a[i])
    return list2
print(tran({"merry":"god","cristmas":"jul","and":"och","happy":"gotta","new":"nytt","year":"ar"},"merry cristmas"))
def new_list(a,b):
    print(a)
    print(b)
    list2=[]
    list1=[i for i in range(a,b+1)]#list compression
    print(list1)
    for i in range (len(list1)):#list2=[list1[i:j+1]for i in range(len(list1)) for j in range(i,len(list1))]
        for j in range(i,len(list1)):
            list2.append(list1[i:j+1])
    print(list2)
    c=0
    d=0
    for i in list2:
        if sum(i)%2!=0:
            c+=1
    print(c)
    for i in list2:
        if (i[0]+i[-1])%2==0:
            d+=1
    print(d)    
new_list(1,3)




    




            
        
    




