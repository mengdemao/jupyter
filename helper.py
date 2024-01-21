#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 设置显示图片
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体,解决中文乱码
plt.rcParams["font.family"] = "Source Han Serif CN"

# 导入numpy
import numpy as np

# 导入opencv
import cv2 as cv

# 导入sympy
from sympy import *

# 导入延时模块
import time

# 使用display打印
from IPython.display import display, Latex

# 打开摄像头获取数据
def getFrame():
	cap = cv.VideoCapture(0)
	ret,frame = cap.read()
	cap.release()
	return frame

# 添加一个打印opencv的函数
def displayImage(Image, title):
	plt.imshow(Image)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title) # 图像题目
	plt.show()

def displayFrame(frame, title):
	# 转换RGB顺序
	frame=cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	plt.imshow(frame)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title) # 图像题目
	plt.show()

def display2Frame(frame, title):
	# 转换RGB顺序
	plt.subplot(121)
	frame0 = cv.cvtColor(frame[0], cv.COLOR_BGR2RGB)
	plt.imshow(frame0)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[0]) # 图像题目

	plt.subplot(122)
	frame1 = cv.cvtColor(frame[1], cv.COLOR_BGR2RGB)
	plt.imshow(frame1)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[1]) # 图像题目
	plt.show()


def display4Frame(frame, title):
	# 转换RGB顺序
	plt.subplot(221)
	frame0 = cv.cvtColor(frame[0], cv.COLOR_BGR2RGB)
	plt.imshow(frame0)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[0]) # 图像题目

	plt.subplot(222)
	frame1 = cv.cvtColor(frame[1], cv.COLOR_BGR2RGB)
	plt.imshow(frame1)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[1]) # 图像题目

	plt.subplot(223)
	frame2 = cv.cvtColor(frame[2], cv.COLOR_BGR2RGB)
	plt.imshow(frame2)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[2]) # 图像题目

	plt.subplot(224)
	frame3 = cv.cvtColor(frame[3], cv.COLOR_BGR2RGB)
	plt.imshow(frame3)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[3]) # 图像题目

	plt.show()
	return

def display6Frame(frame, title):
	# 转换RGB顺序
	plt.subplot(231)
	frame0 = cv.cvtColor(frame[0], cv.COLOR_BGR2RGB)
	plt.imshow(frame0)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[0]) # 图像题目

	plt.subplot(232)
	frame1 = cv.cvtColor(frame[1], cv.COLOR_BGR2RGB)
	plt.imshow(frame1)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[1]) # 图像题目

	plt.subplot(233)
	frame2 = cv.cvtColor(frame[2], cv.COLOR_BGR2RGB)
	plt.imshow(frame2)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[2]) # 图像题目

	plt.subplot(234)
	frame3 = cv.cvtColor(frame[3], cv.COLOR_BGR2RGB)
	plt.imshow(frame3)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[3]) # 图像题目

	plt.subplot(235)
	frame4 = cv.cvtColor(frame[4], cv.COLOR_BGR2RGB)
	plt.imshow(frame4)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[4]) # 图像题目

	plt.subplot(236)
	frame5 = cv.cvtColor(frame[5], cv.COLOR_BGR2RGB)
	plt.imshow(frame5)
	plt.axis('off') # 关掉坐标轴为 off
	plt.title(title[5]) # 图像题目
	plt.xticks([])
	plt.yticks([])
	plt.show()
	return