from __future__ import absolute_import, division, print_function, unicode_literals
try:
 import tensorflow.compat.v2 as tf
except Exception:
    pass 

tf.enable_v2_behavior()
print(tf.__version__)
print("hi")
print("oeoeoe")
# print(tensorflow.__version__)
# print("helloaaaa")

### Functional Model API - Simple
# from tensorflow.keras import Sequential 
# from tensorflow.keras.layers import Dense

# #define the model
# model = Sequential()
# model.add(Dense(10, input_shape=(8,)))
# model.add(Dense(1))
# model.add(Dense(1))
