'''
	Lorin Vandegrift
	11354621
	Notes:
		- 24 hour extention allowed
		- I know that nest {} don't function
		- The test file I provided works perfectly
		- Thanks for grading this!
'''

import sys
import re
import types

class SPSParser:

	def __init__ (self):
		#User defined functions and procedures
		self.userDictionary = {}
		#PS operations
		self.systemDictionary = {'def':self.define, 'add':self.add, 'sub':self.sub, 'mul':self.mul,'div':self.div, 'eq':self.eq, 'lt':self.lt, 'gt':self.gt, 'sand':self.sand,'sor':self.sor, 'snot':self.snot, 'if':self.sif, 'clear':self.clear, 'ifelse':self.ifelse, 'dub':self.dub, 'dictz':self.dictz, 'begin':self.begin, 'end':self.end, "=":self.printTop, "stack":self.printStack}
		#Stack of dictionaries
		self.dictStack = [self.systemDictionary, self.userDictionary]
		#Current program stack
		self.stack = []
		# Helps keep track of current scope
		self.scope = 0
		# Helps store operations
		self.tempList = []

	def printEverything (self):
		self.printTop()
		self.printStack()
		for i in reversed(self.dictStack):
			print(i.keys())
			print("----------------")

	def printTop (self):
		print (self.stack[-1])

	def dictz (self):
		newDict = {}
		self.dictStack.append(newDict)

	# Puts new dictionary on dictionary stack	
	def begin (self):
		newDict = {}
		self.dictStack.append(newDict)

	# Removes the top dictionary from the stack
	def end (self):
		if len(self.dictStack) > 2:
			self.dictStack.pop()

	# Exchanges the top two values on the stack
	def exch (self):
		temp = self.stack[-1]
		self.stack[-1] = self.stack[-2]
		self.stack[-2] = temp

	# Dublicates the top value on the stack
	def dub (self):
		self.stack.append(self.stack[-1])

	# Clears the stack
	def clear (self):
		self.stack = []

	# if Statement
	def sif (self):
		if self.slen() > 2:
			oper = self.spop()
			bools = self.spop()
			if bools == 'true':
				self.subOp(oper)

	# if else statement
	def ifelse (self):
		if self.slen() > 3:
			els = self.spop()
			oper = self.spop()
			bools = self.spop()
			if bools == 'true':
				self.subOp(oper)
			else:
				self.subOp(els)
				
	# Preforms sub operations
	def subOp (self, subOp):
		self.evalStack(subOp)

	# Returns the size of the stack
	def slen (self):
		return len(self.stack)

	# Returns if the item is of boolean value
	def isBool (self, item):
		#bools = ['gt','lt','eq','sor','sand','snot']
		#return (item in bools)
		return (item == 'true' or item == 'false')
	
		#And
	def sand(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			if self.isBool(firstOperand) and self.isBool(secondOperand):
				if firstOperand == 'true' and secondOperand == 'true':
					self.spush('true')	
				else:
					self.spush('false')
			else:
				print("Not Boolean")
		return None

	#Or
	def sor(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			if self.isBool(firstOperand) and self.isBool(secondOperand):
				if firstOperand == 'true' or secondOperand == 'true':
					self.spush('true')	
				else:
					self.spush('false')
			else:
				print("Not Boolean")
		return None


	#Not
	def snot(self):
		if self.slen() >= 2:
			firstOperand = self.spop()
			if self.isBool(firstOperand):
				if firstOperand == 'true':
					self.spush('false')	
				else:
					self.spush('true')
			else:
				print("Not Boolean")
		return None

	#Equals
	def eq(self):
		if self.slen() >= 2:
			if self.spop() == self.spop():
				self.spush('true')
			else:
				self.spush('false')
		return None

	#Less than
	def lt(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			if firstOperand < secondOperand:
				self.spush('true')
			else:
				self.spush('false')
		return None

	#Greater Than
	def gt(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			if firstOperand > secondOperand:
				self.spush('true')
			else:
				self.spush('false')
		return None

	#Addition
	def add(self):
		if self.slen() >= 2:
			self.spush(float(self.spop())+float(self.spop()))
		else:
			return None

	#Subtraction
	def sub(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			self.spush(float(firstOperand)-float(secondOperand))
		else:
			return None

	#Multiplication
	def mul(self):
		if self.slen() >= 2:
			self.spush(float(self.spop()) * float(self.spop()))
		else:
			return None

	#Division
	def div(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			self.spush(float(firstOperand) / float(secondOperand))
		else:
			return None

	#Parses input into tokens
	def parseInput (self, line):
		tokens = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", line) 
		return tokens

	# Checks if item is a number
	def isNum (self, item):
		try:
			item = float(item)
			return True
		except:
			return False
	
	# Pushes the item onto the stack
	def spush (self, item):
		self.stack.append(item)

	# Pops a item off the stack
	def spop (self):	
		if len(self.stack) > 0:
			return self.stack.pop()
		else:
			print("Error! Out of values!")

	# Checks if the name is a function
	def isOper (self, item):
		for i in self.dictStack:
			if item in i:
				return True
		return False

	# Preform the function given it's name
	def operate (self, operation):
		for current in reversed(self.dictStack):
			if operation in current:
				current[operation]()
				break

	# Returns the variable given it's name
	def getVar (self, item):
		for current in reversed(self.dictStack):
			if item in current:
				if type(current[item]) == list:
					self.subOp(current[item])
				else:
					return current[item] 
				break

	# Checks if name is a variable
	def isVar (self, item):
		if item[0] == '/':
			return True
		else:
			if self.isOper('/' + str(item)):
				temp = self.getVar('/'+str(item))
				if temp != None:
					self.spush(temp)
				return False
	
	# Stores list in stack
	def storeList (self):
		self.stack.append(self.tempList)
		self.tempList = []

	# Prints the current stack
	def printStack (self):
		print("Current Operating Stack: " + str(self.stack))
		print("Current User Dictionary: " + str(self.userDictionary))

	# defines a new variable
	def define (self):
		value = self.spop()
		key = self.spop()
		self.dictStack[-1][key] = value

	# Evaluates the stack
	def	evalStack (self, tokens):
		p = 0
		while p < len(tokens):
			t = tokens[p]
			p += 1

			if t == '}':
				self.scope -= 1
				if self.scope == 0:
					self.storeList ()

			elif t == '{':
				self.scope += 1

			elif self.scope > 0:
				self.tempList.append(t)
						

			# handle number, push to the stack
			elif self.isNum (t) or self.isVar (t):
				self.spush(t) 

			# handle operator, execute operator
			elif self.isOper (t):
				self.operate(t)


			else:
				self.operate(t)

if __name__ == "__main__":
	fileContents = open(sys.argv[1]).readlines()
	parser = SPSParser ()
	for line in fileContents:
		tokens = parser.parseInput(line)
		parser.evalStack(tokens)
	parser.printEverything()
