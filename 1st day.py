#python programming
#datatype
name="bp"
print("name",name,type(name))
name bp <class 'str'>
rollno=102
print("rollno",rollno,type(rollno)
print("percentage",percentabe,type(percentage))
complex no=102
print("complex no",complexno,type(rollno))

#
a=int(input(""))
if a%3==0:
      print("multiple of 3")
else if a%5==0:
    print("multiple of 5")
else if a%3==0 and a%5==0:
    print("multiple of both 3 and 5")
else:
    print("invalid")
            
#print(* no of object,sep='',end='/n')
#for loop
#range
#1 to 100
#odd btween 1to 100
# even btween 1 to 100


for i in range(0,101):
    print(i,end='')
print()
for i in range(0,101):
    if(i%2!=0):
        print(i,end='')
print()
for i in range(0,101):
    if(i%2==0):
        print(i,end='')
print()
#100 to 1
for i in range(100,0,-1):
    print (i,end='')
print()
for i in range(99,0,-2):
    if(i%2!=0):
        print(i,end='')
print()
for i in range(100,1,-2):
    if(i%2==0):
        print(i,end='')
print()
#break
#write a program 1 to 100 on 50 come out of loop
for i in range(1,101):
    if(i==50):
        break
        print(i,end='')
else :
    print("yes")

#continue
for i in range(1,101):
    
    if(i==50):
        continue
    else:
        print(i,end='')
#pass
for i in range(1,101): 
    if(i==50):
        pass
    print(i,end='')
#string rotation
'''input: rhdt:246,ghftd:1246
exp1:here every string is associated with the number seperated by :
----> if sum of sqare of digits is even then rotate the string by 1
2
----> if the sum of sqare of digit  is odd the rotatethe string left by 2 position'''
def sqare(n):
    while(n>0):
        rem=rem+(n%10)**2
        n=n//10
        
str="rhdt:246,ghftd:1246"
list1=[]
list2=[]
list1=str.split(',')
print(list1)
for i in list1:
 list2.append(i.split(':'))
if sqare(int(list2[1]))%2==0:
    print("yes")
print(list2)
    

        
        

