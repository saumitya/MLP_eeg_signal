import numpy as np
import tensorflow as tf
import json
import matplotlib.pyplot as plt


n_steps_in = 100
num_channels = 1


data_test = np.load('data_val.npy')

X_test = data_test[:, :n_steps_in]  
y_test = data_test[:, n_steps_in:]  


X_test = X_test.reshape(-1, n_steps_in, num_channels)


with open('model_architecture.json', 'r') as json_file:
    model_json = json_file.read()
model = tf.keras.models.model_from_json(model_json)


model.load_weights('trained_model.h5')


model.compile(optimizer='adam', loss='mse')

loss = model.evaluate(X_test, y_test)
print("Test Loss:", loss)


predictions = model.predict(X_test)


plt.figure(figsize=(10, 6))
num_samples = min(5, len(predictions))  
for i in range(num_samples):
    plt.plot(predictions[i], label=f'Predicted Signal {i+1}')
    plt.plot(y_test[i], label=f'Electrode sensor {i+1}', linestyle='-')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Predicted vs Actual EEG Signals')
plt.legend()
plt.grid(True)
plt.show()
