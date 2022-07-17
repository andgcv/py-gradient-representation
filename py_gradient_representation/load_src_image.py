from os import path
from cv2 import imread, IMREAD_GRAYSCALE
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

image_name = ""


def load_image():
    global image_name

    # Open window to specify the src image
    image_path = filedialog.askopenfilename()

    # Save the image name without the extension
    image_name = path.basename(image_path).split('.')[0]

    # Load grayscale src image
    src = imread(image_path, IMREAD_GRAYSCALE)

    # Check if image loaded successfully
    if src is None:
        print('Error opening image!')
        print('Usage: load_src_image.py [image_path -- {}] \n'.format(image_path))
        return -1

    return src


def get_image_name():
    return image_name
