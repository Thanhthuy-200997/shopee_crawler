import yaml
import sys
sys.path.append('../../')
import config
import requests
import json
# from crawler import *
# from generate_table import *


import json
 
# Data to be written

 
def Create_Json_Category(dict_cate):
    # Serializing json
    json_object = json.dumps(dict_cate, indent=4)

    # Writing to sample.json
    with open("../data/sample.json", "w") as outfile:
        outfile.write(json_object)
    return None