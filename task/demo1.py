#
#
#
# # from PIL import Image
# # from pytesseract import image_to_string
# # img=Image.open('C:\\Users\\Karimi Infotech\\PycharmProjects\\task\\1.jpg',"rb")
# # text=image_to_string(img)
# # print(text)
#
#
# import pytesseract
# from PIL import Image
# img=Image.open('C:\\Users\\Karimi Infotech\\Downloads\\task1.png')
# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
# r=pytesseract.image_to_string(img,lang="eng")
# print(r)

import cv2
from PIL import Image
import pytesseract
import numpy as np
src_path="C:\\Users\Karimi Infotech\Downloads\task1.png"
def get_data(img_path):
    img=cv2.imread(img_path)
    img=cv2.cvtColor()