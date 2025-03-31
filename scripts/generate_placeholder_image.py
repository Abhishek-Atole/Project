import numpy as np
import cv2
import os
import image_preprocessor  # Import the image_preprocessor module

# Create a 300x300 white image
image = np.ones((300, 300, 3), dtype=np.uint8) * 255

# Save the image to the input_files directory
cv2.imwrite("../input_files/sample_image.png", image)
print("Placeholder image created at ../input_files/sample_image.png")

# Preprocess the image using the C++ module
result = image_preprocessor.preprocess_image(os.path.abspath("../input_files/sample_image.png"))
print("Processed image shape:", result.shape)
print("Processed image data (sample):")
print(result[:5, :5])  # Print the top-left 5x5 portion of the array