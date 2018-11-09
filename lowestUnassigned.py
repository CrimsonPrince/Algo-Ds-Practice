def main(list):

	if len(list) == 0:
		return 1

	if len(list) == 1:
		return list[0] + 1

	current = 0
	for item in list:
		prev = current
		current = item

		if current - prev > 1:
			return prev + 1

list = [1,2,3,5]
list2 = [1,2,3,4,5,6,7,8,9,11]
list3 = []
list4 = [10]
print(main(list3))
print(main(list4))
print(main(list))
print(main(list2))
