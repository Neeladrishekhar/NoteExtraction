import librosa
import numpy as np 
from sklearn.svm import LinearSVC
import os

hop_length = 256


# print(data.shape)

directory='data/wav_data'
# X=np.array([])
Y=[]

i=0
tmpss=1
for filename in os.listdir(directory):
	i=i+1
	if i%50==0:
		print(str(i))
	temp=filename.split('_')
	if(len(temp)==3):
		chord_name = temp[0]+'#'+temp[1]
	else:
		chord_name = temp[0]
	
	if(int(temp[-1].split('.')[0])%2!=0):
		continue

	y, sr = librosa.load(os.path.join(directory, filename))
	mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
	A = np.asarray(mfcc).reshape(-1)
	mfcc_delta = librosa.feature.delta(mfcc)
	A_delta = np.asarray(mfcc_delta).reshape(-1)
	features= np.concatenate((A, A_delta), axis=0)
	if(tmpss==1):
		X=features
		tmpss=2
	else:
		X=np.vstack([X,features])
	Y.append(chord_name)
	
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(Y)
Y=le.transform(Y) 

np.save("X_40_special", X)
np.save("Y_40_special", Y)

data= np.load('X_40_special.npy')
print(data.shape)

data= np.load('Y_40_special.npy')
print(data.shape)


# classifier = LinearSVC(penalty='l1', dual=False)
# classifier.fit(v_train, train_data.target) ###
# predicted = classifier.predict(v_test) ####
