#question
''' WeCare insurance company wants to calculate premium of vhicles.
vehicles are of two types-"two Wheller" and "four wheeler".
Each vechicle is identified by vechile id ,type,cost and preium amount.
premium abount is 2% of vechile cost for two wheeler and ^% of the vechile cost for four eheeler
calculate the premium amount and display the vechile details.
write a python orogram to implement the class chosen with its attributes and methods.
note:
consider all instance variables to be private and methods to be public
includine the getter and setter methods for all instances variables
display appropiate eror message if the vechile type is invalid
perform case sensitive string coparision
repesent few objects of class,initilize instances variable using stter methods,invoke apporopiatementhods and test your program'''
class WeCare:
    def __init__(self,ids,types,cost):
        self.__ids=ids
        self.__types=types
        self.__cost=cost
        self.__premium_amount=None
    def get_ids(self):
         return self.__ids
    def get_types(self):
         return self.__types
    def get_cost(self):
         return self.__cost
    def calculate(self,types):
        if self.__types=="two Wheller":
            self.__premium_amount=self.__cost*0.02
            return self.__premium_amount
        elif self.__types=="four Wheller":
            self.__premium_amount=self.__cost*0.06
            return self.__premium_amount
        else:
            self.__premium_amount="invalid"
            return self.__premium_amount
    def set_premium_amount(self):
         self.__premium_amount=self.calculate(self.__types)
    def get_premium_amount(self):
        self.set_premium_amount()
        return self.__premium_amount
    def display(self):
        print("id",self.get_ids())
        print("types",self.get_types())
        print("cost",self.get_cost())
        print("premium_cost",self.get_premium_amount())
c1=WeCare(101,"two Wheller",20000)
c1.display()
''' a university wants to auomate their admission process.
students are admitted based on marks scored in a qualifing exam.
a student is identified by student id,age,and marks in quilifing exam
data are valid,if:
                 age >20
                 marks is btween 0 and 100(both inclusive)
                 a student qualifies for admission ,if
                 age and marks are valid and marks is 65or more
write a python program to represnt the student seeking
admission in the university
RULE TO FOLLOW:
the details of student class are given below
class name: student'''
class student:
    def __init__(self,ids,age,marks):
        self.__ids=ids
        self.__age=age
        self.__marks=marks
        
    def get_ids(self):
        return self.__ids
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def validate_marks(self,marks):#validate marks
        if self.__marks>=0 or self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self,age):#validate age
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks(self.__marks) and self.validate_age(self.__age):
            if self.__marks>=65:
                print("eligiable for admission")
                self.cfees()
                
            else :
                print(" not eligiable for admission")
        else:
            print("invalid input")
    def cfees(self):
        sub_code=int(input())
        if sub_code== 1001:
            if self.__marks>85:
                print("fees",25575*0.75)
            else:
              print("fees",25575)
        elif sub_code== 1002:
            if self.__marks>85:
                print("fees",15500*0.75)
            else:
                print("fees",15500)
        else:
            print("not valid course")
    def display(self):
            print("id",self.get_ids())
            print("age",self.get_age())
            print("marks",self.get_marks())
            
s1=student(1,22,99)
s1.display()
s1.check_qualification()
s2=student(1,2,99)
s2.display()
s2.check_qualification()
s2=student(1,23,45)
s2.display()
s2.check_qualification()

#question
'''PizzaForYou''' 
types=['small','medium','Small','Medium']
class Customer:
    def __init__(self,c_name,quantity):
        self.__c_name=c_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_c_name(self):
        return self.__c_name
    def get_quantity(self):
        return self.__quantity
class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__s_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
            if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
                if self.__pizza_type.title()=="Small":
                    self.pizza_cost=150*Customer.get_quantity(self.__customer)
                    if self.__additional_topping:
                        self.pizza_cost+=35*Customer.get_quantity(self.__customer)
                if self.__pizza_type.title()=="Medium":
                    self.pizza_cost=200*Customer.get_quantity(self.__customer)
                    if self.__additional_topping:
                        self.pizza_cost+=50*Customer.get_quantity(self.__customer)
                if not self.__s_id:
                    self.__service_id=self.__pizza_type[0]+ str(Pizzaservice.counter+1)
                    Pizzaservice.counter+=1
            else:
                self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance):
        self.__delivery_charge=0
        self.__distance=distance 
        Pizzaservice.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance(self):
        if self.__distance in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                dis=1
                while(dis<=self.__distance):
                    if dis in range(1,6):
                        self.pizza_cost+=5
                    if dis in range(6,11):
                        self.pizza_cost+=7
                    dis+=1
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance(self):
        return self.__distance
c=Customer("Bhagyashree",5)
p1=Pizzaservice(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())
d1=Doordelivery(c,"MEDIUM",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())        
        
    

        
        
            
         
