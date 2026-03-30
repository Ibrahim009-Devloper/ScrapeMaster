from config.setting import *
from utils.sever import DataSever
from utils.logger import log_maker
import re
import pandas as pd
from scrapers.Amazon.locators import AmazonLocators
from utils.browser import Browser_setup
from concurrent.futures import ThreadPoolExecutor



import os



class Amazon_link_scraper():
    logger = log_maker.log_Gen()

    def __init__(self,page):

         self.page = page
         self.total_page = Total_page_to_scrape_link
         self.search_quary = scarch_quary
         self.folder_path = folder_path
         
         self.product_url = []

    def clean_Amazon_url(self,url):
        matching = re.search(r"(dp|gb/product)/([A-Z0-9]{10})",url)
        if matching:
            return f"https://www.amazon.com/dp/{matching.group(2)}"
    
        asin_in_ad = re.search(r"dp%2F([A-Z0-9]{10})", url)
        if asin_in_ad:
            return f"https://www.amazon.com/dp/{asin_in_ad.group(1)}"
        return url.split("?")[0]



    def start_link_scrape(self):
        self.logger.info("*******start link scraping*******")
        try:
            
            for page_no in range(1,self.total_page +1):
                    print("scrapint page no: ", page_no)
                    target_url = f"https://www.amazon.com/s?k={ self.search_quary}&page={page_no}"
                    try:
                       
                        self.page.goto(target_url,timeout=timeout)
                        
                        self.page.wait_for_load_state("load")
                        product_link = self.page.locator(AmazonLocators.Amazon_link_page_get_link_locator)
                        product_link.first.wait_for(state="visible",timeout=timeout)
                        count = product_link.count()
                        product_links = product_link.all()
                        for item in product_links:
                            link = item.get_attribute("href")
                            full_link = f"https://www.amazon.com{link}" if link.startswith("/") else link
                            short_link = self.clean_Amazon_url(full_link)
                            self.product_url.append({"product_links": short_link})
                        

                            

                    except Exception as e:
                        self.logger.error(f"****some error has orccard in link scraper page{e}")



        finally:
            
            DataSever.save_link_to_excel(self.product_url,self.folder_path,"Amazon_links.xlsx")
            self.logger.info(f"*******data sucessfully save to Data/row_data/Amazon_links.xlsx file*******")

                     


                     
if __name__ == "__main__":
    scraper =Amazon_link_scraper()
    
    scraper.start_link_scrape()
        