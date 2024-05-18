import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

num_channels = 1  
n_steps_in = 100

# Load the training data from data_train.npy
data_train = np.load('data_train.npy')

# Assuming data_train.npy contains both input (X_train) and output (y_train) data
# If the data is not structured this way, adjust accordingly
X_train = data_train[:, :n_steps_in]  # Assuming the input data is the first n_steps_in columns
y_train = data_train[:, n_steps_in:]  # Assuming the output data is the remaining columns

# Reshape X_train to match the expected input shape of the model
X_train = X_train.reshape(-1, n_steps_in, num_channels)

# Adjust n_steps_out based on the actual number of output steps in your training data
n_steps_out = y_train.shape[1]  # This will set n_steps_out to the second dimension of y_train

# Define the model
model = models.Sequential([
    layers.Input(shape=(n_steps_in, num_channels)), 
    layers.Conv1D(filters=64, kernel_size=3, activation='relu'),  
    layers.MaxPooling1D(pool_size=2), 
    layers.Flatten(),
    layers.Dense(64, activation='relu'),  
    layers.Dropout(0.5),  
    layers.Dense(n_steps_out)  # Update the number of units in the output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10, validation_split=0.2)  # You can adjust validation_split as needed

# Save the weights
model.save_weights('model_weights.weights.h5')
