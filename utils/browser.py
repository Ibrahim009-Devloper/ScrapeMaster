from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
from utils.logger import log_maker
from config.setting import proxy





logger = log_maker.log_Gen()

logger.info("*******Browser is connecting to the seleniumbase cdp mode to undetecteble**********")

class Browser_setup():
    def __init__(self):
        
        
        self.sb = sb_cdp.Chrome(uc=True,headless = True)

        endpoint_url = self.sb.get_endpoint_url()
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.connect_over_cdp(endpoint_url)

    def newpage(self):
        context = self.browser.new_context(proxy=proxy)
        return context.new_page()
    
    def close(self):
        self.browser.close()
        self.playwright.stop()
        


        

        

            


