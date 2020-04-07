import sklearn.datasets
from sklearn.svm import SVC
import pickle

# create iris model
iris = sklearn.datasets.load_iris()
clf = SVC()
model = clf.fit(iris.data, iris.target)
with open('model.pkl', mode='wb') as fp:
    pickle.dump(model, fp)
