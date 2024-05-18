import numpy as np
import mne

file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A06E.gdf'

raw = mne.io.read_raw_gdf(file_path, preload=True)

raw.filter(1, 60)

events, event_id = mne.events_from_annotations(raw)

tmin, tmax = -4, 8  

epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=None, event_repeated='merge')

frequencies, psd = mne.time_frequency.psd_array_multitaper(epochs.get_data(), sfreq=raw.info['sfreq'], fmin=1, fmax=60, n_jobs=1)

print("Shape of PSD array:", psd.shape)

np.save('psd_array11.npy', psd)
