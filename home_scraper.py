import requests
from bs4 import BeautifulSoup


class HomeScraper:
    def __init__(self):
        self.page = requests.get('https://www.grocery.com/store/')
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.product_grid_items = None
        self.products = []

    def scrape_products(self):
        self.product_grid_items = self.soup.find_all(class_="product-grid-item")
        for i in range(len(self.product_grid_items)):
            product = {}
            single_product = self.product_grid_items[i]
            product_details = single_product.find(class_="product-details")
            name = product_details.find(class_="name").get_text().replace("\n", "")
            product_image = single_product.find(class_="image")
            image = product_image.img['data-src']
            price = product_details.find(class_="price").get_text().replace("\n", "")
            product_url = product_details.a['href']
            # print(product_url)
            if ' ' in price:
                price_old = price.split(' ')[0]
                price_new = price.split(' ')[1]
                product['price'] = {'old_price': price_old, 'new_price': price_new}
            else:
                product['price'] = price
            product['name'] = name
            product['image'] = image
            product['product_url'] = product_url
            self.products.append(product)

    def get_products(self):
        return self.products

