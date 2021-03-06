import os.path
import unittest
import numpy as np
import geode

class TestChdir(unittest.TestCase):
	def setUp(self): # to get example data
		mat = []
		genes = []
		with open (os.path.join(os.path.dirname(__file__), '../examples/example_expression_data.txt')) as f:
			next(f)
			for line in f:
				sl = line.strip().split('\t')
				gene = sl[0]
				row = list(map(float, sl[1:]))
				genes.append(gene)
				mat.append(row)

		self.col_labels = ['1','1','1','2','2','2']
		self.mat = np.array(mat)
		self.genes = genes

	def test_output(self):
		output = geode.chdir(self.mat, self.col_labels, self.genes)
		self.assertEqual(len(self.genes), len(output))

if __name__ == '__main__':
	unittest.main()