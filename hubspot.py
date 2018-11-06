sum = 8

def sumArray(tmp):

	for i in range(0,len(tmp)):

		for j in range(0 + i, len(tmp)):
			if tmp[i] == tmp[j]:
				continue
			if tmp[i] + tmp[j] == sum:
				print(tmp[i],tmp[j])



def main():
	input = [9,4,42,6,-1,2]
	sumArray(input)

main()
