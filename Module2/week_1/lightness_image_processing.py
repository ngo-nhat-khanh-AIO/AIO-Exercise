import numpy as np
import matplotlib . image as mpimg
img = mpimg.imread("/content/dog.jpeg")
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
gray_img_01[0, 0]


