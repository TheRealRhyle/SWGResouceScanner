from time import sleep
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from datetime import datetime, timedelta
import utils.parsedata as par
import utils.auth as a
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
start_time = datetime.now()
output = []

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
    try:
        sample = par.Resource(dict1['Resource Type'], dict1['Resource Class'])
    except KeyError:
        with open ('errorlog.txt', "w") as elog:
            elog.write('Examined item is not a resource or nothing to examined.')
        
        return "KeyError", "KeyError"
    
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

def pseudo_isd():
    # Point(x=336, y=38)
    # Point(x=813, y=959)
    image = ImageGrab.grab(bbox=(336,35,636,975))
    image = np.array(image)
    image_normalized = np.zeros((image.shape[0], image.shape[1]))
    image = cv2.normalize(image, image_normalized, 10, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    # image = cv2.GaussianBlur(image, (1,1), 13)
    image = cv2.resize(image, (700,2000))
    image = cv2.medianBlur(image, 3)
    return image

def dump_to_file():
    # cap = ImageGrab.grab(bbox=(336,38,813,970))
    cap = pseudo_isd()
    # scrape_arr = np.array(cap)
    # cv2.imshow("", cap)
    
    resource = pytesseract.image_to_string(cap)
    res_lines = resource.split('\n')
    for line in res_lines:
        print(line)

    # print(len(res_lines))
    for line in res_lines:
        if line.split(" ")[0]== "" or len(line.split(" ")) > 1:
            continue
        elif line.split(" ")[0] not in output:
            res_name = line.split(" ")[0]
            if res_name == '\x0c' or res_name == '\f' or res_name == 'a':
                continue
            exists = a.check_resource(res_name)
            if exists.split(" ")[1] == "new":
                output.append(f'{line.split(" ")[0]} - Not listed on GH')
        else:
            continue
    # if cv2.waitKey(1) == 27:
    #     break
    # cv2.destroyAllWindows

    with open("dumpfile.txt", "w") as df:
        df.writelines('\n'.join(output))
    # image = get_resource_info()
    # resource_sample = parse_validate_write(image)

    # sample_json = par.class_to_json(resource_sample)
    
    # with open('outdata\sample.json','w') as fi:
    #     # fi.write(sample_json)
    #     fi.write(json.dumps(json.loads(sample_json), indent=4, sort_keys=False))

        # auth.verify_resource(sample_json)    

def test_reader():
    while True:

        # cap = ImageGrab.grab(bbox=(336,38,813,970))
        cap = pseudo_isd()
        # scrape_arr = np.array(cap)
        cv2.imshow("", cap)
        
        resource = pytesseract.image_to_string(cap)
        res_lines = resource.split('\n')
        for line in res_lines:
            print(line)
        
        if cv2.waitKey(1) == 27:
            for line in res_lines:
                if line.split(" ")[0]== "" or len(line.split(" ")) > 1:
                    continue
                elif line.split(" ")[0] not in output:
                    res_name = line.split(" ")[0]
                    if res_name == '\x0c' or res_name == '\f' or res_name == 'a':
                        continue
                    exists = a.check_resource(res_name)
                    if exists.split(" ")[1] == "new":
                        output.append(f'{line.split(" ")[0]} - Not listed on GH')
                else:
                    continue
            # if cv2.waitKey(1) == 27:
            #     break
            # cv2.destroyAllWindows

            with open("dumpfile.txt", "w") as df:
                df.writelines('\n'.join(output))
            break
        cv2.destroyAllWindows

if __name__=="__main__":
    test_reader()

