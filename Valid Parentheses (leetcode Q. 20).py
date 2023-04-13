class Solution:
	def isValid(self, s: str) -> bool:

		stack = []

		for i in s:

			if i == '(' or i == '{' or i == '[':
				stack.append(i)
			else:

				if not stack:
					return False

				st= stack.pop()

				if st == '(' and i != ')':
					return False
				if st == '{' and i != '}':
					return False
				if st == '[' and i != ']':
					return False

		if stack :
			return False
		else:
			return True
