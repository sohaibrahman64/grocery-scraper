from categories_scraper.categories_scraper import CategoriesScraper
from home_scraper import HomeScraper
from categories_menu_scraper import CategoriesMenuScraper
from single_product_scraper import SingleProductScraper
from categories_scraper.single_product_category_scraper import SingleProductCategoryScraper

from db.database import Base, engine, DbUtils, Categories, Products, Home


def get_product_urls(products):
    urls = []
    if len(products) != 0:
        for index in range(len(products)):
            product = products[index]
            product_url = product['product_url']
            urls.append(product_url)
    return urls


def get_home_products():
    home_scraper = HomeScraper()
    home_scraper.scrape_products()
    home_page_products = home_scraper.get_products()
    return home_page_products


def get_categories():
    categories_scraper = CategoriesMenuScraper()
    categories_scraper.scrape_categories_new_new()
    some_categories = categories_scraper.get_subcategories()
    return some_categories


def get_single_products():
    single_product_scraper = SingleProductScraper(product_urls)
    single_product_scraper.scrape_products()
    products = single_product_scraper.get_products()
    return products


def get_category_products(categories_dict):
    category_products = {}
    for key in categories_dict:
        categories_list = categories_dict[key]
        for i in range(len(categories_list)):
            category_url = categories_list[i]['url']
            category_name = categories_list[i]['name']
            categories_scraper = CategoriesScraper(category_url)
            categories_scraper.scrape_products()
            products = categories_scraper.get_products()
            category_name = "{0}".format(category_name).replace(' & ', '_') \
                .replace(' ', '_').replace(',', '_').lower().replace('__', '_')
            category_products[category_name] = products
            pass
    return category_products


def get_category_products_new(categories_list):
    category_products = {}
    for i in range(len(categories_list)):
        category_url = categories_list[i]['url']
        category_name = categories_list[i]['name']
        categories_scraper = CategoriesScraper(category_url)
        categories_scraper.scrape_products()
        products = categories_scraper.get_products()
        category_name = "{0}".format(category_name).replace(' & ', '_') \
            .replace(' ', '_').replace(',', '_').lower().replace('__', '_')
        category_products[category_name] = products
    return category_products


def collect_products_per_categories(products):
    product_urls_list = []
    for i in range(len(products)):
        product = products[i]
        product_url = product['product_url']
        product_urls_list.append(product_url)

    pass


def get_product_urls_per_category():
    product_url_with_categories = []
    for key in category_products_dictionary:
        # category_name = key
        for i in range(len(category_products_dictionary[key])):
            products = {}
            category_products = category_products_dictionary[key][i]
            products["category_name"] = key
            products["product_url"] = category_products["product_url"]
            product_url_with_categories.append(products)
    return product_url_with_categories

    pass


def get_single_products_per_category():
    single_products_per_category_scraper = SingleProductCategoryScraper(product_urls_per_category)
    single_products_per_category_scraper.scrape_products_new_new()
    single_products_per_category = single_products_per_category_scraper.get_products_new()
    return single_products_per_category


def create_db():
    Base.metadata.create_all(engine)


def insert_categories():
    db_utils = DbUtils(engine)
    db_utils.insert_records(Categories, categories)


def insert_home_products():
    db_utils = DbUtils(engine)
    db_utils.insert_records(Home, single_products)


def insert_category_products():
    db_utils = DbUtils(engine)
    db_utils.insert_records(Products, single_products_as_per_category)


if __name__ == '__main__':
    home_products = get_home_products()
    categories = get_categories()
    product_urls = get_product_urls(home_products)
    single_products = get_single_products()
    category_products_dictionary = get_category_products_new(categories)
    product_urls_per_category = get_product_urls_per_category()
    single_products_as_per_category = get_single_products_per_category()

    create_db()

    insert_home_products()

    insert_category_products()
