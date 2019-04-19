import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import numpy

#img = cv2.imread("C:\\Users\\Teo\\Desktop\\Testing-Image-Processing\\first_image.png")

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts from BGR to RGB

imageDir = "C:\\Users\\Teo\\Desktop\\Testing-Image-Processing\\images_training"
imageFiles = os.listdir(imageDir)
imageList = [] #this list will contain all the test images
for i in range(0, len(imageFiles)):
    imageList.append(mpimg.imread(imageDir +"\\"+imageFiles[i]))

def display_images(images, cmap=None):
    plt.figure(figsize=(10,10))
    for i, image in enumerate(images):
        plt.subplot(3,2,i+1)
        plt.imshow(image, cmap)
        plt.autoscale(tight=True)
    plt.show()


display_images(imageList)
