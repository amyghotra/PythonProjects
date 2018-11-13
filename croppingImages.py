#cropping images

#import the libraries 
import matplotlib.pyplot as plt
import numpy as np

#get name of file of image to be altered
userImg = input("Enter a file name: ")

#read the image
img = plt.imread(userImg)

#Load the image into pyplot
plt.imshow(img)

#show the image
plt.show()

#ask user for the name for the output file
outImg = input("Enter name of output file: ")
t = int(input("Top dimension: "))
b = int(input("Bottom dimension: "))
l = int(input("Left dimension: "))
r = int(input("Right dimension: "))

#crop the original image based on specified demensions
newImg = img[t:b,l:r]

plt.imshow(newImg)
plt.show()

plt.imsave(outImg , newImg)
