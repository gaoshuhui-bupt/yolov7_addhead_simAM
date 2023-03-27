from turtle import width
import numpy as np
import os
import cv2
import sys

def draw_rect(lines, color_id=0):
    for line in lines:
        print(line)
        cls_id, c_x,c_y,w,h = line.strip().split(" ")
        print(cls_id, c_x,c_y,w,h)
        if int(cls_id)==0 or int(cls_id) ==14 or int(cls_id)==1 :
            c_x,w = int(float(c_x)*wid), int(float(w)*wid)
            c_y,h = int(float(c_y)*hei), int(float(h)*hei)


            xmin,ymin = c_x - w/2, c_y-h/2
            xmax,ymax = c_x + w/2, c_y+h/2
            if color_id==0:
                cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255,0,0), 2)
            else:
                cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0,255,0), 2)


base_path_gt = "../dataset/test1000/img_new/"
base_path_pred = "runs/detect/exp/labels/"

txt_name = base_path_gt + sys.argv[1]
f = open(txt_name)
lines = f.readlines()

f_pred = open(base_path_pred+ sys.argv[1])
lines_pred = f_pred.readlines()

wid = 1920
hei = 1080

img_name = txt_name.split(".txt")[0] + ".jpg"
print(img_name)
img = cv2.imread(img_name)
draw_rect(lines,color_id=0)
draw_rect(lines_pred,color_id=1)


cv2.imwrite("tmp_draw.jpg", img)




