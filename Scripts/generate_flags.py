import os
import sys
import shutil
import glob
import zipfile
import re
import string
import json
from random import *
min_char = 20
max_char = 25
allchar = string.ascii_letters + string.digits
hostname = 'ctf.shawisec.ca'
challenges = []

for filepath in glob.iglob('../challenges/*'):
    print(filepath)
    with open(filepath+'/.config', 'r') as config_file:
        filedata = config_file.read()
        config_json = json.loads(filedata)


    newflag = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    filedata = re.sub(r"FLAG-\w+", "FLAG-"+newflag, filedata)
    print(filedata)

    with open(filepath+'/.config', 'w') as file:
        file.write(filedata)
        challenges.append(filedata)
        config_json = json.loads(filedata)
    #add new flag to challenge
    with open(filepath+'/'+config_json['flag_file'], 'r') as file:
        filedata = file.read()

    with open(filepath+'/'+config_json['flag_file'], 'w') as file:
        filedata = re.sub(r"FLAG-\w+", config_json['flags'], filedata)
        file.write(filedata)
        print('updated file: '+filepath+'/'+config_json['flag_file'])


imported_challenges = []
imported_keys = []
for idx, chal in enumerate(challenges):
    try:
        chal = json.loads(chal)
        chal["id"] = idx + 1
        del chal['web-folder']
        del chal['flag_file']
        imported_keys.append({'id': chal["id"],'chal': chal["id"], 'type': 'static', 'flag': chal['flags'], 'data': None})
        del chal['flags']

        chal["type"] = "standard"
        chal["max_attempts"] = 0
        imported_challenges.append(chal)
    except KeyError:
        print("Key 'testing' not found")

print(imported_challenges)
if( os.path.isdir("db") ):
    shutil.rmtree('db')
os.mkdir('db')

with open('db/challenges.json', 'w') as challenge_files:
    challenge_files.write("{\"count\": "+str(len(imported_challenges))+ ", \"results\": " +json.dumps(imported_challenges) + ", \"meta\": {}}")

# Replace all $(HOST) in challenges
with open('db/challenges.json', 'r') as config_file:
    filedata = config_file.read()
    filedata = re.sub(r"\$\(HOST\)", hostname, filedata)

with open('db/challenges.json', 'w') as file:
    file.write(filedata)

with open('db/keys.json', 'w') as keys_files:
    keys_files.write("{\"count\": "+str(len(imported_keys))+ ", \"results\": " +json.dumps(imported_keys) + ", \"meta\": {}}")

with open('db/files.json', 'w') as file:
    file.write('')

with open('db/tags.json', 'w') as file:
    file.write('')

with open('db/awards.json', 'w') as file:
    file.write('')

with open('db/tracking.json', 'w') as file:
    file.write('')

with open('db/hints.json', 'w') as file:
    file.write('')

# Change CTF Base Config here
config = '{"count": 1, "results": [{"id": 1, "name": "ShawiSec", "email": "ctf@shawisec.ca", "password": "$bcrypt-sha256$2b,12$v0Z9Z8CfY.efYsZhqgA4oe$kJFBdtOPX7GCO.MLXqksL.z.Oh8WLsW", "website": "https://shawisec.ca", "affiliation": "", "country": "Canada", "bracket": null, "banned": 1, "verified": 0, "admin": 1, "joined": "2018-12-16T19:21:29"}], "meta": {}}'

with open('db/config.json', 'w') as file:
    file.write(config)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('shawisec.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('db/', zipf)
zipf.close()

# Clean rep
if( os.path.isdir("db") ):
    shutil.rmtree('db')
