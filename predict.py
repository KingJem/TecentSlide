'''
predict.py有几个注意点
1、如果想要保存，利用r_image.save("img.jpg")即可保存。
2、如果想要获得框的坐标，可以进入detect_image函数，读取top, left, bottom, right这四个值。
3、如果想要截取下目标，可以利用获取到的top,left,bottom,right这四个值在原图上利用矩阵的方式进行截取。
'''
import cv2
import numpy

from centernet import CenterNet
from PIL import Image

centernet = CenterNet()

for i in range(1, 20):
    path = fr"D:\code\matchineLearn\003_object_detection\ObjectDetectionCenterNet_TecentSlide\img\1\{i}.jpg"
    image = Image.open(path)
    image = centernet.detect_image(image)
    image.show()
