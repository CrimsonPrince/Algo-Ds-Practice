list = [1,2,3,4,5,6,7,7,8,8,9,11]

for i in range(len(list) -1):

	if list[i+1] - list[i] > 1:
		print(list[i] + 1)
