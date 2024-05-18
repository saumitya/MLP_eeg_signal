import mne


file_path = r'C:\Users\saumi\OneDrive\Desktop\MLP\dataset\A02E.gdf'

raw = mne.io.read_raw_gdf(file_path)


raw.load_data()


events, event_dict = mne.events_from_annotations(raw)

print("Event Dictionary:")
print(event_dict)

event_types = [event_id for event_id in event_dict.keys()]
trigger_names = [event_dict[event_id] for event_id in event_types]


print("\nEvent Types and Trigger Names:")
for event_type, trigger_name in zip(event_types, trigger_names):
    print(f"Event Type: {event_type}, Trigger Name: {trigger_name}")
