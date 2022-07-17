from load_src_image import load_image
from cv2 import medianBlur, bilateralFilter

# Load the src image
img = load_image()


def apply_smoothing():
    # Apply median blur and bilateral filtering to the image
    img_median_blur = medianBlur(img, 3)
    img_bilateral_filter = bilateralFilter(img_median_blur, 11, 21, 7)

    return img_bilateral_filter
