from sklearn.svm import SVC
import pickle
from address import *

class VoiceModel:
    def __init__(self):
        self.model = SVC(kernel='linear', probability=True)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def save_model(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, file_path):
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)