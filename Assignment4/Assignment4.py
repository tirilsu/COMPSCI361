import sys
print(sys.version)

import pandas as pd
import collections
from collections import Counter  

training_set = pd.read_csv("trg.csv")
#target = training_set['class']

Prob_A = (training_set['class'] == 'A').sum()/training_set.shape[0]
Prob_B = (training_set['class'] == 'B').sum()/training_set.shape[0]
Prob_E = (training_set['class'] == 'E').sum()/training_set.shape[0]
Prob_V = (training_set['class'] == 'V').sum()/training_set.shape[0]


file_A = ""
file_B = ""
file_E = ""
file_V = ""

"""fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        numFiles.append(fileNames)

for i in numFiles:
    file = open(os.path.join(pathName, i), "rU")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        for column in row:
            print(column)
            if column=="A": """
num_A = 0
num_B = 0
num_E = 0
num_V = 0

for index,row in training_set.iterrows():
	if row['class'] == 'A':
		file_A = file_A + row.abstract
		num_A = num_A + 1
	elif row['class'] == 'B':
		file_B = file_B + row.abstract
		num_B = num_B + 1
	elif row['class'] == 'E':
		file_E = file_E + row.abstract
		num_E = num_E + 1
	elif row['class'] == 'V':
		file_V = file_V + row.abstract
		num_V = num_V + 1

"""file_A = string_A.split() #split string into list
file_B = string_B.split()
file_E = string_E.split()
file_V = string_V.split()"""

file_A = file_A.replace('-',' ').split(' ')
file_B = file_B.replace('-',' ').split(' ')
file_E = file_E.replace('-',' ').split(' ')
file_V = file_V.replace('-',' ').split(' ')

#dict_A = collections.Counter(file_A)
#dict_B = collections.Counter(file_B)
#dict_E = collections.Counter(file_E)
#dict_V = collections.Counter(file_V)

instance = training_set.iloc[2]

words = instance.abstract.replace('-',' ').split(' ')

counter_A = 0
counter_B = 0
counter_E = 0
counter_V = 0

for word in words:
	counter_A += file_A.count(word)
	counter_B += file_B.count(word)
	counter_E += file_E.count(word)
	counter_V += file_V.count(word)

prob_A = 1
prob_B = 1
prob_E = 1
prob_V = 1

for word in words:
	prob_A *= (file_A.count(word) + 1) / (cntA + len(set(words)))
	prob_B *= (file_B.count(word) + 1) / (cntB + len(set(words)))
	prob_E *= (file_E.count(word) + 1) / (cntE + len(set(words)))
	prob_V *= (file_V.count(word) + 1) / (cntV + len(set(words)))

prob_A *= Prob_A
prob_B *= Prob_B
prob_E *= Prob_E
prob_V *= Prob_V

print(str.format('{0:.30f}', prob_A))
print(str.format('{0:.30f}', prob_B))
print(str.format('{0:.30f}', prob_E))
print(str.format('{0:.30f}', prob_V))

prediction = 'A'
class_var = 'A'
if prob_B > prediction:
	prediction = prob_B
	class_var = 'B'
if prob_E > prediction:
	prediction = prob_E
	class_var = 'E'
if prob_V > prediction:
	prediction = prob_V
	class_var = 'V'

print('Class: ', instance['class'])
print('Prediction: ', class_var)

prior_A = 

"""
prob_A = 1
prob_B = 1
prob_E = 1
prob_V = 1

counter_A = 0
counter_B = 0
counter_E = 0
counter_V = 0

for word in file_A:
	counter_A += file_A.count(word)
for word in file_B:
	counter_B += file_B.count(word)
for word in file_E:
	counter_E += file_E.count(word)
for word in file_V:
	counter_V += file_V.count(word)

for word in file_A:
	prob_A *= (file_A.count(word) + 1) / (counter_A + len(dict_A))"""

 
