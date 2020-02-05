

#1.读取输入图像
import skimage.data

import matplotlib.pyplot as plt
#Reading the image
img = skimage.data.chelsea()
print(img.shape)
plt.imshow(img)
plt.show()
#Converting the image into gray.
img = skimage.color.rgb2gray(img)
print(img.shape)
plt.imshow(img)
plt.show()

#2.准备滤波器
import numpy
l1_filter = numpy.zeros((2,3,3))
#按如下方式覆滤波器的值，以检测垂直和水平边缘。
l1_filter[0,:,:] = numpy.array([[[-1,0,1],
                                 [-1,0,1],
                                 [-1,0,1]]])
l1_filter[1,:,:] = numpy.array([[[1,1,1],
                                 [0,0,0],
                                 [-1,-1,-1]]])
print(l1_filter)
#3.卷积层
