from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

'wws example'


class brow:
    def __init__(self,item) -> None:
        self.item = item
        self.url_head = "https://www.woolworths.com.au/shop/search/products?searchTerm="
        self.url = self.url_head +item
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
       

    def get_soup_pages(self):
        #get html from url
        # first open browser to get pages, then loop pages to get price and title data
        self.driver.get(self.url)
        #async wait
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.CLASS_NAME, "primary")))
            WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-title-link")))
            # WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CLASS_NAME, "paging-section")))
            #get page html source 
            html = self.driver.page_source
            #use BeautifulSoup to analize
            soup = BeautifulSoup(html, 'lxml')
            #soup tool to get total pages of pagination
            pages = soup.find('span', class_='page-count')
            # only use 2 page search results for now
            if pages != None:
                pages = '2'
            else:
                pages = '1'
            
            return soup, pages
        except TimeoutError:
            print('Internet delay! Quit and try again!')
    
    def get_title_price(self):
        self.lists = []
        self.title_price_list ={}
        pages = self.get_soup_pages()[1]
        #loop 1 or 2 pages
        for page in range(1,int(pages)+1):
            # price_list and titles_list need to be empty every time loop start, to put search results of new page
            prices_list =[]
            titles_list = []
            # then change page number in url if lopp pages
            self.url = self.url+'&pageNumber='+str(page)
            #get soup
            soup = self.get_soup_pages()[0]
            #soup tool to get price in the page
            prices = soup.find_all('div',class_='primary')
            for price in prices:
                prices_list.append(price.get_text()[1:])
            #soup tool to get product title in the page
            titles = soup.find_all('a',class_='product-title-link ng-star-inserted')
            for title in titles:
                titles_list.append(title.get_text())
            #put product title and relative prive in a dict, 1st page: {price: title, price:title,...}
            title_price = dict(zip( prices_list, titles_list))
            #add dict together in a list, append 2,3,4... page {price: title, price:title,..., price: title, price:title,...}
            self.title_price_list.update(title_price)
            self.url = self.url_head +self.item
        # add item search results in list: [{price: title, price:title,...price: title, price:title,...}]
        # once applying user input, will loop items, so get a results list of different items, and same item in one dict
        self.lists.append(self.title_price_list)
        return self.lists
    
    def closewindow(self):
        self.driver.close()
    

