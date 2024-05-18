from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('trained_model.h5')

# Convert the model architecture to JSON
model_architecture = model.to_json()

# Save the model architecture to a JSON file
with open('model_architecture.json', 'w') as json_file:
    json_file.write(model_architecture)
