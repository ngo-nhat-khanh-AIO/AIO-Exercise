import numpy as np
import matplotlib . image as mpimg
img = mpimg . imread ("/content/dog.jpeg")
gray_img_02 = (np.average(img, axis=2))
gray_img_02 [0 , 0]
