import image_preprocessor

# Test the preprocess_image function
result = image_preprocessor.preprocess_image("../input_files/sample_image.png")
print("Processed image shape:", result.shape)
print("Processed image data (sample):")
print(result[:5, :5])  # Print the top-left 5x5 portion of the array