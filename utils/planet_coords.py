# Point(x=1755, y=100)
# Point(x=1919, y=180)

import re
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from time import sleep
# from datetime import datetime, timedelta
# import utils.parsedata as par
# import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# start_time = datetime.now()

def get_planet():
    capture_examine = ImageGrab.grab(bbox=(1806,106,1866,126))
    image = np.array(capture_examine)
    # image_normalized = np.zeros((image.shape[0], image.shape[1]))
    # image = cv2.normalize(image, image_normalized, 10, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(image, (1,1), 1)
    image = cv2.resize(image, (800,400))
    image = cv2.medianBlur(image, 5)
    return image

def get_coords():
    x_coord = ImageGrab.grab(bbox=(1751,166,1800,178))
    y_coord = ImageGrab.grab(bbox=(1864,166,1913,178))
    image_x = np.array(x_coord)
    image_normalized = np.zeros((image_x.shape[0], image_x.shape[1]))
    image_x = cv2.normalize(image_x, image_normalized, 150, 255, cv2.NORM_MINMAX)
    image_x = cv2.resize(image_x, (400,100))
    image_x = cv2.GaussianBlur(image_x, (1,1), 1)
    image_x = cv2.medianBlur(image_x, 5) 
    image_x = cv2.threshold(image_x, 225, 255, cv2.THRESH_BINARY)[1]

    image_y = np.array(y_coord)
    image_normalized = np.zeros((image_y.shape[0], image_y.shape[1]))
    image_y = cv2.normalize(image_y, image_normalized, 150, 255, cv2.NORM_MINMAX)
    image_y = cv2.resize(image_y, (400,100))
    image_y = cv2.GaussianBlur(image_y, (1,1), 1)
    image_y = cv2.medianBlur(image_y, 5) 
    image_y = cv2.threshold(image_y, 225, 255, cv2.THRESH_BINARY)[1]
    return (image_x, image_y)

def parse_validate_write(image):
    dict1 = {}
    resource = pytesseract.image_to_string(image).replace('\n\n','\n')
    resource_line = resource.split('\n')

    print('\n'.join(resource_line))
    # text_out = []
    # for line in range(4,len(resource_line)-1):
        
    #     k,v = resource_line[line].strip().split(":" , 1)
    #     if k == 'Resource Class':
    #         v=v.strip().split(" ")
    #         v=v[::-1]
    #         v='_'.join(v).lower()
    #     text_out.append(resource_line[line] + '\n')
    #     dict1[k] = v.strip().lower()

    # sample = par.Resource(dict1['Resource Type'], dict1['Resource Class'])
    
    # for k,v in dict1.items():
    #     if k =='Cold Resistance':
    #         sample.CR=v
    #     if k == 'Conductivity':
    #         sample.CD=v
    #     if k == 'Decay Resistance':
    #         sample.DR=v
    #     if k == 'Flavor':
    #         sample.FL=v
    #     if k == 'Heat Resistance':
    #         sample.HR=v
    #     if k == 'Malleability':
    #         sample.MA=v
    #     if k == 'Potential Energy':
    #         sample.PE=v
    #     if k == 'Overall quality':
    #         sample.OQ=v
    #     if k == 'Shock Resistance':
    #         sample.SR=v
    #     if k == 'Unit Toughness':
    #         sample.UT=v
    #     if k == 'Entangle Resistance':
    #         sample.ER=v
    # resname = sample.resName
    # with open(f'outdata\{resname}.txt', 'w') as fi:
    #     fi.writelines(text_out)

    # return sample


if __name__=="__main__":
    while True:
        planet_name = get_planet()
        c_x, c_y = get_coords()

        planet_name = pytesseract.image_to_string(planet_name).replace('\n','').replace("\x0c","")
        outx = pytesseract.image_to_string(c_x).replace('\n','').replace("\x0c","")
        outy = pytesseract.image_to_string(c_y).replace('\n','').replace("\x0c","")
        

        print(f'Waypoint: /wp {planet_name} {outx} {outy}')
        # parse_validate_write(get_planet_waypoint())
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyAllWindows()
    
    
    # image = get_planet_waypoint()
    
    # resource_sample = parse_validate_write(image)

    # sample_json = par.class_to_json(resource_sample)
    
    # with open('outdata\sample.json','w') as fi:
    #     # fi.write(sample_json)
    #     fi.write(json.dumps(json.loads(sample_json), indent=4, sort_keys=False))

    # auth.verify_resource(sample_json)    
    



