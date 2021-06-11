import re
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from datetime import datetime, timedelta
import parsedata
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
start_time = datetime.now()

def get_resource_info():
    capture_examine = ImageGrab.grab(bbox=(14,35,245,250))
    image = np.array(capture_examine)
    image_normalized = np.zeros((image.shape[0], image.shape[1]))
    image = cv2.normalize(image, image_normalized, 10, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(image, (1,1), 1)
    image = cv2.resize(image, (600,600))
    image = cv2.medianBlur(image, 5)
    return image

def parse_validate_write(image):
    dict1 = {}
    resource = pytesseract.image_to_string(image).replace('\n\n','\n')
    resource_line = resource.split('\n')


    for line in range(4,len(resource_line)-1):
        
        k,v = resource_line[line].strip().split(":" , 1)
        dict1[k] = v.strip()

    sample = parsedata.Resource(dict1['Resource Type'], dict1['Resource Class'])
    
    for k,v in dict1.items():
        if k =='Cold Resistance':
            sample.CR=int(v)
        if k == 'Conductivity':
            sample.CD=int(v)
        if k == 'Decay Resistance':
            sample.DR=int(v)
        if k == 'Flavor':
            sample.FL=int(v)
        if k == 'Heat Resistance':
            sample.HR=int(v)
        if k == 'Malleability':
            sample.MA=int(v)
        if k == 'Potential Energy':
            sample.PE=int(v)
        if k == 'Overall quality':
            sample.OQ=int(v)
        if k == 'Shock Resistance':
            sample.SR=int(v)
        if k == 'Unit Toughness':
            sample.UT=int(v)
        if k == 'Entangle Resistance':
            sample.ER=int(v)

    return sample


if __name__=="__main__":
    image = get_resource_info()
    resource_sample = parse_validate_write(image) 
    print(resource_sample.resName)
    resource_sample.forceOp = 'add'
    print(resource_sample.forceOp)



