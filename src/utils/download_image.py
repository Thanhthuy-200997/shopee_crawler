import requests
import json
import pandas as pd
import yaml
import sys
import re
sys.path.append('../../')
import config
import pandas as pd
from time import sleep
from utils.request import *
  
def download_image(request_img,df_Details,dir_dest):
  for i in range(len(df_Details)):
    img_url = request_img + df_Details['image'][i]
    img_name = df_Details['image'][i]
    img_name = dir_dest + ''.join(img_name) + '.jpg'
    request_image(img_url, img_name)
  return None
