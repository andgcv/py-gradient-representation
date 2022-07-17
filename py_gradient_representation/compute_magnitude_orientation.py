from preprocessing_smoothing import apply_smoothing
from cv2 import Sobel, CV_64F
from numpy import sqrt, arctan2, pi

# Load image preprocessed with blur and bilateral filtering
img = apply_smoothing()

# Compute gradients along the x and y axis
gradient_x = Sobel(img, CV_64F, 1, 0)
gradient_y = Sobel(img, CV_64F, 0, 1)


def compute_magnitude():
    # Compute gradient magnitude
    magnitude = sqrt((gradient_x ** 2) + (gradient_y ** 2))
    return magnitude


def compute_orientation():
    # Compute gradient orientation
    orientation = arctan2(gradient_y, gradient_x) * (180 / pi) % 180
    return orientation
