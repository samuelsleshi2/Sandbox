import cv2
import numpy as np

# Read the image
image = cv2.imread('ttt.png')

# Check if the image was properly loaded
if image is None:
    print("Could not read the image.")
    exit()

# If it was, greyscale it and display it
print("Image read successfully.")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tic Tac Toe board", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()