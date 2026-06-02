import cv2 as cv
import numpy as np
import pyvirtualcam as cam
import time

# Read the image, greyscale it, then make it black and white
image = cv.imread("ttt.png")
grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_, monochrome_image = cv.threshold(grey_image, thresh=110, maxval=255, type=cv.THRESH_BINARY_INV)

# Retrieve the borders of the image to get its boundaries
contours, hierarchy = cv.findContours(monochrome_image, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)

# Get the height and width of the image to put a box overlay on it
height, width = monochrome_image.shape
center_x = width // 2
center_y = height // 2
box_overlay = cv.rectangle(monochrome_image, pt1=(0,0), pt2=(width,height), color=(0,255,0), thickness=5)


# Calculate cell dimensions and make 3x3 array 
cell_w = width // 3
cell_h = height // 3
board = np.full((3, 3), "-", dtype=str)

# Nested loop to find contours of each cell
for row in range(3):
    for col in range(3):
        # Cell range of interest, this is the part of image that is analyzed
        x1 = col * cell_w
        y1 = row * cell_h
        x2 = x1 + cell_w
        y2 = y1 + cell_h
        cell_roi = monochrome_image[y1:y2, x1:x2]
        
        # Contours of the roi subimage
        cell_contours, _ = cv.findContours(cell_roi, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # If length of current cell contour shape list is 0, cell is empty
        if len(cell_contours) == 0:
            board[row, col] = " "
        else:
            # Sort to get largest shape in cell
            cell_contours = sorted(cell_contours, key=cv.contourArea, reverse=True)
            contour = cell_contours[0]

            # Look at the shape in the cell, initalize its bounds within the cell
            area = cv.contourArea(contour)
            x, y, w, h = cv.boundingRect(contour)
            
            # Look at how much space the shape takes up not in the whole cell, but in its contour
            extent = area / (w * h) if (w * h) > 0 else 0

            # Print statement for debugging. This is to see what the computer sees
            print(f"Row {row}, Col {col} - Extent: {extent:.2f}")
            time.sleep(0.1)
            
            # If the shape takes up over a certain amount of space, must be an O. Else, X
            if extent > 0.65:
                board[row, col] = "O"
            else:
                board[row, col] = "X"

print(board)

# Display the image, exit program when key is pressed
cv.imshow("Tic Tac Toe Board", monochrome_image)
cv.waitKey(0)
cv.destroyAllWindows()