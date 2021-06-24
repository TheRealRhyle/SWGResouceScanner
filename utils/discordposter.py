import requests
import json

with open('data/hooks.json', 'r') as hooks:
    discord_hooks = json.load(hooks)

x = discord_hooks['webooks']

data = {"content":'''
<@&857276487413268542> you may delete this post as it was only made for testing purposes.
```
/way Corellia -6539 -2543 79% Durabafo

Resource Type: Durabafo
Resource Class: Diatium Copper
Cold Resistance: 394
Conductivity: 780
Decay Resistance: 336
Heat Resistance: 395
Malleability: 770
Overall quality: 967
Shock Resistance: 528
Unit Toughness: 592
```'''}


for hook in x:
    r = requests.post(hook,data=data)
    print(r.status_code)
    print(r.content)