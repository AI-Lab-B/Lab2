import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio  # For reading image files


image_path = "q3_image.jpg"
img_array = iio.imread(image_path)  # Read the image into a NumPy array


gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114]) # grayscale
rotated_img = np.rot90(img_array)             #rotate 90 degree
flipped_img = np.fliplr(img_array)            # flip horizontally


fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].imshow(img_array)
axes[0, 0].set_title("Original Image")

axes[0, 1].imshow(rotated_img)
axes[0, 1].set_title("Rotated Image (90°)")

axes[1, 0].imshow(flipped_img)
axes[1, 0].set_title("Flipped Image (Horizontally)")

axes[1, 1].imshow(gray_img, cmap="gray")
axes[1, 1].set_title("Grayscale Image")

# Remove axes for better visualization
# for ax in axes.ravel():
#     ax.axis("off")

plt.show()
