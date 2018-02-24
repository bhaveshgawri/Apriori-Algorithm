from collections import defaultdict
from itertools import combinations

class Apriori:
	def __init__(self, minSupport=0.015, minConfidence=0.4):
		self.K_itemsets = dict()
		self.support_count = defaultdict(int)
		self.minSupport = minSupport
		self.minConfidence = minConfidence

	def read_transactions_from_file(self, transaction_file):
		"""
		Desc: Reads the transaction file and returns a list
		of transactions. Each transaction is represented as a
		'set' of items.
		"""
		with open (transaction_file, 'r') as infile:
			transactions = [set(line.rstrip('\n').split(',')) 
							for line in infile]
		
			return transactions

	def get_one_itemset(self, transactions):
		one_itemset = set()
		for transaction in transactions:
			for item in transaction:
				one_itemset.add(frozenset([item]))
		return one_itemset

	def self_cross(self, Ck, itemset_size):
		result = {itemset1.union(itemset2) 
					for itemset1 in Ck for itemset2 in Ck 
					if len(itemset1.union(itemset2)) == itemset_size}
		return result

	def prune_Ck(self, Ck, Lk, itemset_size):
		Ck_ = set()
		for itemset in Ck:
			subsets_of_itemset = list(combinations(itemset, itemset_size-1))
			flag = 0
			for subset in subsets_of_itemset:
				if not frozenset(subset) in Lk:
					flag = 1
					break
			if flag == 0:
				Ck_.add(itemset)
		return Ck_

	def get_min_supp_itemsets(self, Ck, transactions):
		"""
		Ck: candidate itemset with itemsets of width k
		"""
		temp_freq = defaultdict(int)
		for transaction in transactions:
			for itemset in Ck:
				if itemset.issubset(transaction):
					temp_freq[itemset] += 1
					self.support_count[itemset] += 1

		N = len(transactions)
		result = [itemset for itemset, freq in temp_freq.items() 
					if freq/N > self.minSupport]
		return set(result)

	def apiori(self, transactions):
		Ck = self.get_one_itemset(transactions)
		Lk = self.get_min_supp_itemsets(Ck, transactions)
		k = 2
		while len(Lk) != 0:
			self.K_itemsets[k-1] = Lk
			Ck = self.self_cross(Lk, k)
			print(k, len(Ck))
			Ck = self.prune_Ck(Ck, Lk, k)
			print(k, len(Ck))
			Lk = self.get_min_supp_itemsets(Ck, transactions)
			print(k, len(Lk))
			k += 1
		
		# for key, set_ in self.K_itemsets.items():
		# 	for item in set_:
		# 		print(item, self.support_count[item])

if __name__ == '__main__':
	in_transaction_file = "./groceries.csv"
	# minSupport = 0.005
	# minConfidence = 0.67

	ap = Apriori()
	# ap = Apriori(minSupport, minConfidence)
	transactions = ap.read_transactions_from_file(in_transaction_file)
	ap.apiori(transactions)