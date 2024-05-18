import mne

file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A01E.gdf'

raw = mne.io.read_raw_gdf(file_path)

channel_names = ['EEG-Fz', 'EEG-0', 'EEG-1', 'EEG-2', 'EEG-3', 'EEG-4', 'EEG-5', 'EEG-C3', 'EEG-6', 'EEG-Cz', 'EEG-7', 'EEG-C4', 'EEG-8', 'EEG-9', 'EEG-10', 'EEG-11', 'EEG-12', 'EEG-13', 'EEG-14', 'EEG-Pz', 'EEG-15', 'EEG-16', 'EOG-left', 'EOG-central', 'EOG-right']
channel_positions = {
    'EEG-Fz': (0, 0, 1),
    'EEG-Cz': (0, 0, 0),
    'EEG-Pz': (0, 0, -1),
    'EEG-O1': (-0.5, -0.5, -1),
    'EEG-O2': (0.5, -0.5, -1),
    'EEG-T7': (-1, 0, 0),
    'EEG-T8': (1, 0, 0),
    'EEG-Fp1': (-0.5, 0.5, 1),
    'EEG-Fp2': (0.5, 0.5, 1),
    'EEG-F3': (-0.5, 0, 1),
    'EEG-F4': (0.5, 0, 1),
    'EEG-C3': (-0.5, 0, 0),
    'EEG-C4': (0.5, 0, 0),
    'EEG-P3': (-0.5, 0, -1),
    'EEG-P4': (0.5, 0, -1),
    'EEG-T3': (-1, 0, -1),
    'EEG-T4': (1, 0, -1),
    'EEG-T5': (-1, -0.5, -1),
    'EEG-T6': (1, -0.5, -1),
    'EEG-Oz': (0, -0.5, -1),
    'EOG-left': (-1, 1, 0),
    'EOG-right': (1, 1, 0),
    'EOG-horizontal': (0, 1, 0)
}

montage = mne.channels.Montage(
    pos=channel_positions,
    ch_names=channel_names,
    kind='custom', 
    selection=None, 
    coord_frame='head'  
)


raw.set_montage(montage)


raw.plot_sensors()
