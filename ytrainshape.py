# Load the training data from data_train.npy
data_train = np.load('data_train.npy')

# Assuming data_train.npy contains both input (X_train) and output (y_train) data
# If the data is not structured this way, adjust accordingly
X_train = data_train[:, :n_steps_in]  # Assuming the input data is the first n_steps_in columns
y_train = data_train[:, n_steps_in:]  # Assuming the output data is the remaining columns

# Print the shape of y_train to verify its size
print(y_train.shape)

# Reshape X_train to match the expected input shape of the model
X_train = X_train.reshape(-1, n_steps_in, num_channels)

# Reshape y_train to match the expected output shape of the model
y_train = y_train.reshape(-1, n_steps_out)
