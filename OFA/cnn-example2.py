from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets.mnist import load_data
from numpy import unique
from numpy import argmax
from matplotlib import pyplot
import os

#load dataset
(x_train, y_train), (x_test, y_test) = load_data()

#Reshaping & Normalizing of Images
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))
x_test = x_test.reshape((x_test.shape[0],x_test.shape[1], x_test.shape[2], 1))
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
imgArray = []
#image to be evaluated by model
#x_test_img = x_train[0]
for i in range(0,25):
    imgArray.append(x_test[i])

#load json file
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

#evaluate loaded model on test data
loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
score = loaded_model.evaluate(x_train, y_train,verbose=0)
for i in range(0,imgArray.__len__()):
   x_test_img = imgArray[i]
   yhat = loaded_model.predict([[x_test_img]])
   print('Predicted: class=%d' % argmax(yhat))
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
print("%s: %.2f%%" % (loaded_model.metrics_names[0], score[0]*100))
#summary of model
loaded_model.summary()