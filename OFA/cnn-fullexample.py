#example of a cnn for image classification
from numpy import unique
from numpy import argmax
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from matplotlib import pyplot

#load dataset
(x_train, y_train), (x_test, y_test) = load_data()

temp_imgtoshow = x_train[3]
#reshape data to have a single channel
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))
x_test = x_test.reshape((x_test.shape[0],x_test.shape[1], x_test.shape[2], 1))

#determine the shape of the input images
in_shape = x_train.shape[1:]

#determine the number of classes
n_classes = len(unique(y_train))
print(in_shape, n_classes)

#normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

#define the model
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', input_shape=in_shape))
model.add(MaxPool2D((2,2)))
model.add(Flatten())
model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax'))

#define model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#fit the model
model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=0)

#evaluate the model
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print('Accuracy: %.3f' % acc)

#Make a prediction
image = x_train[3]
pyplot.subplot(1, 1, 1)
pyplot.imshow(temp_imgtoshow,  cmap=pyplot.get_cmap('gray'))
pyplot.savefig("example1.png")
# tf.keras.preprocessing.image.save_img()
yhat = model.predict([[image]])
print('Predicted: class=%d' % argmax(yhat))

#summarize model
model.summary()

#serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
#serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")