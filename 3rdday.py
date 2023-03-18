#list comprehension
#for loop version
'''result=[]
for i in range(11):
    result.append(i)
print(result)'''
#list comprehension
'''list1=[i for i in range(11)]
print(list1)'''
#for  loop version===>odd
'''list1=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(list1)'''
#list comprehension ==>odd
'''list2=[i for i in range(11)if i%2!=0]
print(list2)'''
#for  loop version===>odd and square of even
'''result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)'''
#list comprehension ==>odd and square of even
'''list2=[i if i%2!=0 else i**2 for i in range(11)]
print(list2)'''
#for  loop version===>sqare of odd and cube of even in a matrix
'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    for j in i:
     if j%2!=0:
        result.append(j**2)
     else:
        result.append(j**3)
print(result)'''
#list comprehension ==>sqare of odd and cube of even in a matrix
'''list2=[j**2 if j%2!=0 else j**3   for i in mat for j in i]
print(list2)'''
##for  loop version===>sqare of odd and cube of even in a matrix but print in matrix format
'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    k=[]
    for j in i:
        
     if j%2!=0:
        k.append(j**2)
     else:
        k.append(j**3)
    result.append(k)    
print(result)'''

#list comprehension ==>sqare of odd and cube of even in a matrix but print in matrix format
'''result=[[j**2 if j%2!=0 else j**3 for j in i ]for i in mat ]
print(result)'''
#question tuple
'''def give(a,b):
    res=[]
    for i in b:
        res.append((i,a.index(i)))
    print(res)
give([9,3,6,1,5,0,8,2,4,7],[6,4,6,1,2,2])
def give(a,b):
    res=[(i,a.index(i)) for i in b]
give([9,3,6,1,5,0,8,2,4,7],[6,4,6,1,2,2])'''
#question dictonary(himanshu)
'''problem statement: for each number in list_b,get the number and its position(index) in mylist as return list of tubles
 mylist=[9,3,6,1,5,0,8,2,4,7]
 list_b=[6,4,6,1,2,2]'''
'''a=[9,3,6,1,5,0,8,2,4,7]
b=[6,4,6,1,2,2]
res={}
for i in b:
        res[i]=a.index(i)
print(res)
res={i:a.index(i) for i in b}
print(res)'''
#question
'''problem Statement: the goal is to tokenize the following 5 sentences into  words,excluding  the stop words
input:
sentences=["a new world record was set","in the holy city of ayodhya"
           ,"on the eve of diwali on tuesday","with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of saruyu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']'''
'''sen=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of saruyu river"]
stop=['for','a','of','the','and','to','in','on','with','was']
newres=[]
for i in sen:
    data=[]
    for j in i.split():
        if j not in stop:
            data.append(j)
newres.append(data)
newres=[[ j for j in i.split() if j not in stop]for i in sen]
print(newres)
#question
n=list(map(int,input().split(',')))
num1=sum(n[:n.index(5)])+sum(n[n.index(8)+1:])
l=n[n.index(5):n.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1)'''
#question
'''string rotation
input: rhdt:246,ghftd:1246
exp1:here every string is associated with the number seperated by :
----> if sum of sqare of digits is even then rotate the string by 1
2
----> if the sum of sqare of digit  is odd the rotatethe string left by 2 position'''

'''s=input().split(',')
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))'''
#question
'''given a number n,write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n.
g(n)=f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
where g(n) is the  sum and f(n) is largest prime factor
example:-
g(n)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
    =5    +11   +3    +  13 + 7   +  5  + 2   + 17  + 3
    =66'''
def gprime(n):
    list1=[]
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
def prime(n):
    for i in range(2,n+1):
        




                          
                             


    

        












