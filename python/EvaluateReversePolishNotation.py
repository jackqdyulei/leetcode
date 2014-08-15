"""
Comment: this is not a perfect problem because of the following weakness.
		First, the problem doesn't give enough description about the divide operation.
		Second, python and cpp deal with negative devide operation in different way. 
		In cpp 1/-6 = 0 while in python 1/-6 = -1 
Wrong Time: 2
Wrong Reason: look up the second weakness in the comment 
"""
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
    	stack = []
        for item in tokens:
        	if ( item == '+' or item == '-' or item == '*' or item == '/'):
        		number1 = stack[-2]
        		number2 = stack[-1]
        		if item == '+':
        			solu = number1 + number2
        		elif item == '-':
        			solu = number1 - number2
        		elif item == '*':
        			solu = number1 * number2
        		elif item == '/':
        			if number1 * number2 == 0:
        				solu = 0
        			elif number1 * number2 < 0 and number1 % number2 != 0:
        				solu = number1 / number2 + 1 #assume that number2 not equal zero
        			else:
        				solu = number1 / number2

        		stack = stack[:-2]
        		stack.append(solu)
        	else:
        		stack.append(int(item))

        return int(round(stack[0]))


solution = Solution()
print solution.evalRPN(["2", "1", "+", "3", "*"]) 
print solution.evalRPN(["4", "13", "5", "/", "+"])
print solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print solution.evalRPN(["4","-2","/","2","-3","-","-"])

