import numpy as np
from tensorflow.keras.models import model_from_json
import tensorflow as tf

# Define the custom loss function
def custom_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Load the validation data
data_val = np.load('data_val.npy')

# Load the model architecture from JSON file
with open('model_architecture.json', 'r') as json_file:
    model_json = json_file.read()
model = model_from_json(model_json)

# Load the model weights
model.load_weights('model_weights.weights.h5')

# Compile the loaded model with the custom loss function
model.compile(optimizer='adam', loss=custom_loss)

# Assuming you have defined n_steps_in and num_channels somewhere in your code
n_steps_in = 100
num_channels = 1

# Assuming you have defined X_val somewhere in your code
X_val = data_val[:, :n_steps_in]  # Assuming the input data is the first n_steps_in columns
X_val = X_val.reshape(-1, n_steps_in, num_channels)

# Assuming you have defined y_val somewhere in your code
y_val = data_val[:, n_steps_in:]  # Assuming the output data is the remaining columns

# Evaluate the model on the validation data
loss = model.evaluate(X_val, y_val)

print("Validation Loss:", loss)
