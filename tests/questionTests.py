from sys import path
path.insert(1, "..")

import unittest
import question as question

questionObject = None

# Unit tests for testmk's Question class
class TestQuestion(unittest.TestCase):
	def test_getAnswer(self):
		questionObject = question.Question()
		questionObject.number = 1
		questionObject.question = "What is the name of this program?"
		questionObject.answer = "testmk"
		questionObject.choices = ["testmk", "mktest", "test"]

		# Right answer
		self.assertEqual(questionObject.getAnswer("a"), True)

		# Wrong answer
		self.assertEqual(questionObject.getAnswer("b"), False)

		# Answer that doesn't exist
		self.assertEqual(questionObject.getAnswer("e"), False)
		return

	def test_checkAttributePresence(self):
		questionObject = question.Question()

		# No attributes present
		self.assertEqual(questionObject.checkAttributePresence("?"), False)
		self.assertEqual(questionObject.checkAttributePresence("A"), False)
		self.assertEqual(questionObject.checkAttributePresence("C"), False)

		# Some attributes present 
		questionObject.question = "A question"
		self.assertEqual(questionObject.checkAttributePresence("?"), True)
		self.assertEqual(questionObject.checkAttributePresence("A"), False)
		self.assertEqual(questionObject.checkAttributePresence("C"), False)

		# All attributes present
		self.assertEqual(questionObject.checkAttributePresence("?"), True)

		questionObject.answer = "Something"
		self.assertEqual(questionObject.checkAttributePresence("A"), True)

		questionObject.choices = ["value", "value", "value"]
		self.assertEqual(questionObject.checkAttributePresence("C"), True)

		return
	
	def test_checkAllAttributes(self):
		questionObject = question.Question()

		# Empty object
		self.assertEqual(questionObject.checkAllAttributes(), False)

		# Incomplete object
		questionObject.number = 1
		questionObject.question = "A question"

		self.assertEqual(questionObject.checkAllAttributes(), False)

		# Complete object
		questionObject.answer = "Something"
		questionObject.choices = ["value", "value"]

		self.assertEqual(questionObject.checkAllAttributes(), True)
		return

if __name__ == "__main__":
	unittest.main()
