import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

image=PIL.Image.open('pup.jpeg')

#convert this image into numpy array
image_array=np.array(image)

#plot that numpy array using matplot lib pyplot.

plt.imshow(image_array)
plt.show()

rotated_image=np.rot90(image_array)
flipped_image=np.fliplr(image_array)

plt.imshow(rotated_image)
plt.show()
plt.imshow(flipped_image)
plt.show()


gray_image=np.dot(image_array[...,:3],[0.299,0.587,0.114])
plt.imshow(gray_image,cmap='gray')
plt.show()






