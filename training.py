import librosa
import numpy as np 
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import train_test_split
import os
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from random import randint
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

TEST_SPLIT=0.95
directory='data/wav_data'

X= np.load('X_20_special.npy')
Y= np.load('Y_20_special.npy')

# X_single= np.load('X_single.npy')
# Y_single= np.load('Y_single.npy')
X_all= np.load('X_all.npy')
Y_all= np.load('Y_all.npy')

X=X_all
Y=Y_all

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=TEST_SPLIT, random_state=randint(0, 100))

# X_test=X_all
# Y_test=Y_all


print(X.shape)
print(X_train.shape)
print(X_test.shape)
print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)


# clf = SVC(kernel='poly')
# clf.fit(X_train, Y_train) ###
# print("svc: " + str( clf.score(X_test, Y_test) ))

# clf = MLPClassifier(hidden_layer_sizes=(2000,))
# clf.fit(X_train, Y_train) ###
# print("mlp: " + str( clf.score(X_test, Y_test) ))

# clf = LinearSVC(penalty='l2')
# clf.fit(X_train, Y_train) ###
# print("linear svc: " + str( clf.score(X_test, Y_test) ))

# clf = DecisionTreeClassifier(max_depth=2000)
# clf.fit(X_train, Y_train) ###
# print("decision tree: " + str( clf.score(X_test, Y_test) ))

# clf = KNeighborsClassifier(n_neighbors=3)
# clf.fit(X_train, Y_train) ###
# print("knn: " + str( clf.score(X_test, Y_test) ))

clf =  RandomForestClassifier(max_depth=500, n_estimators=100, max_features=20)
clf.fit(X_train, Y_train) ###
print("radnom forest: " + str( clf.score(X_test, Y_test) ))
