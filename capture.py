#!/usr/bin/env python
import numpy as np
import cv2

if _name_=='_main_':
	cap=cv2.VideoCapture(0)
	ret,frame=cap.read()
	cv2.imwrite('rpi_test.jpg',frame)
	print("Hello world")
	cap.release()

