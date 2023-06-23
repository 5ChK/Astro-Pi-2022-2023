import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the grayscale image
grayscale_image = Image.open('download4.png').convert('L')

# Convert the grayscale image to a numpy array
grayscale_array = np.array(grayscale_image)

# Normalize the grayscale array to the range [0, 1]
normalized_array = grayscale_array / 255.0

# Apply a color map to the normalized array to create a false color image
color_map = plt.cm.jet  # Choose the color map, e.g., 'jet'
false_color_array = color_map(normalized_array)

# Convert the array to PIL Image
false_color_image = Image.fromarray((false_color_array[:, :, :3] * 255).astype(np.uint8))

# Save the false color NDVI image as png
false_color_image.save('false_color_ndvi_download4.png')
