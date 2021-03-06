import utils.auth as auth
import utils.readscreen as rs
import utils.parsedata as par 
import utils.planet_coords as wp  
import utils.discordposter as discord
from playsound import playsound
import keyboard
import time
# import json

def main_process():
    _login, gh_sid = auth.get_auth()
    gh_sid = gh_sid.strip('\n')
    wp_planet = wp.get_planet()
    wp_way = wp.get_coords()
    getinfo = rs.get_resource_info()

    resource_sample, _ = rs.parse_validate_write(getinfo)
    resource_sample.gh_sid = gh_sid
    resource_sample.planet = wp_planet
    resource_sample.forceOp = "verify"

    sample_json = par.class_to_json(resource_sample)

    # build string as form data
    submit_string = '?'
    test_dict = eval(sample_json)
    for k,v in test_dict.items():
        submit_string = submit_string + k+"="+v+"&"
    return submit_string

while True:
    # . post to Galaxy Harvester
    # ; post to Discord
    if keyboard.read_key() == ".":
        rs.dump_to_file()
        playsound('resources/success1.mp3')
    elif keyboard.read_key() == ",":
        resource_sample, _ = rs.parse_validate_write(rs.get_resource_info())
        playsound('resources/success1.mp3')
    elif keyboard.read_key()=="'":
        break
    
#     if keyboard.read_key() == ".":
#         # wp_planet = wp.get_planet()
#         #  getinfo = rs.get_resource_info()
#         # _, getinfo = rs.parse_validate_write(getinfo)
        
#         getinfo = rs.get_resource_info()
#         resource_sample, _ = rs.parse_validate_write(getinfo)

#         # print(getinfo)
#         # string = main_process()
#         # print(string)

#         print(getinfo)
#         if resource_sample != 'KeyError':
            
#             playsound('resources/success1.mp3')
#         else:
#             playsound('resources/JarJarClumsy.mp3')

#         #     resp = auth.add_resource()
#         #     # resp = discord.post_to_discord(wp_planet, x,y, getinfo)
#         #     if resp == 200 or resp == 204:
#         #         playsound('resources/success1.mp3')
#         #     else:
#         #         playsound('resources/fail1.mp3')
#         # else:
#         #     playsound('resources/JarJarClumsy.mp3')
        
#     elif keyboard.read_key() == ";":
#         wp_planet = wp.get_planet()
#         x,y = wp.get_coords()
#         getinfo = rs.get_resource_info()
#         _, getinfo = rs.parse_validate_write(getinfo)
#         if getinfo != 'KeyError':
#             resp = discord.post_to_discord(wp_planet, x,y, getinfo)
#             if resp == 200 or resp == 204:
#                 playsound('resources/success1.mp3')
#             else:
#                 playsound('resources/fail1.mp3')
#         else:
#             playsound('resources/JarJarClumsy.mp3')
#     elif keyboard.read_key()=="'":

#         break
    
# r = auth.add_resource(login, submit_string)
# print(r.status_code)
# print(r.content)