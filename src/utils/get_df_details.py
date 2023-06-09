import requests
import json
import pandas as pd
import yaml
import sys
sys.path.append('../../')
import config
import yaml
import re
from time import sleep
from utils.request import *


# yaml_file = open("../config/config.yaml")
# cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

def get_ItemCatid(API_spx,dict_product):
  '''
    Input: API shopee in recommend menu
    Output: dataframe include details information about all product recommend
  '''
  df = pd.DataFrame()
  for catid in dict_product.keys():
    offset= 0
    limit= 60
    offset_var = 60
    # limit_var = 60
    for i in range(0, 5):
      API = API_spx + "&catid=" + str(catid) + "&limit=" + str(limit) +  "&offset=" + str(offset)
      json_load = request_API(API)
      if df.shape[0] == 0:
        df = pd.json_normalize(json_load['data']['sections'][0]['data']['item'])
      else:
        new_df = pd.json_normalize(json_load['data']['sections'][0]['data']['item'])
        df = pd.concat([df, new_df], ignore_index=True)
      offset = offset + offset_var
    sleep(5)
  return df
