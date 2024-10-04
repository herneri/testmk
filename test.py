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

import question

# ANSI color escape codes
# for distinguishing output
C_PROMPT = "\x1b[36m"
C_LINE = "\x1b[35m"
C_WRONG = "\x1b[31m"
C_RIGHT = "\x1b[32m"
C_CLEAR = "\x1b[0m"

def arrayToString(array):
	string = ""

	for element in array:
		string += element

	return string

# Check whether or not operation has already been done
def getOperation(question, operation):
	if operation == "?" or operation == "A" or operation == "C":
		if question.checkAttributePresence(operation) == False:
			return True

		print("testmk: STATEMENT ERROR: " + operation + " used twice for one question")
		return False

	print("testmk: SYNTAX ERROR: " + operation + " is an invalid value")
	return False

# Set an attribute of the question object at the end of a statement
def endStatement(question, operation, value):
	value = arrayToString(value)
	if operation == "?":
		question.question = value
	elif operation == "A":
		question.answer = value
	elif operation == "C":
		question.choices.append(arrayToString(value))

	return question

def readTest(testFile, questionSet):
	f = open(testFile)
	operation = "n"

	questionObject = question.Question()
	questionNumber = 1
	value = []

	settingValue = False
	isStatement = False

	for line in f:
		for char in line:
			# Complete question object
			if questionObject.checkAllAttributes() == True and isStatement == False:
				questionObject.number = questionNumber
				questionSet.append(questionObject)
				questionObject = question.Question()
				questionNumber += 1
				continue

			# End of statement
			if char == ";" and isStatement == True:
				if settingValue == False:
					print("testmk: SYNTAX ERROR: Missing assignment (=) operator")
					exit(1)

				isStatement = False
				settingValue = False
				questionObject = endStatement(questionObject, operation, value)
				value = []
				continue
			# Value assignment
			elif char == "=" and isStatement == True:
				if settingValue == True:
					print("testmk: SYNTAX ERROR: Missing semicolon (;) at end of statement")
					exit(1)

				settingValue = True
				continue

			# Check for syntax errors regarding operations
			if isStatement == False and (char != '\n' and char != ' '):
				operation = char
				isStatement = getOperation(questionObject, operation)
				if isStatement == False:
					exit(1)

				continue

			# Choices handling
			if settingValue == True and isStatement == True:
				if char == ",":
					questionObject = endStatement(questionObject, operation, value)
					value = []
					continue

				value.append(char)
				continue

	f.close()
	return

def startTest(questionSet):
	for question in questionSet:
		question.print()
		question.getAnswer(input(f"{C_PROMPT}> "))

		print(C_CLEAR)

	return

def getResults(questionSet):
	numberCorrect = 0
	for question in questionSet:
		print(f"{question.number}. {question.question}")

		if question.isCorrect == False:
			print(f"{C_WRONG}X{C_CLEAR} - {question.answer}")
			continue

		print(f"{C_RIGHT}C{C_CLEAR} - {question.answer}")
		numberCorrect += 1
	
	print("\nTotal score: " + str(numberCorrect/len(questionSet)))
	print(str(numberCorrect) + " out of " + str(len(questionSet)))
	return
