from load_src_image import get_image_name
from compute_magnitude_orientation import compute_magnitude, compute_orientation
from matplotlib.pyplot import imsave
from os.path import dirname, join

# Define project root and export path
project_root = dirname(dirname(__file__))
export_path = join(project_root, 'gradient_export')


def export_gradient():
    print("Available colormaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html")

    # Request input for the colormap to be used during the export
    cmap = input("Which colormap do you want to export with?: ")

    # Export the gradient representations of the image, using the cmap provided
    imsave('{}\\{}-magnitude-{}.png'.format(export_path, get_image_name(), cmap), compute_magnitude(), cmap=cmap)
    imsave('{}\\{}-orientation-{}.png'.format(export_path, get_image_name(), cmap), compute_orientation(), cmap=cmap)

    print("Image has been processed.")
