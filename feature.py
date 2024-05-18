import mne


file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A01T.gdf'


raw = mne.io.read_raw_gdf(file_path, preload=True)


raw.filter(1, 60)


events, event_id = mne.events_from_annotations(raw)


tmin, tmax = -4, 8 


epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=None, event_repeated='merge')


epochs.plot_image(combine='mean', cmap='interactive', sigma=0.5)


mne.viz.tight_layout()
mne.viz.show()
