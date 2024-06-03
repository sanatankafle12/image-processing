# image-processing

# Task 1:

![image](https://github.com/sanatankafle12/image-processing/assets/42962016/ea421b86-ba21-4f7a-9d4e-8d742c3608ce)



### Load the input image: 
The script starts by loading the input image using the read_image() function, which reads the image from the specified path and returns a NumPy array representation of the image.

### Calculate the dimensions of the image: 
The find_dimensions() function is used to determine the width, height, and the coordinates of the center of the input image.

### Calculate the radius of the large circle: 
The _find_large_circle_radius() function calculates the radius of the large circle by traversing through the pixels along the vertical center of the image. It identifies the edge and break points of the large circle and calculates the radius by dividing the distance between these points by 2.

### Calculate the radius of the small circles: 
The _find_small_circle_radius() function calculates the radius of the small circles based on the radius of the large circle and a provided small circle radius factor.

### Determine the positions of the small circles:
The _find_small_circle_postision() function calculates the positions of the four small circles based on the radius of the large circle, the radius of the small circles, and the center of the image.

### Draw the small circles: 
The _draw_small_circles() function creates a new image and draws the four small circles at the calculated positions.

### Draw the large circle: 
The _draw_large_circle() function takes the image with the small circles and draws the large circle around them.

### Save the final image: 
The _save_small_circles() function saves the final image with the large and small circles to the specified output path. 


# Task 2:
![image](https://github.com/sanatankafle12/image-processing/assets/42962016/a154e067-e6a1-40e0-be12-4bcd510fbedb)



### Define the change_color_in_image function: 
This is the main function that performs the color replacement.

### Read the input image: 
Use the _read_image function to read the image from the specified path.

### Convert the image to RGB and HSV color spaces: 
Use the _convert_color function to convert the image from BGR to RGB and then to HSV.

### Create a color mask:
Use the _create_color_mask function to create a binary mask that identifies the pixels in the image that match the color_to_replace range.

### Refine the color mask: 
Use the _refine_color_mask function to apply morphological operations to the mask to improve its coverage and remove small holes or gaps.

### Replace the color while preserving lighting:
Use the replace_color_preserving_lighting function to replace the color in the masked regions while preserving the lighting effects (i.e., the saturation and value channels remain unchanged).

### Convert the image back to BGR color space:
Use the convert_image_back function to convert the modified HSV image back to the BGR color space.

### Save the output image: 
Use the save_image function to save the modified image to the specified output path. 


# Steps to Run the code Locally

1. Download and install Docker on your machine.
2. ```docker build . -t circle_task ``` 
3. ``` docker run --rm -v $(pwd)/images:/usr/src/app/images circle_task  task1.py**** ```
