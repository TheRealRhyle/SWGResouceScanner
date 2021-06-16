import json

class Resource:
    def __init__(self, name, type):
        self.resName = name
        self.resType = type
        # self.forceOp = 'verify'
        # self.galaxy = '115'

def class_to_json(resource):
    return json.dumps(resource.__dict__)
    

# if __name__=="__main__":
#     dict1={}
#     with open('outdata\Osab.txt') as fh:
#         for line in fh:
#             desc, v = line.strip().split(": ",1)
#             dict1[desc] = v.strip()
    
#     out_file = open('outdata\Osab.json', 'w')
#     json.dump(dict1, out_file,indent=4)
#     out_file.close()