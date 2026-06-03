# from ultralytics import YOLO
import cv2 as cv
import numpy as np
import pyvirtualcam as cam
import time
from file_selector import get_image_path

def process_board_image(filepath):
    """Computer vision logic for analyzing, thresholding, and slicing the board"""
    # Read the image, greyscale it, then make it black and white
    image = cv.imread(filepath)
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, monochrome_image = cv.threshold(grey_image, thresh=110, maxval=255, type=cv.THRESH_BINARY_INV)

    # Get the height and width of the image
    height, width = monochrome_image.shape

    # Calculate cell dimensions and make 3x3 array
    cell_w = width // 3
    cell_h = height // 3
    mx = int(cell_w * 0.3)
    my = int(cell_h * 0.3)
    board = np.full((3, 3), "-", dtype=str)

    # Nested loop to find contours of each cell
    for row in range(3):
        for col in range(3):
            # Cell range of interest, this is the part of image that is analyzed
            x1 = col * cell_w
            y1 = row * cell_h
            x2 = x1 + cell_w
            y2 = y1 + cell_h
            cell_roi = monochrome_image[y1+my:y2-my, x1+mx:x2-mx]
            
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
                time.sleep(0.2)
                
                # If the shape takes up over a certain amount of space, must be an O. Else, X
                if extent > 0.65:
                    board[row, col] = "O"
                else:
                    board[row, col] = "X"

    print(board)
    time.sleep(0.5)

    # For debugging: show the grid + cell ROIs on a color copy (delete when done)
    debug_view = cv.cvtColor(monochrome_image, cv.COLOR_GRAY2BGR)
    for row in range(3):
        for col in range(3):
            x1, y1 = col * cell_w, row * cell_h
            x2, y2 = x1 + cell_w, y1 + cell_h
            cv.rectangle(debug_view, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv.rectangle(debug_view, (x1+mx, y1+my), (x2-mx, y2-my), (0, 255, 0), 2)
            cv.putText(debug_view, board[row, col], (x1+mx+5, y1+my+30),
                       cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    cv.imshow("Debug grid", debug_view)

    # Display the image, exit program when key is pressed
    cv.imshow("Tic Tac Toe Board", monochrome_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return board

# def are_moves_left(board):
#     ...

# def evaluate_board(board):
#     """Checks 2D NumPy array for a winner"""

# def minimax(board, depth, is_maximizing):
#     ...

# def find_best_move(board):
#     ...

if __name__ == "__main__":
    # Retrieves the inputted image from other file's function
    target_image = get_image_path()

    # Exit program if no image is inputted
    if not target_image:
        print("No valid file selected.")
        exit()
    
    print(f"Processing image: {target_image}")

    # Pass board image into CV processing function and find score/winner
    current_board = process_board_image(target_image)
    # score = evaluate_board(current_board)