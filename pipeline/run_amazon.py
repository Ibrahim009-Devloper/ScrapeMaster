from scrapers.Amazon.links_scraper import Amazon_link_scraper
from scrapers.Amazon.product_scraper import AmazonProductScraper
from utils.logger import log_maker
from utils.browser import Browser_setup
from Data_cleaner.Amazon_product_clean import clean_Amazon_data
import time


logger = log_maker.log_Gen()
browser = Browser_setup()
def start_link_scrapin_pipline():
    logger.info("******starting amazon link scraping page*******")
    
    page1 = browser.newpage()
    link_engine = Amazon_link_scraper(page1)
    link_engine.start_link_scrape()
    page1.close()
    logger.info("*******Amazon link scrape ended********")
    
def start_product_info_scrapint_pipline():
    logger.info("*******starting amazon product page scraping*********")
    page2 = browser.newpage()
    product_engine = AmazonProductScraper(page2)
    product_engine.start_product_scrape()
    page2.close()
    
    logger.info("*****amazon product scrape sucessfully********")

def start_Amazon_data_cleaning():
    logger.info("*******amazon data cleaning has been started**********")
    clean_Amazon_data()

    
    





if __name__ == "__main__":
    start_link_scrapin_pipline()
    time.sleep(3)
    start_product_info_scrapint_pipline()
    start_Amazon_data_cleaning()

