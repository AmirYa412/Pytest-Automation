from selenium.webdriver.common.by import By


class HomePageLocators(object):
    HOMEPAGE_MAIN_LOGO = (By.CSS_SELECTOR, "div[class='app_logo']")
    HOMEPAGE_ITEM_TITLE = (By.CSS_SELECTOR, "div[class='inventory_item_name']")
    HOMEPAGE_ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    SORT_BUTTON = (By.XPATH, "//select[@data-test='product_sort_container']")
    SORT_DROPDOWN_OPTIONS = (By.XPATH, "//select[@data-test='product_sort_container']")
