import numpy as np
import cv2

def draw_circle(image_path):
    image = cv2.imread(image_path)
    width, height = image.shape[:2]

    center_x = width//2
    center_y = height//2

    for y in range(height):
        pixel = image[y, center_x]
        if np.sum(np.abs(pixel-[255,255,255]))>50:
            edge_y = y 
            break

    for y in range(edge_y+1, height):
        pixel = image[y, center_x]
        if np.sum(np.abs(pixel-[255,255,255]))>50:
            break_y = y
            break
    
    if 'edge_y' in locals() and 'break_y' in locals():
        large_radius = (break_y - edge_y) //2

    new_image = np.ones((height, width, 3), dtype=np.uint8) * 255


    rescale = 3
    small_radius = int(large_radius / rescale)

    # Calculate the positions of the smaller circles
    center_x = width // 2
    center_y = height // 2
    left_center = (center_x - large_radius - small_radius, center_y)
    right_center = (center_x + large_radius + small_radius, center_y)
    top_center = (center_x, center_y - large_radius - small_radius)
    bottom_center = (center_x, center_y + large_radius + small_radius)

    # Draw the smaller circles
    cv2.circle(new_image, left_center, small_radius, (0, 0, 0), 2)
    cv2.circle(new_image, right_center, small_radius, (0, 0, 0), 2)
    cv2.circle(new_image, top_center, small_radius, (0, 0, 0), 2)
    cv2.circle(new_image, bottom_center, small_radius, (0, 0, 0), 2)

    # Draw the large circle
    cv2.circle(new_image, (center_x, center_y), large_radius, (0, 0, 0), 2)

    cv2.imwrite('images/circles_output.jpg', new_image)

draw_circle('images/circle.jpg')

