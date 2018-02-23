class Apriori:
	def __init__(self, minSupport=0.3, minConfidence=0.6):
		self.transactions_count = 0
		self.minSupport = minSupport
		self.minConfidence = minConfidence

	def read_transactions_from_file(self, transaction_file):
		"""
		Desc: Reads the transaction file and returns a list
		of transactions. Each transaction is represented as a
		'set' of items.
		"""
		with open (transaction_file, 'r') as infile:
			transactions = [set(line.rstrip('\n').split(',')) for line in infile]
			self.transactions_count = len(transactions)
			
			return transactions

if __name__ == '__main__':
	in_transaction_file = "./groceries.csv"
	minSupport = 0.4
	minConfidence = 0.67

	ap = Apriori(minSupport, minConfidence)
	transactions = ap.read_transactions_from_file(in_transaction_file)
	# print(ap.transactions_count)