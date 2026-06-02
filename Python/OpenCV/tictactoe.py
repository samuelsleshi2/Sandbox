import cv2 as cv

# Read the image
image = cv.imread('ttt.png')

# Check if the image was properly loaded
if image is None:
    print("Could not read the image.")
    exit()

# If it was, greyscale it and display it
print("Image read successfully.")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Tic Tac Toe board", gray_image)
cv.waitKey(0)
cv.destroyAllWindows()