
print("starting")
def manipulate_data(list_item):
	if not isinstance(list_item, list):
		raise ValueError('Only lists allowed')

	positive_sum = 0
	negative_sum = 0
	result = []

	for item in list_item:
		if not isinstance(item,int):
			raise ValueError("Only integers can be summed")

		if item >= 0:
			positive_sum += 1

		if item < 0:
			negative_sum += item

	result.append(positive_sum)
	result.append(negative_sum)
	return result



manipulate_data([1, -9, 2, 3, 4, -5])

