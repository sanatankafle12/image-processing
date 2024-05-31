import cv2
import numpy as np


def change_color_in_image(image_path, color_to_replace, replacement_color):
    """
    Replaces a specific color in an image with another color.

    Args:
        image_path (str): Path to the image file.
        color_to_replace (list): List containing the lower and upper bounds of the color to replace in HSV format.
        replacement_color (list): List containing the HSV value of the replacement color.

    Returns:
        None
    """

    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    mask_color = cv2.inRange(image_hsv, np.array(color_to_replace[0]), np.array(color_to_replace[1]))
    kernel = np.ones((9, 9), np.uint8)
    mask_color = cv2.morphologyEx(mask_color, cv2.MORPH_CLOSE, kernel)
    mask_color = cv2.morphologyEx(mask_color, cv2.MORPH_OPEN, kernel)
    replacement_color_hsv = np.array(replacement_color)
    image_hsv[mask_color > 0] = replacement_color_hsv
    image_rgb_new = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
    cv2.imwrite("images/output_fish.jpg", cv2.cvtColor(image_rgb_new, cv2.COLOR_BGR2RGB))

color_to_replace = [[0, 200, 200], [255, 255, 255]]  
replacement_color = [60, 255, 255]  

change_color_in_image("images/fish.jpg", color_to_replace, replacement_color)