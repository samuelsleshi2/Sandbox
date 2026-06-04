import pyvirtualcam as pycam

def broadcast(frame):
    """Send a single BGR frame of both board displays to the virtual camera."""
    height, width = frame.shape[:2] # Dimensions for entire frame to be broadcasted
    
    # Make a virtual camera device with the frame dimensions
    with pycam.Camera(width=width, height=height, fps=30, fmt=pycam.PixelFormat.BGR) as vcam:
        print(f"\nBroadcasting to OBS: {vcam.device}")
        # Continuously send the frame to the live OBS feed until CTRL+C in terminal
        while True:
            try:
                vcam.send(frame)
                vcam.sleep_until_next_frame()
            except KeyboardInterrupt:
                print("\nStream stopped")
                break