from PIL import Image
import numpy as np

img = Image.open('image.jpg')

img_array = np.array(img)

print("Форма массива:", img_array.shape)
print("Тип данных:", img_array.dtype)

gray = 0.299 * img_array[:,:,0] + 0.587 * img_array[:,:,1] + 0.114 * img_array[:,:,2]

print("Форма серого:", gray.shape)
print("Тип данных:", gray.dtype)

rotated = np.flip(gray.T,axis=0)

kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

blurred = np.zeros_like(rotated)

for i in range(1, rotated.shape[0] - 1):
    for j in range(1, rotated.shape[1] - 1):
        patch = rotated[i-1:i+2, j-1:j+2]
        blurred[i, j] = np.sum(patch * kernel)