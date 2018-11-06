def reverse(s):
	return(s[::-1])

def reverse2(s):
	return(''.join(reverse(s)))

def reverse3(s):
	length = len(s)
	char = list(s)
	for i in range(len(s) //2):
		tmp = char[i]
		char[i] = char[length - 1 - i]
		char[length - 1 -i] = tmp
