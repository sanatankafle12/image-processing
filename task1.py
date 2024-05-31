from PIL import Image, ImageDraw, ImageChops
import numpy as np

# Load the image
image_path = "circle.jpg"
image = Image.open(image_path)

# Convert to grayscale
gray_image = image.convert("L")

# Binarize the image (thresholding)
binary_image = gray_image.point(lambda p: p > 128 and 255)

# Find the bounding box of the circle
bbox = binary_image.getbbox()

# Calculate the radius
width = bbox[2] - bbox[0]
height = bbox[3] - bbox[1]
radius = width / 2

print(radius)