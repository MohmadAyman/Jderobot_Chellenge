import sys
import numpy as np 
import time
import json

import unittest

class TestStringMethods(unittest.TestCase):
	test_pattern = []
	k=[]
	for i in range(5):
		for j in range(6):
			k.append(0)
		test_pattern.append(k)

	test_rules_pattern = []
	test_rules_pattern.append([0,0,0,0,0,0])
	test_rules_pattern.append([0,0,0,0,0,0])
	test_rules_pattern.append([0,0,1,1,0,0])
	test_rules_pattern.append([0,0,1,1,0,0])
	test_rules_pattern.append([0,0,0,0,0,0])
	test_rules_pattern.append([0,0,0,0,0,0])

	def test_neighbors(self):
		# no neighbors
		self.assertEqual(num_nagbours(self.test_pattern,1,1), 0)

	def test_rules(self):
		# using the stationary pattern
		np.testing.assert_array_equal(apply_rules(self.test_rules_pattern),self.test_rules_pattern)

def num_nagbours(pattern,x,y):
	return pattern[x-1][y-1]+pattern[x-1][y]+pattern[x-1][y+1]+pattern[x][y-1]+pattern[x][y+1]+pattern[x+1][y-1]+pattern[x+1][y]+pattern[x+1][y+1]

def apply_rules(pattern):
	new_pattern = np.array(pattern)
	rows = new_pattern.shape[0]
	cols = new_pattern.shape[1]
	print(rows-2)
	for x in range(rows-2):
		for y in range(cols-2):
			# print(new_pattern)
			if(pattern[x+1][y+1]==1):
				if(num_nagbours(pattern,x+1,y+1)<2):
					new_pattern[x+1][y+1]=0
				elif(num_nagbours(pattern,x+1,y+1)==2 or num_nagbours(pattern,x+1,y+1)==3):
					new_pattern[x+1][y+1]=1
				elif(num_nagbours(pattern,x+1,y+1)>3):
					new_pattern[x+1][y+1]=0
			else:
				if(num_nagbours(pattern,x+1,y+1)==3):
					new_pattern[x+1][y+1]=1
			# print(new_pattern)
	print(new_pattern)
	return new_pattern


if __name__ == '__main__':
	with open('config.json') as data_file:
		config = json.load(data_file)

	# for testing mode change the test variable in the config file
	if(config["test"]=="false"):
		speed=config["speed"]
		print(speed)
		print('Enter the size of the game first, cols -> rows')
		cols = int(input('cols'))
		rows = int(input('rows'))
		pattern=[]
		row=0
		while(1):
			inp = []
			inp.append(0)
			for i in input():
				inp.append(int(i))
			my_array = np.array(inp)
			if(len(inp)-1 == cols):
				inp.append(0)
				pattern.append(inp)
				row+=1
			else:
				inp.clear()
				print('dim invalid, retry')
			if(rows==row):
				break

		while(1):
			time.sleep(speed)
			pattern = apply_rules(pattern)
	else:
		unittest.main()
