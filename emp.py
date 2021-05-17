class Employee:
	def __init__(self):
		self.empid=0
		self.empname=" "
		self.address=" "
		self.phno=0
	def read(self):
		self.empid=int(input("enter ur no"))
		self.empname=input("enter ur name")
		self.address=input("enter ur address")
		self.phno=int(input("enter ur phno"))
	def print(self):
		print("empid=",self.empid)
		print("empname=",self.empname)
		print("address=",self.address)
		print("phno=",self.phno)
o=Employee()
o.read()
o.print()
