from __future__ import absolute_import, division, print_function, unicode_literals
try:
 import tensorflow.compat.v2 as tf
except Exception:
    pass 

tf.enable_v2_behavior()
print(tf.__version__)


### Sequential Model API - Simple
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense

# #define the model
model = Sequential()
model.add(Dense(10, input_shape=(8,)))
model.add(Dense(1)) #dense parameter: units - the positive integer that indicated the dimensionality of the output shape

### Functional Model API - Advanced
from tensorflow.keras.models import Model
from tensorflow.keras import Input 
from tensorflow.keras.layers import Dense

#define the layers
x_in = Input(shape=(8,))
x = Dense(10)(x_in)
x_out = Dense(1)(x)

takis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(takis[5:])
#define the model
model = Model(inputs = x_in, outputs=x_out)
