'''
Lorin Vandegrift
2/7/2015

Assigment 1:
	-- Number Operations: add, sub, mul, div, eq, lt, gt
	-- Boolean Operators: and, or, not
	-- Sequencing Operators: if, ifelse
	-- Create Dictionary: dictz (No operands)
	-- Stack Operations: begin, end
	-- Name definition: def (takes value and name)
	-- entire stack printing: stack
	-- top-of-stack printing operator: = 	

Assignment 2:
	integer constants	(123)
	boolean constants	(true and false)
	name constants		(/fact)
	code constants		(Code bewtween {...})
	stack operators:	(dup, exch, pop)
	read input file
	print error messages
	the operand stack	(spush, spop, checkTop)
	SPS Dictionaries	(check name, retrieve value, new pair)
	Dictionary Stack
	interpreter			(Tokenizing input, use re)
	Loop over tokens	(Push and pop stack)
	Output				(Print stacks when done)
	
'''



import sys
import re

#Program Variables
# The User Dictionary is checked before the system dictionary
# If the name is in the dictionary, it either pushes the value onto the stack
# preforms the operation
# Else, it raises an error



class SPSParser:

	#All Dictionaries are kept on the dictionary stack
	self.systemDictionary = {'''add':add, 'sub':sub, 'mul':mul, 'div':div, 'eq':eq, 'lt':lt, 'gt':gt'''}
	self.userDictionary = {}
	self.dictStack = [userDictionary, systemDictionary]
	self.stack = []	

	#Setup Dictionaries and other variables
	def __init__(self):
		pass

	'''
		Parsing the PostScript
	'''

	def evalLoop (self, tokens):
		p = 0 # control the loop by idex p
		while p < len(tokens):
			t = tokens[p]
			p += 1
			# handle number, push to the stack
			if self.isNum (t):
				self.spush (t)
			# handle operator, execute operator
			if self.isOper (t):
				self.operate(t)	#Finds out which dict the operator is in
			# handle {
			if t == '{':
				# push everything between { and } to the stack
				# store function name as key, function operations as list
				pass

		# handle stack operations pop, clear, stack
		# handle def
		# push name and array to the dict stack
		# handle if
		# recursively call “evalLoop” to execute the code array
		# handle ifelse
		# recursively call “evalLoop” to execute the code array
		# handle dict
		# define empty dict
		# begin: push dict to the dictionary stack
		# end: pop dict from the dictionary stack

	def parseProgram (self, fileContents):
		for line in fileContents:
			tokens = re.findall( "/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", line)
			#self.evalLoop (tokens)
			print (tokens)

	def execute (self):
		pass

	'''
		Dictionary Operations
	'''

	#Adds new item to the stack
	def spush(self, item):
		stack.append(item)		
		return None

	#Removes Item from the top of the stack
	#Throws error is the stack is empty
	def spop(self):
		if not stack:		
			err("Error in pop: Stack is empty...")
			return None
		else:					
			return stack.pop()

	#Returns the number of items in the stack
	def slen(self):
		pass

	#Empties the stack
	def sclear(self):
		pass

	#Duplicates the top item on the stack
	def dup(self):
		pass

	#Exhanges the top two item on the stack
	def exch(self):
		pass

	'''
		Utility Functions
	'''

	#Check if item is a number
	def isNum(self, item):
		if isinstance(item, float):
			return item
		else:
			err("Variable not a float.")

	def isDict(self, item):
		if isinstance(item, dict):
			return item
		else:
			err("Variable not a dictionary.")



	'''
		Math Operations
	'''

	#Addition
	def add(self):
		if slen() >= 2:
			spush(spop()+spop())
		else:
			return None

	#Subtraction
	def sub(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			spush(firstOperand-secondOperand)
		else:
			return None

	#Multiplication
	def mul(self):
		if slen() >= 2:
			spush(spop() * spop())
		else:
			return None

	#Division
	def div(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			spush(firstOperand / secondOperand)
		else:
			return None

	'''
		Boolean Operations
	'''

	#Equals
	def eq(self):
		if slen() >= 2:
			if spop() == spop():
				spush('true')
			else:
				spush('false')
		return None

	#Less than
	def lt(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			if firstOperand < secondOperand:
				spush('true')
			else:
				spush('false')
		return None

	#Greater Than
	def gt(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			if firstOperand > secondOperand:
				spush('true')
			else:
				spush('false')
		return None

	#And
	def sand(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			if isBool(firstOperand) and isBool(secondOperand):
				if firstOperand == 'true' and secondOperand == 'true':
					spush('true')	
				else:
					spush('false')
			else:
				err("Not Boolean")
		return None

	#Or
	def sor(self):
		if slen() >= 2:
			secondOperand = spop()
			firstOperand = spop()
			if isBool(firstOperand) and isBool(secondOperand):
				if firstOperand == 'true' or secondOperand == 'true':
					spush('true')	
				else:
					spush('false')
			else:
				err("Not Boolean")
		return None


	#Not
	def snot(self):
		if slen() >= 2:
			firstOperand = spop()
			if isBool(firstOperand):
				if firstOperand == 'true':
					spush('false')	
				else:
					spush('true')
			else:
				err("Not Boolean")
		return None
		
	'''
		Logical Operators
	'''

	#If
	def sif(self):
		ifcode = isCode(spop()) # Make sure it is code (a list)
		if chBool(spop()):
			evalLoop(ifcode)
		return None

	#elseif
	def selseif(self):
		ifcode = isCode(spop()) # Make sure it is code (a list)
		if chBool(spop()):
			evalLoop(ifcode)
		else:
			evalLoop(spop())	
		return None

	'''
		Dictionary Operators
	'''

	#Adds a new dictionary to the top of the stack
	def dictz (self):
		newDict = dict()
		dictStack.append(newDict)

	#Wasn't sure how this is supposed to be different
	def begin (self):
		dictz ()

	def end (self):
		if(len(dictStack) > 0):
			dictStack.pop()

	'''
		Variable Operations
	'''

	#Defines a key variable with a given value
	def sdef (self):
		if slen() >= 2:
			name = spop ()
			value = spop ()
			dictStack[-1][name] = value
		
	'''
		Stack Operations
	'''	

	#Prints out contents of the stack without changing it
	def sprint (self):
		for i in mainStack:
			print (i)

	#Prints the top item in the stack
	def top (self):
		print (mainStack[-1])
		

if __name__ == "__main__":
	fileContents = open(sys.argv[1]).readlines()
	parser = SPSParser ()
	parser.parseProgram (fileContents)
	parser.execute ()
