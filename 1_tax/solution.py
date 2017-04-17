
test = {"James": 20500, "Mary": '500', "Evan": 70000}
def calculate_tax(taxpayers):
	if isinstance(taxpayers,int):
		raise ValueError("Invalid input of type int not allowed")
		return

	result = {}
	for taxpayer in taxpayers:
		name = taxpayer
		income = taxpayers[taxpayer]

		if(isinstance(income,str)):
			raise ValueError("Allow only numeric input")
			return

		total_tax = 0

		if (1001 <= income <= 10000) or (income > 10000):
			if income < 10000:
				taxable = income - 1000
				total_tax = total_tax + (taxable*.1) 

			else:
				total_tax = total_tax + (9000*.1)
		
		if (10001 <= income <= 20200) or (income > 20200):
			if income < 20200:
				taxable1 = income - 10000
				total_tax = total_tax + (taxable1*.15)
			else:
				total_tax = total_tax + (10200*.15)		

		if (20201 <= income <= 30750) or (income > 30750):
			if income < 30750:
				taxable2 = income - 20200
				total_tax = total_tax + (taxable2*.2)
			else:
				total_tax = total_tax + (10550*.2)		

		if(30751 <= income <= 50000) or (income > 50000):
			if income < 50000:
				taxable3 = income - 30750
				total_tax = total_tax + (taxable3*.25)
			else:
				total_tax = total_tax + (19250*.25)		

		if income > 50000:
			taxable4 = income - 50000
			total_tax = total_tax + (taxable4*.3)

		result[name] = total_tax
	
	return result

calculate_tax(test)
