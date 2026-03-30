import os
import pandas as pd
from utils.logger import log_maker




class DataSever():
    
    @staticmethod
    def save_link_to_excel(data_list,folder_path,file_name,colume_name = "product_links"):
        logger = log_maker.log_Gen()
        if not data_list:
            logger.error("*******data list not found:********")
            
        try:
            logger.info(f"*******sever.py/ saving data to the {folder_path} *******")
            os.makedirs(folder_path,exist_ok=True)
            df = pd.DataFrame(data_list)
            df = df[~df[colume_name].str.contains("javascript",na=False)]
            df = df[df[colume_name] != "#"]
            df.drop_duplicates(subset=colume_name,inplace=True)
            file_path = os.path.join(folder_path,file_name)
            df.to_excel(file_path)
        except Exception as e:
            logger.info(f"*******something was wrong about sever.py. error massge: {e}")

    @staticmethod
    def save_product_to_excel_file(data_test,folder_path,file_name):
        logger = log_maker.log_Gen()
        if not data_test:
            logger.error("*********test_data is not found***********")
            return
        try:
            os.makedirs(folder_path,exist_ok=True)
            df = pd.DataFrame(data_test)
            df = df[~df["Price"].str.contains(" with percent savings",na=False)]
            df.drop_duplicates(inplace=True)
            file_path = os.path.join(folder_path,file_name)
            df.to_excel(file_path,index=False)
        except Exception as e:
            logger.error(f"******an error has occurd happend********* the error is {e}")

        

            





