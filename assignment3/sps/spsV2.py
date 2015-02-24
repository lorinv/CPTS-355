import sys
import re

class SPSParser:

	def __init__ (self):
		#User defined functions and procedures
		self.userDictionary = {}
		#PS operations
		self.systemDictionary = {'def':self.define, 'add':self.add, 'sub':self.sub, 'mul':self.mul,
			'div':self.div, 'eq':self.eq, 'lt':self.lt, 'gt':self.gt, 'sand':self.sand, 
			'sor':self.sor, 'snot':self.snot}
		#Stack of dictionaries
		self.dictStack = [self.systemDictionary, self.userDictionary]
		#Current program stack
		self.stack = []
		# Helps keep track of current scope
		self.scope = 0
		# Helps store operations
		self.tempList = []

	def slen (self):
		return len(self.stack)

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
			self.spush(self.spop()+self.spop())
		else:
			return None

	#Subtraction
	def sub(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			self.spush(int(firstOperand)-int(secondOperand))
		else:
			return None

	#Multiplication
	def mul(self):
		if self.slen() >= 2:
			self.spush(self.spop() * self.spop())
		else:
			return None

	#Division
	def div(self):
		if self.slen() >= 2:
			secondOperand = self.spop()
			firstOperand = self.spop()
			self.spush(firstOperand / secondOperand)
		else:
			return None

	def parseInput (self, line):
		tokens = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", line) 
		return tokens

	def isNum (self, item):
		try:
			item = float(item)
			return True
		except:
			return False
	
	def spush (self, item):
		self.stack.append(item)

	def spop (self):	
		if len(self.stack) > 0:
			return self.stack.pop()
		else:
			print("Error! Out of values!")

	def isOper (self, item):
		for i in self.dictStack:
			if item in i:
				return True
		return False

	def operate (self, operation):
		for current in reversed(self.dictStack):
			if operation in current:
				current[operation]()
				break

	#######################Needs to be finished
	def storeOperation (self, item):
		#probably need to store operations as a list in itself...
		pass

	def isVar (self, item):
		if item[0] == '/':
			return True
		else:
			return False

	#####################Needs to be finished
	def ifStatement (self):
		operationList = self.spop()
		boolean = self.spop()
		var1 = self.spop()
		var2 = self.spop()
		if self.systemStack[boolean](var1, var2):
			#do operation
			pass	
	
	def storeList (self):
		self.stack.append(self.tempList)
		self.tempList = []

	def sprint (self):
		print("Current Operating Stack: " + str(self.stack))
		print("Current User Dictionary: " + str(self.userDictionary))

	def define (self):
		value = self.spop()
		self.dictStack[-1][self.spop()] = value

	def	evalStack (self, tokens):
		p = 0
		while p < len(tokens):
			t = tokens[p]
			p += 1

			if t == '}':
				self.scope -= 1
				if scope == 0:
					self.storeList ()

			elif self.scope > 0:
				self.tempList.append(t)		

			# handle number, push to the stack
			elif self.isNum (t) or self.isVar (t):
				self.spush(t) 

			# handle operator, execute operator
			elif self.isOper (t):
				self.operate(t)

			elif t == '{':
				self.scope += 1

			else:
				self.operate(t)

if __name__ == "__main__":
	fileContents = open(sys.argv[1]).readlines()
	parser = SPSParser ()
	for line in fileContents:
		tokens = parser.parseInput(line)
		parser.evalStack(tokens)
	parser.sprint()
