# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:00:45 2019

@author: xxr
"""
from cv2 import cv2  #因为cv2里面还有cv2 所以要这样干！
import numpy as np

#读取原始图片
image= cv2.imread('../shuibiaotupian/shuibiao3.jpg')

#读入一张白色的图
image2=cv2.imread('../shuibiaotupian/white.png')
image3=image2

#图片的缩小，记住比例 的缩放
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
image2=cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)

#图像灰度化处理
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#基于Canny的边沿检测(生成的也是二值图)
canny=cv2.Canny(grayImage,30,180)
#cv2.imshow("canny_image",canny)
#再canny处理图像以后 用hough直线检测
#统计概率霍夫线变换

#  步长         阈值      最小直线长度    最大构成直线的点的间隔
lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 60, minLineLength=30, maxLineGap=8)
for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image2, (x1, y1), (x2, y2), (0, 0, 255), 1)



#这里进行矩形的轮廓检测  !!!应该找 白色的矩形框
image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#黑白颜色颠倒
height, width = image2.shape
dst = np.zeros((height,width,1), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        grayPixel = image2[i, j]
        dst[i, j] = 255-grayPixel


#高斯滤波（使图像模糊，平滑）
#dst=cv2.GaussianBlur(dst,(7,7),0)
"""
cv2.imshow('dst', dst)
contours, hierarchy = cv2.findContours(dst,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
"""
# #绘制直线
"""
max=0
max_i=0
print(len(contours[2]))
for i in range(len(contours)):
         if(5==len(contours[i])):
                max_i=i
cv2.drawContours(image3,contours,-1,(0,255,255),3)
cv2.imshow("draw_img0", image3)
"""

# #绘制矩形
"""
for i in range(0,len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    cv2.rectangle(image3, (x,y), (x+w,y+h), (153,153,0), 5)
cv2.imshow("draw_img0", image3)
"""
#打印矩形
# for i in range(0,len(contours)):
#     x, y, w, h = cv2.boundingRect(contours[i])
#     print(contours[0])
#     cv2.rectangle(image3, (x,y), (x+w,y+h), (255,153,0), 5)

#标准霍夫线变换（但在这里不太实用）
"""
lines = cv2.HoughLines(canny, 1, np.pi/180, 150)
for line in lines:
        rho, theta = line[0]  #line[0]存储的是点到直线的极径和极角，其中极角是弧度表示的。
        a = np.cos(theta)   #theta是弧度
        b = np.sin(theta)
        x0 = a * rho    #代表x = r * cos（theta）
        y0 = b * rho    #代表y = r * sin（theta）
        x1 = int(x0 + 1000 * (-b)) #计算直线起点横坐标
        y1 = int(y0 + 1000 * a)    #计算起始起点纵坐标
        x2 = int(x0 - 1000 * (-b)) #计算直线终点横坐标
        y2 = int(y0 - 1000 * a)    #计算直线终点纵坐标    注：这里的数值1000给出了画出的线段长度范围大小，数值越小，画出的线段越短，数值越大，画出的线段越长
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)    #点的坐标必须是元组，不能是列表。
cv2.imshow("image-lines", image)
"""
# 二值化图片
# #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
"""
threshold_pic =  cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 25, 10)
ret,threshold_pic=cv2.threshold(grayImage,127, 255, cv2.THRESH_BINARY)
cv2.imshow("threshold_image",threshold_pic)
"""
#等待显示（不添加这两行将会报错）
cv2.waitKey(0)
cv2.destroyAllWindows()