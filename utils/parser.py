from scrapers.Amazon.locators import AmazonLocators



class AmazonParser():
    def __init__(self,page):
        self.page = page
    


    def get_product_title(self):
        try:
            elemant =self.page.locator(AmazonLocators.Amazon_product_title_locator)
            return elemant.inner_text().strip()
        except Exception:
            return "N/A"
        
    def get_product_price(self):
        try:
            price_el = self.page.locator(AmazonLocators.Amazon_product_price_locator).inner_text()
            return price_el.replace("$","")
        except Exception:
            return "00.0"
        
    def get_product_sels(self):
        try:
            sels_el = self.page.locator(AmazonLocators.Amazon_product_sels_locator)
            return sels_el.inner_text()
        except Exception:
            return "N/A"
        
    def get_product_reating(self):
        try:
            reating_el = self.page.locator(AmazonLocators.Amazon_product_reating_locator)
            return reating_el.inner_text()
        except:
            return "N/A"
        
    
    def get_product_data(self):
        return {
            "Title": self.get_product_title(),
            "Price": self.get_product_price(),
            "monthly sels" : self.get_product_sels(),
            "Rating": self.get_product_reating()
        }
        
