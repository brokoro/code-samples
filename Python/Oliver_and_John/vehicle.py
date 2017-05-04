class Vehicle:

	def __init__(self, name, kind, color, value):
		self.name = name
		self.kind = kind
		self.color = color
		self.value = value

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

	def changeName(self, newName):
		self.name = newName

	def changeKind(self, newKind):
		self.kind = newKind

	def changeColor(self, newColor):
		self.color = newColor

	def changeValue(self, newValue):
		self.value = newValue

	def describe(self):
		desc = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		# desc = "%s is a %s %s worth $%.2f." % (self.getName(), self.getColor(), self.getKind(), self.getValue())
		return desc