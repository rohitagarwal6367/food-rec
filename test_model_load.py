from tensorflow.keras.models import load_model

try:
    model = load_model("model/food_model.h5")  # ya .h5
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Failed to load model:")
    print(e)
