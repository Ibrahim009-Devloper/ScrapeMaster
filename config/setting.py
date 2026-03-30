import random


base_url = "https://www.amazon.com/"
scarch_quary = "electronics item"

timeout = 10000

retry_count = 1

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


Total_page_to_scrape_link = 100


folder_path = "Data/row_data"

proxy = [{
    "server": "31.59.20.176:6754",  
    "username": "brphuhss",
    "password": "37o3hk48y1u5"},

    {
    "server": "23.95.150.145:6114",  
    "username": "brphuhss",
    "password": "37o3hk48y1u5"},

    {"server": "198.23.239.134:6540",  
    "username": "brphuhss",
    "password": "37o3hk48y1u5"},
    {"server": "45.38.107.97:6014",  
    "username": "brphuhss",
    "password": "37o3hk48y1u5"}]


proxy = random.choice(proxy)


