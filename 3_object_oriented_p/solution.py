class BankAccount(object):
	"""docstring for ClassName"""
	def withdraw(self):
		raise NotImplementedError 

	def deposit(self):
		raise NotImplementedError

class SavingsAccount(BankAccount):
	"""docstring for ClassName"""
	def __init__(self, opening_balance = 500):		
		self.balance = opening_balance

	def deposit(self, deposit_amount):
		if deposit_amount < 0:
			return "Invalid deposit amount"
		self.balance = self.balance + deposit_amount
		return self.balance

	def withdraw(self, withdraw_amount):
		if isinstance(withdraw_amount,str):
			raise ValueError("Invalid input of type string not allowed")
			return
		if withdraw_amount < 0:
			return ("Invalid withdraw amount")

		if withdraw_amount > self.balance:
			return "Cannot withdraw beyond the current account balance"

		if (self.balance - withdraw_amount) < 500:
			return "Cannot withdraw beyond the minimum account balance"

		self.balance -= withdraw_amount
		return self.balance

class CurrentAccount(BankAccount):
	def __init__(self, opening_balance = 0):
		self.balance = opening_balance

	def deposit(self, deposit_amount):
		if deposit_amount < 0:
			return "Invalid deposit amount"
		self.balance = self.balance + deposit_amount
		return self.balance
	
	def withdraw(self, withdraw_amount):
		if withdraw_amount < 0 :
			return "Invalid withdraw amount"

		if withdraw_amount >= self.balance:
			return "Cannot withdraw beyond the current account balance"

		self.balance -= withdraw_amount
		return self.balance

		
	
		