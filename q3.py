import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image_path = "cacti.jpeg"
img = Image.open(image_path)
cacti_arr = np.array(img)
rotate = np.rot90(cacti_arr)
flip = np.fliplr(cacti_arr)
#plt.imshow(flip)
gray_img = np.dot (cacti_arr[..., :3], [0.299, 0.587, 0.114])
fig, images = plt.subplots(1, 4, figsize=(17, 5))  
images[0].imshow(cacti_arr)
images[0].set_title("Original Image")


images[1].imshow(rotate)
images[1].set_title("90 degree rotated Image")

images[2].imshow(flip)
images[2].set_title("flipped Image")

images[3].imshow(gray_img)
images[3].set_title("gray scaled  Image")


plt.show()