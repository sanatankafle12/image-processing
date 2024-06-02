import cv2
import numpy as np


def change_color_in_image(image_path: str, color_to_replace: list, replacement_hue: float) -> None:
    """Replaces a color in an image with another while preserving lighting."""

    image = _read_image(image_path)
    image_rgb = _convert_color(image, cv2.COLOR_BGR2RGB)
    image_hsv = _convert_color(image_rgb, cv2.COLOR_RGB2HSV)

    mask = _create_color_mask(image_hsv, color_to_replace)
    mask = _refine_color_mask(mask)

    image_hsv_new = replace_color_preserving_lighting(image_hsv, mask, replacement_hue)
    image_bgr_new = convert_image_back(image_hsv_new)

    save_image(image_bgr_new, "images/output_fish.jpg")


def _read_image(image_path: str) -> np.ndarray:
    """Reads an image from the specified path."""

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error reading image from '{image_path}'")
    return image


def _convert_color(image: np.ndarray, conversion_code: int) -> np.ndarray:
    """Converts an image between different color spaces."""

    return cv2.cvtColor(image, conversion_code)


def _create_color_mask(image_hsv: np.ndarray, color_to_replace: list) -> np.ndarray:
    """Creates a mask for a specific color range in HSV."""
    return(cv2.inRange(image_hsv, np.array(color_to_replace[0]), np.array(color_to_replace[1])))


def _refine_color_mask(mask: np.ndarray, kernel_size=(6, 6)) -> np.ndarray:
    """Refines a color mask for better coverage."""

    kernel = np.ones(kernel_size, np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=3)
    return mask


def replace_color_preserving_lighting(image_hsv: np.ndarray, mask: np.ndarray, replacement_hue: float) -> np.ndarray:
    """Replaces color in a mask while preserving lighting effects."""

    image_hsv_new = image_hsv.copy()
    image_hsv_new[:, :, 0] = np.where(mask == 255, replacement_hue, image_hsv_new[:, :, 0])
    return image_hsv_new


def convert_image_back(image_hsv: np.ndarray) -> np.ndarray:
    """Converts an image from HSV back to BGR color space."""

    return cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)


def save_image(image: np.ndarray, output_path: str) -> None:
    """Saves an image to the specified path."""

    cv2.imwrite(output_path, image)


color_to_replace = [[0, 200, 200], [255, 255, 255]]
replacement_hue = 60

change_color_in_image("images/fish.jpg", color_to_replace, replacement_hue)