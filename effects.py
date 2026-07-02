import cv2
import numpy as np


def apply_blur(frame, hand_landmarks, frame_shape):
    """
    Blur the ENTIRE frame when peace gesture is detected.
    Uses lighter blur for smoother, faster processing.
    """
    # Light blur - faster processing
    frame[:] = cv2.GaussianBlur(frame, (35, 35), 0)
    return frame
