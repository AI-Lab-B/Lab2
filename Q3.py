import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Download the image


image = Image.open('me.png')
img_array = np.array(image)


# Plot the original image
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img_array)
plt.title("Original Image")


# Rotate and flip the image
rotated_img = np.rot90(img_array)
flipped_img = np.fliplr(img_array)


# Plot the rotated and flipped images
plt.subplot(1, 3, 2)
plt.imshow(rotated_img)
plt.title("Rotated Image")

plt.subplot(1, 3, 3)
plt.imshow(flipped_img)
plt.title("Flipped Image")


# Grayscale conversion
gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])


# Plot the grayscale image
plt.figure(figsize=(5,5))
plt.imshow(gray_img, cmap='gray')  
plt.title("Grayscale Image")
<<<<<<< HEAD
<<<<<<< HEAD
=======
plt.savefig("Q3-1")
>>>>>>> 4785f2f043781628b8d3ac5b770f467e24c323d6
=======
plt.savefig("Q3-1")
>>>>>>> 4785f2f043781628b8d3ac5b770f467e24c323d6

plt.show()