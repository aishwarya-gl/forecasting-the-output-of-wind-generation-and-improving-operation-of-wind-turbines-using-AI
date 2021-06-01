class Student:
	def __init__(self):
		self.rollno=0
		self.name=" "
		self.age=0
	def read(self):
		self.rollno=int(input("enter a roll number"))
		self.name=input("enter ur name")
		self.age=int(input("enter ur age"))
	def print(self):
		print ("roll no= ",self.rollno)
		print("name=",self.name)
		print("age=",self.age)
o=Student()
o.print()
o1=Student()
o.read()
o.print()
