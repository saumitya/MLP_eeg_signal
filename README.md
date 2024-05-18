# MLP_eeg_signal
# README

## Project Overview

This project is designed to build and train a neural network model for time series prediction using TensorFlow and Keras. The input data for training is assumed to be in the form of a `.npy` file (NumPy array format), specifically `data_train.npy`. The script preprocesses the data, defines a Convolutional Neural Network (CNN) model, trains it, and saves both the trained model and its architecture.

## Prerequisites

To run this project, you need the following libraries installed:
- `numpy`
- `tensorflow`
- `keras` (included within TensorFlow)

You can install the necessary libraries using pip:
```sh
pip install numpy tensorflow
```

## Data Description

The data used for training (`data_train.npy`) is expected to be in the form of a NumPy array. This array contains both the input features and the output labels for the training process. The structure of the data is as follows:
- The first `n_steps_in` columns represent the input features.
- The remaining columns represent the output labels.

### Example Data Structure
If `n_steps_in` is 100:
- Columns 0 to 99: Input features
- Columns 100 onward: Output labels

## Script Explanation

### Imports
```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import json
```
We import necessary libraries for data manipulation and model building.

### Parameters
```python
num_channels = 1
n_steps_in = 100
```
We define the number of channels (assuming univariate time series data) and the number of input steps.

### Data Loading
```python
data_train = np.load('data_train.npy')
```
We load the training data from the `data_train.npy` file.

### Data Preprocessing
```python
X_train = data_train[:, :n_steps_in]
y_train = data_train[:, n_steps_in:]

X_train = X_train.reshape(-1, n_steps_in, num_channels)
n_steps_out = y_train.shape[1]
```
We split the data into input features (`X_train`) and output labels (`y_train`). The input data is reshaped to match the expected input shape of the model.

### Model Definition
```python
model = models.Sequential([
    layers.Input(shape=(n_steps_in, num_channels)),
    layers.Conv1D(filters=64, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(n_steps_out)
])
```
We define a sequential CNN model with Conv1D, MaxPooling1D, Flatten, Dense, and Dropout layers.

### Model Compilation
```python
model.compile(optimizer='adam', loss='mse')
```
We compile the model using the Adam optimizer and Mean Squared Error (MSE) loss function.

### Model Training
```python
model.fit(X_train, y_train, epochs=10, validation_split=0.2)
```
We train the model with the training data for 10 epochs and use 20% of the data for validation.

### Save Model
```python
model.save('trained_model.h5')
```
We save the trained model to a file named `trained_model.h5`.

### Save Model Architecture
```python
model_json = model.to_json()
with open("model_architecture.json", "w") as json_file:
    json_file.write(model_json)
```
We save the model architecture to a JSON file named `model_architecture.json`.

## Running the Script

1. Ensure your training data is available in `data_train.npy` file.
2. Run the script:
```sh
python script_name.py
```
Replace `script_name.py` with the actual name of your script file.

## Notes

- Adjust `n_steps_in` and the structure of `data_train.npy` as needed for your specific data.
- Modify the model architecture and training parameters (e.g., number of epochs, batch size) based on your specific requirements and data characteristics.

## Conclusion

This README provides an overview and instructions for using the script to train a CNN model for time series prediction. Ensure your data is correctly formatted and adjust parameters as necessary for optimal performance.
