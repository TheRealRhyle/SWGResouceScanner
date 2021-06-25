import requests
import json

from requests.models import Response
from requests.sessions import session

def get_auth():
    """Calls the Galaxy harvest auth Endpoint

    Returns:
        json: the contents of data/deets.json
        string: auth token
    """
    with open ('data/deets.json', 'r') as deets:
        payload = json.load(deets)
    r = requests.post('http://www.galaxyharvester.net/authUser.py', data=payload )
    session_token = r.text.split('-')[1]
    return (payload, session_token)

def add_resource(head, sample_json):
    
    # data1 = {"gh_sid":get_auth(),"galaxy":"115","planet":"Tatooine"}
    
    r = requests.post('http://www.galaxyharvester.net/postResource.py/115/' + sample_json)
    return r


# if __name__=="__main__":
#     gh_sid = get_auth().strip("\n")
#     sr = {"resName": "Pierae", "resType": "Neutronium Steel", "forceOp": "add", "CR": 405, "CD": 303, "DR": 716, "HR": 801, "OQ": 522, "SR": 690, "gh_sid": "bb99d6cee52a642d37f7c0576846973cfc61c82b", "galaxy": 115, "planet": "corellia"}
    
#     add_resource(sr)
