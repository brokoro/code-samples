class Vehicle:

	# Initialization 
	def __init__(self, name, kind, color, value):
		self.name = name
		self.kind = kind
		self.color = color
		self.value = value
		self.history = {}

	# Accessor methods. Retrieve the value of a field

	def getName(self):
		return self.name

	def getKind(self):
		return self.kind

	def getColor(self):
		return self.color

	def getValue(self):
		return self.value

	# Mutator methods. Change the value of a field

	def setName(self, newName):
		self.name = newName

	def setKind(self, newKind):
		self.kind = newKind

	def setColor(self, newColor):
		self.color = newColor

	def setValue(self, newValue):
		self.value = newValue


	#Descriptor methods
	def describe(self):
		desc = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		# desc = "%s is a %s %s worth $%.2f." % (self.getName(), self.getColor(), self.getKind(), self.getValue())
		return desc

	def addHistory(self, date, desc):
		