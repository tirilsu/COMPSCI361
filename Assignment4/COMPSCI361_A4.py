import sys
print(sys.version)

import pandas as pd

import collections
from collections import Counter  

import numpy as np

training_set = pd.read_csv('trg.csv')
test_set = pd.read_csv('tst.csv')

words = {'A': 0, 'B': 0,'E': 0,'V': 0}

#saving frequency of words
dictionary = {'A': {},'B': {},'E': {},'V': {} }

"""
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

"""

counter = {'A': 0,'B': 0,'E': 0,'V': 0,'sum': 0,} 

c = 0

#training model
def train_data(data,c,counter,dictionary,words):
	for index, row in data.iterrows():
		training_column = row['class']
		counter[training_column]+=1
		counter['sum']+=1

		abstract = row['abstract'].replace('-',' ').split(' ') #preprocessing
		for word in abstract:

			words[training_column] += 1

			if word not in dictionary[training_column]:
				dictionary[training_column][word] = 1
				c += 1
			else:
				dictionary[training_column][word] += 1

	return c,counter,dictionary

#classifying data
def classify_data(data,c,counter,dictionary,words):
	prediction = []

	"""
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

	"""
	for index, row in data.iterrows():
		count_A = np.log(counter['A']/counter['sum'])

		count_B = np.log(counter['B']/counter['sum'])

		count_E = np.log(counter['E']/counter['sum'])

		count_V = np.log(counter['V']/counter['sum'])

		abstract = row['abstract'].replace('-',' ').split(' ')
		abs_V = c
		for word in abstract:

			#Laplace smoothing
			if word in dictionary['A']:
				count_A += np.log((dictionary['A'][word] + 1)/(words['A'] + abs_V))
			elif word in dictionary['B']:
				count_B += np.log((dictionary['B'][word] + 1)/(words['B'] + abs_V))
			elif word in dictionary['E']:
				count_E += np.log((dictionary['E'][word] + 1)/(words['E'] + abs_V))
			elif word in dictionary['V']:
				count_V += np.log((dictionary['V'][word] + 1)/(words['V'] + abs_V))

		count_class = {'A': count_A,'B': count_B,'E': count_E,'V': count_V} 
		print(count_class)
		prediction.append(min(count_class,key=count_class.get))

	return prediction

c, counter, dictionary = train_data(training_set,c,counter,dictionary,words)
prediction = classify_data(training_set,c,counter,dictionary,words)

print(counter)

print('Accuracy: ', (training_set['class'] == prediction).sum() / len(prediction), '%')

c, counter, dictionary = train_data(training_set,c,counter,dictionary,words)
prediction = classify_data(test_set,c,counter,dictionary,words)
test_set['class'] = prediction
test_set.drop(['abstract'],axis=1).to_csv('kaggle_submission.csv',index=False)
