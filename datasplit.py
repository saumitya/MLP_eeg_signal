import numpy as np
from sklearn.model_selection import train_test_split


dataset_files = ['psd_array.npy', 'psd_array2.npy','psd_array3.npy','psd_array4.npy','psd_array5.npy','psd_array6.npy','psd_array7.npy','psd_array8.npy','psd_array9.npy','psd_array10.npy','psd_array11.npy',]

data = []
labels = []


for file in dataset_files:
    loaded_data = np.load(file)
    data.append(loaded_data)



data_train, data_val = train_test_split(data, test_size=0.2, random_state=42)

np.save('data_train.npy', data_train)
np.save('data_val.npy', data_val)
