import os
import sys
import glob
import re
import string
import json
from random import *
min_char = 20
max_char = 25
allchar = string.ascii_letters + string.digits

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

with open('challenges', 'w') as challenge_files:
    challenge_files.write(json.dumps(challenges))
