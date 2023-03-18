#question
'''write a python function,nearest_palindrom() which accepts a number and return palindrome greater than the given no.
sample           expectedoutput
99                      101
1221                   1331    '''
'''import sys
def nearest_palindrom(n):
    for i in range(n+1,sys.maxsize):
       if(str(i)==str(i)[::-1]):
           return i
print(nearest_palindrom(99))
print(nearest_palindrom(90))'''
#question
'''the patient is stored in a list. the details of the medical specialities
'''
'''dictonary={"p":"pediatrics","o":"orthopedices","e":"ent"}
list1=[101,'p',102,'o',302,'p',305,'p']
def max_visit_specility(dictonary,list1):
 p=(list1.count('p'))
 o=(list1.count('o'))
 e=(list1.count('e'))
 if p>e and p>o:
    specility=dictonary['p']
 elif e>p and e>o:
    specility=dictonary['e']
 else :
    specility=dictonary['o']
 return  specility
print( max_visit_specility(dictonary,list1))'''
#question need to wor more
'''

str1="I like Python "
str2="Java is a very popular language"
str3="l"
str4="k"
def match(list1,list2):
    list3=[]
    for i in list1:
      for j in list2:
         if(i==j and i!=' ' and j!=' '):
             list3.append(j)
             break
    if(len(list3)!=0):
        for i in list3:
         print(i,end='')
        
    else:
        print(-1)
match(str1,str2)
match(str3,str4)'''
'''class pinu:
 def  __returnn(self):
    print("hello")
s1.pinu()
s1.'''
class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=dam("abc dam",3.5)
print("dan name:",dam1.name)
print("dam length:",dam1.get_length())
'''class table:
    def __init__(self):
        self.no_of_legs=4
        self  .__glass_top=None'''
        
