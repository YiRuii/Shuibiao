# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:00:45 2019

@author: xxr
"""
from cv2 import cv2  #因为cv2里面还有cv2 所以要这样干！
import numpy as np  


#读取原始图片
image= cv2.imread('../shuibiaotupian/shuibiao1.jpg')

#图片的缩小，记住比例 的缩放 
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#图像灰度化处理
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#基于Canny的边沿检测(生成的也是二值图)
canny=cv2.Canny(grayImage,30,180)
#cv2.imshow('canny', canny)
# 运用OpenCV findContours函数检测图像所有轮廓
contours, hierarchy = cv2.findContours(canny,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
# 对于检测出的轮廓，contourArea限制轮廓所包围的面积的大小,boundingRect识别出正矩形，通过矩形的宽度和高度筛选出想要的图片区域。
# count=0
# minx=10000
# miny=10000
# height=0
# weight=0
for cnt in contours:
    if cv2.contourArea(cnt)>900:  #筛选出面积大于30的轮廓
        [x,y,w,h] = cv2.boundingRect(cnt) #x,y是左上角的坐标，h,w是高和宽
        if  h > 50 and h < 55:  # 根据期望获取区域，即数字区域的实际高度预估28至50之间
            # if(minx>x):
            #     minx=x
            # if(miny>y):
            #     miny=y
            # count+=1
            # height+=h
            # weight+=w
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
#             #截取特定区域
# imagehh = image[miny:miny+height,minx:minx+weight]

cv2.imshow("Photo",image)
# print(str(count)+"jjjjjjjj")




cv2.waitKey(0)
cv2.destroyAllWindows()