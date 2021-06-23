import requests

webhook_url = ['https://discord.com/api/webhooks/856649563574108170/dEBqaUvgretUTdkTjPaBIUJz_tbdGh0PSFoqkYT5ujUQ6cV18umS5XTmBRjkPK148JkE']


data = {"content": '''
Post test:
```
/wp Yavin 4 609 5320

Resource Type: Gano
Resource Class: Conductive Borcarbitic Coppper
Cold Resistance: 149
Conductivity: 183
Decay Resistance: 894
Heat Resistance: 208
Malleability: 735
Overall quality: 932
Shock Resistance: 884
Unit Toughness: 287
```
'''}
response = requests.post(webhook_url[0], json=data)

print(response.status_code)

print(response.content)