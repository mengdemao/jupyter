#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 修改打印函数
# 覆盖系统
from rich import print

# 设置显示图片
import matplotlib.pyplot as plt

# 导入numpy
import numpy as np

# 导入opencv
import cv2 as cv

# 导入pytorch
import torch
from torch import autograd
import torchvision
import torchvision.transforms as transforms

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
def displayImage(Image):
    plt.imshow(Image)
    plt.axis('off') # 关掉坐标轴为 off
    plt.title('Catch Image') # 图像题目
    plt.show()
    
def displayFrame(frame):
    # 转换RGB顺序
    frame=cv.cvtColor (frame, cv.COLOR_BGR2RGB)
    plt.imshow(frame)
    plt.axis('off') # 关掉坐标轴为 off
    plt.title('Catch Image') # 图像题目
    plt.show()
