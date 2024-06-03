import numpy as np
import cv2


def draw_circle(
        image_path: str,
        small_circle_radius_factor: int,
        final_image_path: str,
) -> np.ndarray:
    "Main function to draw 4 cirles based on the image"
    image = read_image(image_path)
    width, height, center_x, center_y = find_dimensions(image)
    large_circle_radius = _find_large_circle_radius(image, height, center_x)
    small_circle_radius = _find_small_circle_radius(large_circle_radius, small_circle_radius_factor)
    small_circle_position = _find_small_circle_postision(large_circle_radius, small_circle_radius, center_x, center_y)
    small_circles = _draw_small_circles(small_circle_position, small_circle_radius, height, width)
    combined_circle = _draw_large_circle(small_circles, large_circle_radius, center_x, center_y)
    if final_image_path:
        _save_small_circles(combined_circle, final_image_path)
    return small_circles


def read_image(image_path: str) -> np.ndarray:
    "Function to read an image"
    image = cv2.imread(image_path)
    return image


def find_dimensions(image: np.ndarray) -> tuple:
    "Function to find dimensions"
    width, height = image.shape[:2]
    center_x = width // 2
    center_y = height // 2
    return width, height, center_x, center_y


def _find_large_circle_radius(image: np.ndarray, height: int, center_x: int) -> int:
    "Returns the radius of the large circle"
    edge_y, break_y = None, None
    for y in range(height):
        pixel = image[y, center_x]
        if np.sum(np.abs(pixel - [255, 255, 255])) > 50:
            edge_y = y
            break

    for y in range(edge_y + 1, height):
        pixel = image[y, center_x]
        if np.sum(np.abs(pixel - [255, 255, 255])) > 50:
            break_y = y
            break

    if edge_y != None and break_y != None:
        large_radius = (break_y - edge_y) // 2
        return large_radius
    
    return None


def _find_small_circle_radius(large_circle_radius: int, small_circle_radius_factor: int) -> int:
    "Find the radius of small circles"
    return int(large_circle_radius / small_circle_radius_factor)


def _find_small_circle_postision(
        large_radius: int,
        small_radius: int,
        center_x: int,
        center_y: int,
) -> list:
    "Calculates the postition of small circles to be drawn"
    left_center = (center_x - large_radius - small_radius, center_y)
    right_center = (center_x + large_radius + small_radius, center_y)
    top_center = (center_x, center_y - large_radius - small_radius)
    bottom_center = (center_x, center_y + large_radius + small_radius)
    return [left_center, right_center, top_center, bottom_center]


def _draw_small_circles(
        small_circle_position: list,
        small_circle_radius: int,
        height: int,
        width: int,
) -> np.ndarray:
    "Create an empty image and draws 4 small circles based on the position passed to it"
    new_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.circle(new_image, small_circle_position[0], small_circle_radius, (0, 0, 0), 2)
    cv2.circle(new_image, small_circle_position[1], small_circle_radius, (0, 0, 0), 2)
    cv2.circle(new_image, small_circle_position[2], small_circle_radius, (0, 0, 0), 2)
    cv2.circle(new_image, small_circle_position[3], small_circle_radius, (0, 0, 0), 2)
    return new_image


def _draw_large_circle(
        image: np.ndarray,
        large_circle_radius: int,
        center_x: int,
        center_y: int,
) -> np.ndarray:
    "takes the image with small circles and draws the initial circle given to us"
    cv2.circle(image, (center_x, center_y), large_circle_radius, (0, 0, 0), 2)
    return image


def _save_small_circles(combined_circle: np.ndarray, final_image_path: str) -> None:
    "Saves the final image to the output final path"
    cv2.imwrite(final_image_path, combined_circle)


draw_circle('images/circle.jpg', 5, 'images/circles_output_clean.jpg')