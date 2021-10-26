import sys

sys.path.append('../Task07')
sys.path.append('../Task04_refactor03')

import json
from Task07_functions import *


def openJson(file_path='./', file_name='my_json.json'):
    json_file = json.load(open(file_path + file_name))
    return json_file


json_post = openJson()
for i in range(len(json_post)):
    print(json_post[i]["post_code"], json_post[i]["post_text"])
