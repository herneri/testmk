"""
    Copyright 2024 Eric Hernandez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class Question:
	# ASCII decimal value for 'a', where
	# lettering for answers begins
	startingLetter = 97

	# ASCII decimal value for 'z', where
	# lettering for answers ends
	lastLetter = 122

	def __init__(self):
		self.number = None
		self.question = None
		self.answer = None
		self.choices = []
		self.isCorrect = None

	def print(self):
		print(f"{self.number}. {self.question}")

		letter = Question.startingLetter
		for choice in self.choices:
			print(chr(letter) + ". " + choice)
			letter += 1

		return

	def getAnswer(self, givenAnswer):
		letter = Question.startingLetter
		for choice in self.choices:
			if givenAnswer == chr(letter) and choice == self.answer:
				self.isCorrect = True
				return self.isCorrect
			letter += 1

		self.isCorrect = False
		return self.isCorrect

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
