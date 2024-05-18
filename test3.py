import mne
import matplotlib.pyplot as plt


file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A05T.gdf'


raw = mne.io.read_raw_gdf(file_path)


channel_names = ['EEG-Fz', 'EEG-0', 'EEG-1', 'EEG-2', 'EEG-3', 'EEG-4', 'EEG-5', 'EEG-C3', 'EEG-6', 'EEG-Cz', 'EEG-7', 'EEG-C4', 'EEG-8', 'EEG-9', 'EEG-10', 'EEG-11', 'EEG-12', 'EEG-13', 'EEG-14', 'EEG-Pz', 'EEG-15', 'EEG-16', 'EOG-left', 'EOG-central', 'EOG-right']


channel_positions = {
    'EEG-Fz': [0, 0, 1],
    'EEG-0': [0, 0, 0],
    'EEG-1': [0, 0, 0],
    'EEG-2': [0, 0, 0],
    'EEG-3': [0, 0, 0],
    'EEG-4': [0, 0, 0],
    'EEG-5': [0, 0, 0],
    'EEG-C3': [-1, 0, 0],
    'EEG-6': [0, 0, 0],
    'EEG-Cz': [0, 0, 0],
    'EEG-7': [0, 0, 0],
    'EEG-C4': [1, 0, 0],
    'EEG-8': [0, 0, 0],
    'EEG-9': [0, 0, 0],
    'EEG-10': [0, 0, 0],
    'EEG-11': [0, 0, 0],
    'EEG-12': [0, 0, 0],
    'EEG-13': [0, 0, 0],
    'EEG-14': [0, 0, 0],
    'EEG-Pz': [0, 0, -1],
    'EEG-15': [0, 0, 0],
    'EEG-16': [0, 0, 0],
    'EOG-left': [0, -1, 0],
    'EOG-central': [0, 0, 0],
    'EOG-right': [0, 1, 0]
}


montage = mne.channels.make_dig_montage(
    ch_pos=channel_positions,
    coord_frame='head'
)


raw.set_montage(montage)


raw.plot_sensors()


plt.show()


raw.filter(1, 40)  
raw.set_eeg_reference()  

raw.info['ch_names']