class User:
	def __init__(self):
		self.name=" "
		self.age=0
		self.phno=0
		self.positive_date=" "
	def read(self):
		self.name=input("enter ur name")
		self.age=int(input("enter ur age"))
		self.phno=int(input("enter ur phno"))
		self.positive_date=input("enter ur positive date")
	def print(self):
		print("name=",self.name)
		print("age=",self.age)
		print("phno=",self.phno)
		print("positive date=",self.positive_date)

		