import re
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from datetime import datetime, timedelta

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
start_time = datetime.now()

def get_resource_info():
    capture_examine = ImageGrab.grab(bbox=(14,35,245,250))
    image = np.array(capture_examine)
    image_normalized = np.zeros((image.shape[0], image.shape[1]))
    image = cv2.normalize(image, image_normalized, 10, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(image, (1,1), 1)
    return image

def parse_validate_write(image):
    out_file = []
    resource_name = ""
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resource = pytesseract.image_to_string(image).replace('\n\n','\n')
    resource_line = resource.split('\n')

    for line in range(len(resource_line)-1):
        if resource_line[line] != "":
            out_file.append(resource_line[line])
        
        if 'Resource Type:' in resource_line[line]:
            resource_name = resource_line[line].split(': ')[1]
        
    with open(resource_name + ".txt", 'w') as file:
        file.writelines('\n'.join(out_file))

while True:

    image = get_resource_info()
    # resize is width, height
    big = cv2.resize(image, (600,600))
    big = cv2.medianBlur(big, 5)
    cv2.imshow("", big)


    # if datetime.now() > start_time + timedelta(seconds=5):
    parse_validate_write(big)

        # start_time = datetime.now()
        
    # if cv2.waitKey(1) == 27:
    break



