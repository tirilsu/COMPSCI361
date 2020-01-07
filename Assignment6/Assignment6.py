import pandas as pd
import numpy as np
from skmultiflow.data import DataStream
from skmultiflow.trees import HAT
from scipy.io import arff
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from skmultiflow.evaluation import EvaluatePrequential
from skmultiflow.trees import HoeffdingTree
from skmultiflow.bayes import NaiveBayes
from skmultiflow.lazy.knn_adwin import KNNAdwin

# 1. Create a stream
data = arff.loadarff('elecNormNew.arff')
df = pd.DataFrame(data[0])
enc = LabelEncoder()
class_num = enc.fit_transform(df["class"])
stream = DataStream(df.drop(["class"], axis = 1), y = class_num)
stream.prepare_for_use()

# 2. Instantiate the HoeffdingTree and NaiveBayes classifiers
hat = HAT(nominal_attributes = [1,8])
ht = HoeffdingTree(nominal_attributes = [1,8])
nb = NaiveBayes(nominal_attributes = [1,8])
knn_adwin = KNNAdwin(n_neighbors=8, leaf_size=40, max_window_size=2000,nominal_attributes = [1,8])

# Pre training the classifier with 200 samples
X, y = stream.next_sample(200)
knn_adwin = knn_adwin.partial_fit(X, y)


# 3. Setup evaluator
evaluator = EvaluatePrequential(show_plot = True, n_wait = 500, max_samples = 1000000)

# 4. Run evaluation
#print("----Evaluating HoeffdingTree----")
#evaluator.evaluate(stream = stream, model = ht)
#evaluator.evaluate(stream = stream, model = hat)
#print("--------------------------------")
#print()

#print("----Evaluating HoeffdingTree----")
#evaluator.evaluate(stream = stream, model = knn_adwin)
#evaluator.evaluate(stream = stream, model = hat)
#print("--------------------------------")

print("----Evaluating NaiveBayes----")
evaluator.evaluate(stream = stream, model = nb)
print("--------------------------------")
