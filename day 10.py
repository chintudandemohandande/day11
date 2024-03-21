# ! method riding
# * polymorphism in classes

# class bank:
#     def ratio(self):
#         print("all banks has repo rate")
        
# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 9%")
        
# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 7.5%")

# i=IOB()
# i.ratio()

# s=SBI()
# s.ratio()

# ? eg :2
# class USA:
#     def language(self):
#         print("english")
    
#     def capital(self):
#         print("Washington")
        
# class INDIA(USA):
#     def language(self):
#         print("NONE")
    
#     def capital(self):
#         print("NEW DELHI")
        
# I = USA()
# I.language()
# I.capital()

# EG:3
# POLYmorphism using objects

# c1, c2 ----> c1 = print(c1), print(c2)
# f1, f2
# class c1:
#     def multi1(self):
#         print("class1")
        
# class c2(c1):
#     def multi2(self):
#         super.multi1()       
#         print("class2")

# obj1 =c2()
# obj2 =c1()

# eg 4:
# def display(a):
#     a.multi1()
    
# display(obj1)
# display(obj2)


# obj2 =c1()
# obj2.multi2()

# changw the functionality of built in functions
# eg 5
# a = 9
# b = 6
# print(a. __add__(b)) #? duner method or marfic method
# print(a. __sub__(b))

# eg 6
# class shoping:
#     def __item__(self, l1):
#         self.items = len(l1)
        
#     def __len__(self):
#         length = len(self.items)
#         return length
        
# s =  shoping([1,2,3,4,5])
# print(len(s))

# ! ---> method overloading
# class suming:
#     def add(self, a, b):
#         print(a+b)
        
#     def add(self, a, b, c):
#         print(a+b+c)
    
    
# s = suming()
# s.add(4,5)
# s.add(4,5,1)

# eg:2
# class suming:
#     def add(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=Nonew and b!=None:
#             print(a+b)
#         else:
#             print(a)
            
# obj=suming()
# obj.add(2)
# obj.add(3, 4)
# obj.add(1,20,3)


@@ -114,3 +114,157 @@
# obj.add(1,20,3)

# ! ------> abstraction
# the process of hiding 
# the implementation ddetails in abstraction

# ? eg 4

# from abc import ABC,abstractmethod
# class shapes(ABC):
#     @abstractmethod
#     def sides(self):
#         print('all shapes have sides except circle')

#     def names(self):
#         print("i am triangle")

#     def sides(self):
#         pass 
# class square(shapes):
#     def square(self):
#         print("4 sides")

#     def sides(self):
#         pass

# tr=triangle()
# tr.traingle_sides()
# tr.name()


# def greet():
#     return 'good morning'
# print(greet())

# ! Rulesto define abstract class1
# 1.) absract class cannot be instantiated
# 2.)from abc import ABC , absraction method
# 3.) subclasess the normal class with ABC
# 4.)convert the normal method inside the abstraction class to class
# 5.) All the child classes have to be subclassed with abstract class
# 6.) The abstract method should be present in the child classes

# ! eg:2
# class a1(ABC):
#     def m1(self):
#         print("this is abstract class")

# class c2(c1):
#     def m2(self):
#         super().m1()
#         print("i am a child 1")

#     def m1(self):
#         pass

# class = c2()
# class2.m2()

# eg :3
# from abc import ABC, abstractmethod
# class password(ABC):
#     @abstractmethod
#     def pwd(self):
#         pswd = 'sidd1994$'
#         return pswd

# class login:
#     def validate(self, name, password):
#         if super().pwd()==password:
#             print("welcome", name, '||')
#             print("login sucessfully")
#         else:
#             print("please check the password")
#     def pwd(self):
#         pass

# login = login()
# name = input("enter the name: ")
# pwd = input("enter the password: ")
# login.validate(name, pwd)

#  ! Encapsulation 
#----> eg:1
# class car:
#     __name="bmw"
#     print(__name)
# c1 = car()
# print(c1.name)
# c1.name = "audi"
# print(c1.name)

#---> eg :2
# ? acessing private data outside the class
# class c1:
#     __phone = '8989898898' 

#     def display(self):
#         print(self.__phone)

# c = c1
# c.display()

# -----> eg :3
# ? declare private method
# class class1:
#     def __m1(self):
#         print("i am privte method")

#     def __int)__(self):
#         self.__m1()
# c=class1()  
# c.__m1()  
#     if a == b:
#     print("a is equal to b")
# else:
#     print("a is not equal to b")



#     if a == b: print("a is equal to b") else: print("a

# ? mested class
# class class1:
#     class class2:
#         name='siddu'

#         def display(self):
#             print(self.name)
#     obj1=class2()

# obj = class1()
# obj.obj1.display()
# if name == "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")



#     if name == "John":
#     print("Your name is John")
# elif age == 23:
#     print("You are 23 years old")
# else:
#     print("Your name is not John and you are not 23 years old")


#     if name == "John":
#     pass

# result = "John" if name == "John" else "Jane"
# if name == "John":
#     if age == 23:
#         print("Your name is John and you are 23 years old")
#     else:
#         print("Your name is not John")




















# ! ------> abstraction
