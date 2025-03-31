import image_preprocessor

# Test the preprocess_image function
result = image_preprocessor.preprocess_image("../input_files/sample_image.png")
print("Processed image shape:", result.shape)