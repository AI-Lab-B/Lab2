# Take any image from internet and convert that into numpy array
# > plot that numpy array using matplot lib pyplot.
# > rot and flip that image using np.rot90 and np.fliplr respectively and plot it
# > also apply this grayscale filter to your original numpy image and plot it.
# # Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
# gray_img = np.dot (img_array[..., :3], [0.299, 0.587, 0.114])



import numpy as np
import matplotlib.pyplot as plt
import PIL.Image



img = PIL.Image.open('cat.jpg')

img = np.array(img)


plt.imshow(img)
plt.title('Original Image')

plt.show()

rotated_img = np.rot90(img)
plt.imshow(rotated_img)
plt.title('Rotated Image')

plt.show()

flipped_img = np.fliplr(img)
plt.imshow(flipped_img)
plt.title('Flipped Image')

plt.show()

gray_img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')

plt.show()

