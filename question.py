class Question:
	startingLetter = 97
	lastLetter = 122

	def __init__(self):
		self.number = None
		self.question = None
		self.answer = None
		self.choices = []

	def print(self):
		print(f"{self.number}. {self.question}")

		letter = Question.startingLetter
		for choice in self.choices:
			print(chr(letter) + ". " + choice)
			letter += 1

		return

	def getAnswer(self):
		givenAnswer = input("> ")

		letter = Question.startingLetter
		for choice in self.choices:
			if givenAnswer == chr(letter) and choice == self.answer:
				return True

			letter += 1

		return False

	def checkAttributePresence(self, operation):
		if operation == "?" and self.question != None:
			return True
		if operation == "A" and self.answer != None:
			return True
		if operation == "C" and self.choices != []:
			return True

		return False
	
	def checkAllAttributes(self):
		if self.question == None or self.answer == None or self.choices == []:
			return False

		return True
