from utils.get_df_details import *
from utils.request import *
from utils.download_image import *
from utils.Createjson_Category import *
import yaml
import sys
sys.path.append('../../')
import config
import re
import logging

logging.basicConfig(filename="../log/logging.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# yaml_file = open("../config/config.yaml")
yaml_file = open("../config/config.yaml", encoding='utf8')
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
API_spx = cfg['API']['API_spx']
request_img = cfg['API']['request_img']
dict_product_ForHer = cfg['dict_product_ForHer']
dict_product_ForHim = cfg['dict_product_ForHim']
path_rs = cfg['data']['result']


def main():
        # df_Details_ForHer = get_ItemCatid(API_spx,dict_product_ForHer)
        # print(len(df_Details_ForHer))
    try:
        df_Details_ForHer = get_ItemCatid(API_spx,dict_product_ForHer)
        print(len(df_Details_ForHer))
        logger.info(f'Get {len(df_Details_ForHer)} details product for her sucessful -------------------------')
        download_image(request_img,df_Details_ForHer,path_rs)
        logger.info(f'Download {len(df_Details_ForHer)} image for her sucessful -------------------------')
        df_Details_ForHim = get_ItemCatid(API_spx,dict_product_ForHim)
        logger.info(f'Get {len(df_Details_ForHim)} details product for him sucessful -------------------------')
        download_image(request_img,df_Details_ForHim,path_rs)
        logger.info(f'Download {len(df_Details_ForHim)} image for her sucessful -------------------------')
    except Exception as e:
        logger.error(f'Fail with error {e}')
        pass
if __name__ == "__main__":
    main()