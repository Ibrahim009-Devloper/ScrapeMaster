import pandas as pd
import os 
from utils.browser import Browser_setup
from config.setting import *
from utils.parser import AmazonParser
from utils.logger import log_maker
from utils.sever import DataSever




class AmazonProductScraper():

    def __init__(self,page):
        self.page = page
        self.logger = log_maker.log_Gen()
        self.input_file = os.path.join(folder_path,"Amazon_links.xlsx")
        self.output_folder = "Data/processed"
        self.product_info = []
        

    def start_product_scrape(self):
        try:
            if not os.path.exists(self.input_file):
                self.logger.info("******Amazon_links.xlsx file not exist********")
                return
            df = pd.read_excel(self.input_file)
            links = df["product_links"].tolist()
           
            self.logger.info("******going to amazon_links.xlsx url and stracting data********")
            for index,url in enumerate(links,start=1):
                print(f"scraping {index}/{len(links)}: {url}")

                try:
                    self.page.goto(url)
                    self.page.wait_for_load_state("load")

                    parser = AmazonParser(self.page)
                    data = parser.get_product_data()
                    data["URL"] = url
                    self.product_info.append(data)

                except Exception as e:
                    self.logger.error(f"******something was wrong in product_scrape.py {e}********")
        except Exception as e:
            self.logger.error(f"******some error has occourd on start_product_scraper*******error is: {e}")

        finally:
                self.page.close()
                if self.product_info:
                    DataSever.save_product_to_excel_file(self.product_info,self.output_folder,"Amazon_product.xlsx")
            


            


if __name__ == "__main__":
    scraper = AmazonProductScraper()
    scraper.start_product_scrape()

        
                

            

        
