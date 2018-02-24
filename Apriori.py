from collections import defaultdict

class Apriori:
	def __init__(self, minSupport=0.3, minConfidence=0.6):
		self.K_itemsets = dict()
		self.frequency_of_itemset = defaultdict(int)
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
		
			return transactions

	def get_one_itemset(self, transactions):
		one_itemset = set()
		for transaction in transactions:
			for item in transaction:
				one_itemset.add(frozenset([item]))
		return one_itemset

	def get_min_supp_itemsets(self, k_itemsets, transactions):
		"""
		k_itemsets: list of k-itemsets
		"""
		temp_freq = defaultdict(int)
		temp = 0
		for transaction in transactions:
			for itemset in k_itemsets:
				if (itemset.issubset(transaction)):
					temp_freq[itemset] += 1
					self.frequency_of_itemset[itemset] += 1

		N = len(transactions)
		result = [itemset for itemset, freq in temp_freq.items() if freq/N > self.minSupport]
		return set(result)

	def apiori(self, transactions):
		L1 = self.get_one_itemset(transactions)
		# print(L1)
		C1 = self.get_min_supp_itemsets(L1, transactions)
		# print(C1)


if __name__ == '__main__':
	in_transaction_file = "./groceries.csv"
	minSupport = 0.06
	minConfidence = 0.67

	ap = Apriori(minSupport, minConfidence)
	transactions = ap.read_transactions_from_file(in_transaction_file)
	ap.apiori(transactions)