# from ultralytics import YOLO
import cv2 as cv
import numpy as np
import time
import os
from file_selector import get_image_path
from virtualcam import broadcast

def cell_dims(image):
    """Return width and height for each cell and ROI margins for a 3x3 grid over the image.
    Uses shape[:2] so it works on both grayscale (h, w) and color (h, w, 3) images."""
    height, width = image.shape[:2] # Using : only grabs the h and w of the shape
    cell_w, cell_h = width // 3, height // 3
    mx, my = int(cell_w * 0.3), int(cell_h * 0.3)
    return cell_w, cell_h, mx, my

def put_centered_text(image, text, center_x, center_y, scale, color, thickness):
    """Draws text centered on the point (center_x, center_y)"""
    (tw, th), _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, scale, thickness)
    x = center_x - tw // 2   # shift left by half the text width to center it
    y = center_y + th // 2   # shift down by half the text height to center it
    cv.putText(image, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, scale, color, thickness)

def load_and_threshold_image(filepath):
    """Read the image, greyscale it, then make it black and white.
    Returns both the original (color) image and the monochrome version."""
    image = cv.imread(filepath)
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, monochrome_image = cv.threshold(grey_image, thresh=110, maxval=255, type=cv.THRESH_BINARY_INV)
    return image, monochrome_image

def process_board(monochrome_image):
    """Computer vision logic for analyzing and slicing the board into a 3x3 array"""
    # Calculate cell dimensions and make 3x3 array
    cell_w, cell_h, mx, my = cell_dims(monochrome_image)
    board = np.full((3, 3), "-", dtype=str)

    # Nested loop to find contours of each cell to check for its contents (X/O/empty)
    print("\nExtent calculation results:")
    for row in range(3):
        for col in range(3):
            # Cell range of interest, this is the part of image that is analyzed
            x1, y1 = col * cell_w, row * cell_h
            x2, y2 = x1 + cell_w, y1 + cell_h
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

                # Get the area of the shape in the cell (X/O), create its ROI (region of interest) within the cell
                area = cv.contourArea(contour)
                x, y, w, h = cv.boundingRect(contour)
                
                # Look at how much area the shape takes up in its ROI
                extent = area / (w * h) if (w * h) > 0 else 0

                # Print statement for debugging. This is to see what the computer sees
                print( f"\n({row}, {col}) - Extent: {extent:.2f}")
                time.sleep(0.2)
                
                # If the shape takes up over a certain amount of space, must be an O. Else, X
                if extent > 0.65:
                    board[row, col] = "O"
                else:
                    board[row, col] = "X"
    print("\nBoard:\n", board)
    time.sleep(1)
    return board

def game_result(board):
    """Checks 2D NumPy array for a winner, then a draw.
    Returns "X" or "O" for a winner, "Draw" for a draw,
    or None if the game isn't done."""
    # Build the 8 lines that can win: 3 rows, 3 columns, 2 diagonals
    lines = []
    for i in range(3):
        lines.append(board[i, :]) # row i
        lines.append(board[:, i]) # column i
    lines.append(board.diagonal()) # top-left to bottom-right
    lines.append(np.fliplr(board).diagonal()) # top-right to bottom-left

    # A line wins if it isn't empty and all three cells match
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0] # "X" or "O"

    # Must be draw if board is full and previous return statement wasn't triggered
    if " " not in board:
        return "Draw"

    # Otherwise the game is still in progress
    return None

def are_moves_left(board, result):
    """If there's no win/draw yet, uses result from game_result to return
    a list of (row, col) for every empty cell."""
    if result is not None:
        # Winner or draw: the game is over, so there are no moves to make
        return []

    # No winner and board not full: collect the coordinates of the empty cells
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row, col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def show_result(original_image, result, empty_cells=()):
    """Pops up the original image with the game result drawn on it.
    If the game is unfinished, also labels each empty cell with its (row, col)."""
    display = original_image.copy()
    if result is None:
        text = "Game unfinished"
    elif result == "Draw":
        text = "Draw!"
    else:
        text = f"{result} wins!"

    # Center the title text horizontally near the top of the image
    (tw, th), _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 1.5, 3)
    x = (display.shape[1] - tw) // 2
    y = th + 20
    cv.putText(display, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    # Label each empty spot in the center of its cell
    cell_w, cell_h, _, _ = cell_dims(display)
    for (row, col) in empty_cells:
        cx = col * cell_w + cell_w // 2
        cy = row * cell_h + cell_h // 2
        put_centered_text(display, f"({row},{col})", cx, cy, 0.8, (0, 200, 0), 2)

    return display

def show_debug_view(monochrome_image, board):
    """For debugging: show the grid + cell ROIs on a color copy with detected X/O/empty drawn in"""
    cell_w, cell_h, mx, my = cell_dims(monochrome_image)

    debug_view = cv.cvtColor(monochrome_image, cv.COLOR_GRAY2BGR)
    for row in range(3):
        for col in range(3):
            # Finding dimensions for grid layout
            x1, y1 = col * cell_w, row * cell_h
            x2, y2 = x1 + cell_w, y1 + cell_h

            # Using dimensions to make board grid and ROI squares for each cell
            cv.rectangle(debug_view, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv.rectangle(debug_view, (x1+mx, y1+my), (x2-mx, y2-my), (0, 255, 0), 2)

            # Placing text at center of each cell to see what the computer saw (X, O, or empty)
            text = str(board[row, col])
            put_centered_text(debug_view, text, (x1 + x2) // 2, (y1 + y2) // 2, 1.0, (0, 0, 255), 2)

    return debug_view

if __name__ == "__main__":
    # Retrieves the inputted image from other file's function
    target_image = get_image_path()

    # Exit program if no image is inputted
    if not target_image:
        print("No valid file selected.")
        exit()
    
    # Load and threshold the image, then find X's and O's
    print(f"\nProcessing image: {os.path.basename(target_image)}")
    original_image, monochrome_image = load_and_threshold_image(target_image)
    current_board = process_board(monochrome_image)

    # Decide the outcome, then announce it (and any open spots) on the original image
    result = game_result(current_board)
    empty_cells = are_moves_left(current_board, result)   # [] if the game is over
    
    # Make the game result frame of the board, and the debug frame. Then combine them
    result_frame = show_result(original_image, result, empty_cells)
    debug_frame = show_debug_view(monochrome_image, current_board)
    combined_frame = np.hstack((result_frame, debug_frame))

    # Broadcast the combined frame to OBS Studio
    broadcast(combined_frame)