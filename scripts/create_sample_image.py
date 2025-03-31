# filepath: /workspaces/Project/scripts/create_sample_image.py

import cv2
import numpy as np

# Create a blank white image
image = np.ones((200, 600, 3), dtype=np.uint8) * 255

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Hello, Tesseract OCR!", (50, 100), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Save the image
cv2.imwrite("../input_files/equation_image.png", image)
print("Sample image created as 'equation_image.png'")