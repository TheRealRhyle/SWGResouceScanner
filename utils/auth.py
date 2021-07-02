import xml.etree.ElementTree as ET
from requests import Request, Session
import json

def get_auth():
    """Calls the Galaxy harvest auth Endpoint

    Returns:
        payload: the contents of data/deets.json
        session_token: auth token
    """
    with open ('data/deets.json', 'r') as deets:
        payload = json.load(deets)
    r = requests.post('http://www.galaxyharvester.net/authUser.py', data=payload )
    session_token = r.text.split('-')[1]
    return (payload, session_token)

def verify_resource(head, sample_json):
    """Posts resource info to Galaxy Harvester

    Args:
        head (json): the users login deets
        sample_json (json): resource data

    Returns:
        r: request response
    """
    
    # data1 = {"gh_sid":get_auth(),"galaxy":"115","planet":"Tatooine"}
    
    r = requests.post('http://www.galaxyharvester.net/postResource.py/115/' + sample_json)
    return r

def check_resource(res_name):
    exsits = False
    galaxy = 115    
    request = Request(
        'POST',
        'https://www.galaxyharvester.net/getResourceByName.py',
        files = {
            'galaxy': (None, galaxy),
            'name':(None, res_name)
        }
    ).prepare()
    s= Session()
    r = s.send(request)
    root = ET.fromstring(r.content)
    for child in root.iter('*'):
        if child.tag == "resultText":
            ret = (f"{child.tag}: {child.text}")
        elif 'min' in child.tag or 'max' in child.tag:
            continue
        # print(f"{child.tag}: {child.text}")


    return ret

if __name__=="__main__":
    # gh_sid = get_auth().strip("\n")
    r = check_resource('quadofaet')
    print(r)
    # root = ET.fromstring(r.content)
    # print(root.findtext("resultText:"))

    # for child in root.iter('*'):
    #     if child.tag == "resultText":
    #         print(f"{child.tag}: {child.text}")
    #     elif 'min' in child.tag or 'max' in child.tag:
    #         continue
        # print(f"{child.tag}: {child.text}")

    
    
    
