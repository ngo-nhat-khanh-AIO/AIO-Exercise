import numpy as np
import matplotlib . image as mpimg
img = mpimg.imread("/content/dog.jpeg")
gray_img_03 = (0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2])
gray_img_03[0, 0]
