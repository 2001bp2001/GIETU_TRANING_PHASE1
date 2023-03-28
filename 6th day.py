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
'''A bank has many customers and each customer has a bank account
There are also privileged customers 
who can earn bonus points for each of their transaction. 
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- account
_init_(customer_id, customer_name, age, account)
+ withdraw(amount)
+ take_card()
+ get_customer_id()
+ get_customer_name()
+ get_age()
+ get_account()
Account
- account_type
- balance
- min_balance
_init_(account_type,balance,min_balance)
+ get_account_type()
+ get_balance()
+ get_min_balance()
+ set_balance(balance)
PrivilegedCustomer
- bonus_points
_init_ (customer_id, customer_name, age, account, 
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the account balance based on the amount withdrawn. 
Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than account balance.
LimitReachedException - If the balance amount is less than minimum account balance.
take_card(): Displays the message "Take card out from the ATM".
PrivilegedCustomer:
increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method,
if no exceptions occured.
If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

Write a Python program to create a new PrivilegedCustomer with below details:
Customer Id: 100
Customer Name: Gopal
Age: 43
Bonus Points: 100
Account Type: Savings
Account Balance: 1000
Account minimum: 500

The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw.
------------------------------------------

A company is in the process of providing annual hike to its employees based on incentives and performance of the employee.
A partial python program has been written for the above requirement, complete the code by using the information and part of class
diagram given below:

RULES TO FOLLOW
=================
Class Description:
The program has three classes – Company, Employee and PermanentEmployee. Company and Employee classes are already coded for you.
Refer starter code.

Employee class:
Every employee is given a performance rating (1-3) at the end of every year
Last five year's performance rating of an employee is stored in the attribute, performance_list
Refer table for example and interpretation of data in performance_list, assuming current year is 2015
Permanent Employee class:
identify_performance_hike():
Permanent employees are eligible for performance hike based on their last three years performance as given in table
Identify the hike % and return it. If hike is not applicable, return None'''
