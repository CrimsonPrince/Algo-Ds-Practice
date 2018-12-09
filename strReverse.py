def strReverse1(input):
	return input[::-1]

def strReverse2(input):
	return ''.join(reversed(input))

def strReverse1(input):
	reverse = list(input)
	for i in range(len(input)//2):
		tmp = reverse[i]
		reverse[i] = reverse[len(reverse) - i - 1]
		reverse[len(input) - i - 1] = tmp

	return ''.join(reverse)




print(strReverse1("TestingString"))
print(strReverse2("TestingString"))
print(strReverse1("TestingString"))
