import requests
from bs4 import BeautifulSoup


class CategoriesMenuScraper:
    def __init__(self):
        self.page = requests.get('https://www.grocery.com/store/')
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.categories = {}
        self.subcategories = []

    def scrape_categories(self):
        super_menu = self.soup.find(class_="super-menu")
        drop_down = super_menu.find_all(class_="drop-down")
        for i in range(len(drop_down) - 1):
            main_menu_text = drop_down[i].find(class_="main-menu-text").get_text()
            categories_li = drop_down[i].select('li')
            subcategories = []
            for j in range(len(categories_li)):
                subcategories_li_a = categories_li[j].find_all('a')[0].get_text().replace("\n", "")
                subcategories.append(subcategories_li_a)
            self.categories[main_menu_text] = subcategories

    def scrape_categories_new(self):
        super_menu = self.soup.find(class_="super-menu")
        drop_down = super_menu.find_all(class_="drop-down")
        for i in range(len(drop_down) - 1):
            main_menu_text = drop_down[i].find(class_="main-menu-text").get_text()
            categories_li = drop_down[i].select('li')
            subcategories = []
            for j in range(len(categories_li)):
                subcategory = {}
                subcategories_url = categories_li[j].find_all('a')[0]['href']
                subcategories_li_a = categories_li[j].find_all('a')[0].get_text().replace("\n", "")
                subcategories_li_a_alias = categories_li[j].find_all('a')[0].get_text().replace("\n", "").\
                    replace(' & ', '_').\
                    replace(' ', '_').replace(',', '_').lower().replace('__', '_')

                subcategory['name'] = subcategories_li_a
                subcategory['url'] = subcategories_url
                subcategory['alias'] = subcategories_li_a_alias
                subcategories.append(subcategory)
            self.categories[main_menu_text] = subcategories

    def scrape_categories_new_new(self):
        super_menu = self.soup.find(class_="super-menu")
        drop_down = super_menu.find_all(class_="drop-down")
        for i in range(len(drop_down) - 1):
            main_menu_text = drop_down[i].find(class_="main-menu-text").get_text()
            categories_li = drop_down[i].select('li')
            # subcategories = []
            for j in range(len(categories_li)):
                subcategory = {}
                subcategories_url = categories_li[j].find_all('a')[0]['href']
                subcategories_li_a = categories_li[j].find_all('a')[0].get_text().replace("\n", "")
                subcategories_li_a_alias = categories_li[j].find_all('a')[0].get_text().replace("\n", "").\
                    replace(' & ', '_').\
                    replace(' ', '_').replace(',', '_').lower().replace('__', '_')

                subcategory['name'] = subcategories_li_a
                subcategory['url'] = subcategories_url
                subcategory['alias'] = subcategories_li_a_alias
                self.subcategories.append(subcategory)
            # self.categories[main_menu_text] = subcategories

    def get_categories(self):
        return self.categories

    def get_subcategories(self):
        return self.subcategories






