from PIL import Image
from predict import predict_image
from advisory import advisory

# Load image
image = Image.open("test.png").convert("RGB")

# Predict
label, confidence = predict_image(image)

# Get advisory
info = advisory.get(label, {
    "cause": "No information available.",
    "solution": "No information available."
})

# Print result
print("\n--- Prediction Result ---")
print("Disease:", label)
print("Confidence:", confidence)
print("Cause:", info["cause"])
print("Solution:", info["solution"])