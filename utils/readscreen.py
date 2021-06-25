import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from datetime import datetime, timedelta
import utils.parsedata as par
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

    text_out = []
    for line in range(4,len(resource_line)-1):
        
        if ":" not in resource_line[line]:
            resource_line[line-1] = resource_line[line-1] + " " + resource_line[line] 
        else:
            k,v = resource_line[line].strip().split(":" , 1)
            if k == 'Resource Class':
                v=v.strip().split(" ")
                v=v[::-1]
                v='_'.join(v).lower()
            text_out.append(resource_line[line] + '\n')
            dict1[k] = v.strip().lower()

    sample = par.Resource(dict1['Resource Type'], dict1['Resource Class'])
    
    for k,v in dict1.items():
        if k =='Cold Resistance':
            sample.CR=v
        if k == 'Conductivity':
            sample.CD=v
        if k == 'Decay Resistance':
            sample.DR=v
        if k == 'Flavor':
            sample.FL=v
        if k == 'Heat Resistance':
            sample.HR=v
        if k == 'Malleability':
            sample.MA=v
        if k == 'Potential Energy':
            sample.PE=v
        if k == 'Overall quality':
            sample.OQ=v
        if k == 'Shock Resistance':
            sample.SR=v
        if k == 'Unit Toughness':
            sample.UT=v
        if k == 'Entangle Resistance':
            sample.ER=v
    resname = sample.resName
    with open(f'outdata\{resname}.txt', 'w') as fi:
        fi.writelines(text_out)

    return sample, text_out


if __name__=="__main__":
    image = get_resource_info()
    resource_sample = parse_validate_write(image)

    sample_json = par.class_to_json(resource_sample)
    
    with open('outdata\sample.json','w') as fi:
        # fi.write(sample_json)
        fi.write(json.dumps(json.loads(sample_json), indent=4, sort_keys=False))

    # auth.verify_resource(sample_json)    
    



