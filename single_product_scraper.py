import requests
from bs4 import BeautifulSoup


class SingleProductScraper:
    def __init__(self, product_urls):
        self.page = None
        self.soup = None
        self.product_urls = product_urls
        self.products = []

    def scrape_products(self):
        for index in range(len(self.product_urls)):
            product_url = self.product_urls[index]
            single_product = self.scrape_single_product(product_url)
            # print(single_product)
            self.products.append(single_product)
        # print(self.products)

    def init_scraper(self, product_url):
        self.page = requests.get(product_url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        # print(self.soup.prettify())

    def scrape_single_product(self, product_url):
        self.init_scraper(product_url)
        tab_content = self.soup.find(class_="tabs-content")
        single_product = {}
        title = tab_content.h2.get_text()
        single_product["name"] = title
        description_list = tab_content.select('li')
        # descriptions = self.get_descriptions(description_list)
        description_1 = self.get_description_1(description_list)
        description_2 = self.get_description_2(description_list)
        description_3 = self.get_description_3(description_list)
        description_4 = self.get_description_4(description_list)
        description_5 = self.get_description_5(description_list)
        # single_product["descriptions"] = descriptions
        single_product['description_1'] = description_1
        single_product['description_2'] = description_2
        single_product['description_3'] = description_3
        single_product['description_4'] = description_4
        single_product['description_5'] = description_5

        # print(title)
        # print(descriptions)
        # images_list = self.get_images()
        image_1 = self.get_image_1()
        image_2 = self.get_image_2()
        image_3 = self.get_image_3()
        image_4 = self.get_image_4()
        image_5 = self.get_image_5()
        single_product['image_1'] = image_1
        single_product['image_2'] = image_2
        single_product['image_3'] = image_3
        single_product['image_4'] = image_4
        single_product['image_5'] = image_5

        # single_product["images"] = images_list
        # print(images_list)
        stock_status = self.get_availability()
        single_product["availability"] = stock_status
        # print(stock_status)
        product_code = self.get_product_code()
        single_product["product_code"] = product_code
        # print(product_code)

        # product_price = self.get_price()
        # single_product["price"] = product_price

        old_price = self.get_old_price()
        single_product['old_price'] = old_price
        new_price = self.get_new_price()
        single_product['new_price'] = new_price

        return single_product

    @staticmethod
    def get_descriptions(description_list):
        descriptions = []
        for i in range(len(description_list)):
            descriptions.append(description_list[i].get_text())
        return descriptions

    @staticmethod
    def get_description_1(description_list):
        description_1 = 'NA'
        for i in range(len(description_list)):
            if i == 0:
                description_1 = description_list[i].get_text()
                break
        return description_1

    @staticmethod
    def get_description_2(description_list):
        description_2 = 'NA'
        for i in range(len(description_list)):
            if i == 1:
                description_2 = description_list[i].get_text()
                break
        return description_2

    @staticmethod
    def get_description_3(description_list):
        description_3 = 'NA'
        for i in range(len(description_list)):
            if i == 2:
                description_3 = description_list[i].get_text()
                break
        return description_3

    @staticmethod
    def get_description_4(description_list):
        description_4 = 'NA'
        for i in range(len(description_list)):
            if i == 3:
                description_4 = description_list[i].get_text()
                break
        return description_4

    @staticmethod
    def get_description_5(description_list):
        description_5 = 'NA'
        for i in range(len(description_list)):
            if i == 4:
                description_5 = description_list[i].get_text()
                break
        return description_5

    def get_images(self):
        swiper = self.soup.find(class_="swiper")
        images = []
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                image = image_list[i]['src']
                images.append(image)
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            images.append(image_src)
        return images

    def get_image_1(self):
        swiper = self.soup.find(class_="swiper")
        image_1 = 'NA'
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                if i == 0:
                    image = image_list[i]['src']
                    image_1 = image
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            # images.append(image_src)
            image_1 = image_src
        return image_1

    def get_image_2(self):
        swiper = self.soup.find(class_="swiper")
        image_2 = 'NA'
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                if i == 1:
                    image = image_list[i]['src']
                    image_2 = image
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            # images.append(image_src)
            image_2 = image_src
        return image_2

    def get_image_3(self):
        swiper = self.soup.find(class_="swiper")
        image_3 = 'NA'
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                if i == 2:
                    image = image_list[i]['src']
                    image_3 = image
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            # images.append(image_src)
            image_3 = image_src
        return image_3

    def get_image_4(self):
        swiper = self.soup.find(class_="swiper")
        image_4 = 'NA'
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                if i == 3:
                    image = image_list[i]['src']
                    image_4 = image
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            # images.append(image_src)
            image_4 = image_src
        return image_4

    def get_image_5(self):
        swiper = self.soup.find(class_="swiper")
        image_5 = 'NA'
        if swiper is not None:
            image_list = swiper.find_all('img')
            for i in range(len(image_list)):
                if i == 4:
                    image = image_list[i]['src']
                    image_5 = image
        else:
            image_div = self.soup.find(class_="image")
            image = image_div.find('img')
            image_src = image['src']
            # images.append(image_src)
            image_5 = image_src
        return image_5

    def get_availability(self):
        right = self.soup.find(class_="right")
        li_availability = right.find(class_="p-stock")
        stock_status = li_availability.find(class_="journal-stock").get_text()
        return stock_status

    def get_product_code(self):
        right = self.soup.find(class_="right")
        li_product_code = right.find(class_="p-model")
        product_code = li_product_code.find(class_="p-model").get_text()
        return product_code

    def get_price(self):
        if self.soup.find(class_="product-price"):
            product_price = self.soup.find(class_="product-price").get_text()
        else:
            product_price = {}
            old_price = self.soup.find(class_="price-old").get_text()
            new_price = self.soup.find(class_="price-new").get_text()
            product_price['old_price'] = old_price
            product_price['new_price'] = new_price
        return product_price

    def get_old_price(self):
        old_price = 'NA'
        if self.soup.find(class_="product-price"):
            old_price = self.soup.find(class_="product-price").get_text()
        else:
            old_price = self.soup.find(class_="price-old").get_text()
        return old_price

    def get_new_price(self):
        new_price = 'NA'
        if self.soup.find(class_="price-new"):
            new_price = self.soup.find(class_="price-new").get_text()
        return new_price

    def get_products(self):
        return self.products
