import requests
import json

def get_auth():
    with open ('data/deets.json', 'r') as deets:
        payload = json.load(deets)
    r = requests.post('http://www.galaxyharvester.net/authUser.py', data=payload )
    return r.text.split('-')[1]


if __name__=="__main__":
    print(get_auth())
