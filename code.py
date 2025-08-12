import cv2
import numpy as np

# Load image and convert to grayscale
color_img = cv2.imread("lena5.jpg")
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
height, width = gray_img.shape

# Store bit planes
planes = []

for bit_pos in range(8):
    # Extract the bit plane using bitwise operations
    mask = 1 << bit_pos
    extracted_plane = (gray_img & mask) >> bit_pos
    # Convert to visible format (0 or 255)
    visual_plane = extracted_plane * 255
    planes.append(visual_plane.astype(np.uint8))

# Display loop
while True:
    cv2.imshow("Original Color", color_img)
    cv2.imshow("Grayscale", gray_img)
    
    for idx, plane_img in enumerate(planes):
        cv2.imshow(f"Bit Plane {idx}", plane_img)
    
    # Exit on pressing 'x'
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows()
