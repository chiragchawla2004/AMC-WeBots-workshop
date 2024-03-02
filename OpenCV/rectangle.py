import numpy as np
import cv2

# Create a black image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Define rectangle parameters
top_left = (100, 100)
bottom_right = (300, 300)
color = (255, 0, 0)  # Blue color in BGR format
thickness = -1 # Thickness of the rectangle

# Draw the rectangle on the image
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Display the image
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
