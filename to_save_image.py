import mne
import matplotlib.pyplot as plt

# Path to the .gdf file
file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A01E.gdf'

# Read the .gdf file
raw = mne.io.read_raw_gdf(file_path)

# Define channel names
channel_names = ['EEG-Fz', 'EEG-0', 'EEG-1', 'EEG-2', 'EEG-3', 'EEG-4', 'EEG-5', 'EEG-C3', 'EEG-6', 'EEG-Cz', 'EEG-7', 'EEG-C4', 'EEG-8', 'EEG-9', 'EEG-10', 'EEG-11', 'EEG-12', 'EEG-13', 'EEG-14', 'EEG-Pz', 'EEG-15', 'EEG-16', 'EOG-left', 'EOG-central', 'EOG-right']

# Define channel positions
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

# Create a DigMontage object with specified channel positions
montage = mne.channels.make_dig_montage(
    ch_pos=channel_positions,
    coord_frame='head'
)

# Apply the custom montage to the raw object
raw.set_montage(montage)

# Save the plot as an image file
plot_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\sensor_plot.png'
raw.plot_sensors(show_names=True, to_sphere=True, kind='topomap', title='Sensor Locations', show=False)
plt.savefig(plot_path)
print(f"Plot saved as {plot_path}")
