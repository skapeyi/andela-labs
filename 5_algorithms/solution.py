def binary_converter(number):
	if not isinstance(number,int):
		
		return "Invalid input"
	if 0> number or 255 < number:
		
		return ("Invalid input")

	binary_list = []
	binary_string = ''

	if number == 0:
		return str(0)

	while number > 0:
		value = number%2
		number = number//2
		binary_list.append(value)

	binary_list_lenght = len(binary_list) - 1
	while binary_list_lenght >= 0:
		binary_string += str(binary_list[binary_list_lenght])
		binary_list_lenght -= 1
	
	return (binary_string)
	

binary_converter(62)