'''
Lorin Vandegrift
2/7/2015

Assigment 1:
	-- Number Operations: add, sub, mul, div, eq, lt, gt
	-- Boolean Operators: and, or, not
	Sequencing Operators: if, ifelse
	-- Create Dictionary: dictz (No operands)
	-- Stack Operations: begin, end
	-- Name definition: def (takes value and name)
	-- entire stack printing: stack
	-- top-of-stack printing operator: = 
	
'''

import sys
import re

#Program Variables
# The User Dictionary is checked before the system dictionary
# If the name is in the dictionary, it either pushes the value onto the stack
# preforms the operation
# Else, it raises an error

#All Dictionaries are kept on the dictionary stack
systemDictionary = {'add':add, 'sub':sub, 'mul':mul, 'div':div, 'eq':eq, 'lt':lt, 'gt':gt}
userDictionary = {}
dictStack = [userDictionary, systemDictionary]

if __name__ == "__main__":
	fileContents = open(sys.argv[1]).readlines()

#Setup Dictionaries and other variables
def init():
	pass

'''
	Parsing the PostScript
'''

def evalLoop (tokens):
	p = 0 # control the loop by idex p
	while p < len(tokens):
		t = tokens[p]
		p += 1
	# handle number, push to the stack
	# handle operator, execute operator
	# handle {
	# push everything between { and } to the stack
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

def parseProgram (fileContents):
	pass

'''
	Dictionary Operations
'''

#Adds new item to the stack
def spush(item):
	stack.append(item)		
	return None

#Removes Item from the top of the stack
#Throws error is the stack is empty
def spop():
	if not stack:		
		err("Error in pop: Stack is empty...")
		return None
	else:					
		return stack.pop()

#Returns the number of items in the stack
def slen():
	pass

#Empties the stack
def sclear():
	pass

#Duplicates the top item on the stack
def dup():
	pass

#Exhanges the top two item on the stack
def exch():
	pass

'''
	Utility Functions
'''

#Check if item is a number
def isNum(item):
	if isinstance(item, float):
		return item
	else:
		err("Variable not a float.")

def isDict(item):
	if isinstance(item, dict):
		return item
	else:
		err("Variable not a dictionary.")



'''
	Math Operations
'''

#Addition
def add():
	if slen() >= 2:
		spush(spop()+spop())
	else:
		return None

#Subtraction
def sub():
	if slen() >= 2:
		secondOperand = spop()
		firstOperand = spop()
		spush(firstOperand-secondOperand)
	else:
		return None

#Multiplication
def mul():
	if slen() >= 2:
		spush(spop() * spop())
	else:
		return None

#Division
def div():
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
def eq():
	if slen() >= 2:
		if spop() == spop():
			spush('true')
		else:
			spush('false')
	return None

#Less than
def lt():
	if slen() >= 2:
		secondOperand = spop()
		firstOperand = spop()
		if firstOperand < secondOperand:
			spush('true')
		else:
			spush('false')
	return None

#Greater Than
def gt():
	if slen() >= 2:
		secondOperand = spop()
		firstOperand = spop()
		if firstOperand > secondOperand:
			spush('true')
		else:
			spush('false')
	return None

#And
def sand():
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
def sor():
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
def snot():
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
def sif():
	ifcode = isCode(spop()) # Make sure it is code (a list)
	if chBool(spop()):
		evalLoop(ifcode)
	return None

#elseif
def selseif():
	ifcode = isCode(spop()) # Make sure it is code (a list)
	if chBool(spop()):
		evalLoop(ifcode)
	else:
		
	return None

'''
	Dictionary Operators
'''

#Adds a new dictionary to the top of the stack
def dictz ():
	newDict = dict()
	dictStack.append(newDict)

#Wasn't sure how this is supposed to be different
def begin ():
	dictz ()

def end ():
	if(len(dictStack) > 0):
		dictStack.pop()

'''
	Variable Operations
'''

#Defines a key variable with a given value
def sdef ():
	if slen() >= 2:
		name = spop ()
		value = spop ()
		dictStack[-1][name] = value
	
'''
	Stack Operations
'''	

#Prints out contents of the stack without changing it
def sprint ():
	for i in mainStack:
		print i

#Prints the top item in the stack
def top ():
	print mainStack[-1]
	

