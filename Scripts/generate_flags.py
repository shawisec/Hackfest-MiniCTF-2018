import os
import glob
import re
import string
from random import *
min_char = 12
max_char = 15
allchar = string.ascii_letters + string.digits

for filepath in glob.iglob('../challenges/*'):
    print(filepath)
    with open(filepath+'/.config', 'r') as file :
      filedata = file.read()
    #print(filedata)
    newflag = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    filedata = re.sub(r"FLAG-\w+", "FLAG-"+newflag, filedata)
    print(filedata)
    with open(filepath+'/.config', 'w') as file:
      file.write(filedata)
    with open(filepath+'/.config', 'r') as file :
      filedata = file.read()
    #print(filedata)
