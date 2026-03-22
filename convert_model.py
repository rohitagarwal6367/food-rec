from tensorflow.keras.models import load_model

# Purane model ka path
old_model_path = 'model/food_model.h5'

# Load purana model
model = load_model(old_model_path)

# Naye format mein save karo
new_model_path = 'model/food_model.keras'
model.save(new_model_path)

print("Model successfully converted and saved as food_model.keras")