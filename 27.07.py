# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,2)  #super().__init__(3) 

#     def findArea(self):
#         a, b = self.sides
#         area = a*b
#         print('The area of the rectangle is %0.2f' %area)

#     def findPer(self):
#         a, b = self.sides
#         per = (a+b)*2
#         print('The perimetre of the rectangle is %0.2f' %per)

# class Square(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,1)
    
#     def findArea(self):
#         a = self.sides
#         area = a*a
#         print('The area of the square is %0.2f' %area)

#     def findPer(self):
#         a = self.sides
#         per = a*4
#         print('The perimetre of the rectangle is %0.2f' %per)

###################################
# class Auto:
#     '''Docstring'''
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model

#     def start(self):
#         return "Auto started to move"
    
#     def stop(self):
#         return "Auto stopped"
#########################################
# class Person:
#     '''Docstring'''
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Hello, my name is {}".format(self.name))

# class Auto:
#     '''Docstring'''
#     def __init__(self, name):
#         self.name = name

#     def move(self, speed):
#         print("{} moves at the speed {} km/h".format(self.name,speed))
