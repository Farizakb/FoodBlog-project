

# from xml.dom.expatbuilder import parseString


# class BIRD:
#     def sound(self):
#         pass    
    
    
# class CAT:
#     def sound(self):
#         pass
    
    
    
# class PET:
#     def voice(self,animal):
#         if isinstance(animal, CAT):
#             CAT.sound()
#         if isinstance(animal,BIRD):
#             BIRD.sound()    







# Python Program to depict multiple inheritance
# when we try to call the method m for Class1,
# Class2, Class3 from the method m of Class4

# class Class1:
#     @classmethod
#     def m(self):
#         print("In Class1")
	
# class Class2(Class1):
#     @classmethod
#     def m(self):
#         print("In Class2")

# class Class3(Class1):
#     @classmethod
#     def m(self):
#         print("In Class3")	

# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#         Class2.m()
#         Class3.m()

# obj = Class4()
# obj.m()






# class View:
#     def __init__(self,**kwargs):
#         self.name = "eles"
#         self.surname = "gerov"
#         self.number = kwargs["number"]
#     password = 2
#     email = "elesgerovzafiyet"
# class EmailView(View):
#     def show_properties(self):
#         print(self.password)
#         print(self.name)
#         print(self.email)
#         print(self.surname)
#         print(self.number)
        
        
# y = EmailView(number="0890909")
# y.show_properties()