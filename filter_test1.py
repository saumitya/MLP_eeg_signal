import mne


file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A02E.gdf'


raw = mne.io.read_raw_gdf(file_path, preload=True)


raw.filter(1, 40)


event_id = {'event1': 1, 'event2': 2} 


events = mne.find_events(raw, stim_channel='Status')


tmin, tmax = 0, 2  


epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=None)


features = epochs.get_data()  

