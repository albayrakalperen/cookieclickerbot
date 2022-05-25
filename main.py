import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)


def big_cookie_count():
    return int(driver.find_element(By.ID, "cookies")
               .text.split()[0].replace(",", ""))


def product_count():
    product_list = []
    enabled_products = driver.find_elements(By.CLASS_NAME, "unlocked")
    for product in enabled_products:
        product_list.append(product.text)
    del product_list[0]
    return len(product_list)


def product_prices(n):
    price_list = []
    for i in range(n+1):
        product_price = driver.find_element(By.ID, f"productPrice{i}")
        price_list.append(int(product_price.text.replace(",", "")))
    return price_list


def big_cookie_clicker(seconds):
    big_cookie = driver.find_element(By.ID, "bigCookie")
    process_time = time.time() + seconds
    while time.time() < process_time:
        big_cookie.click()


def product_clicker():
    worthy_products = product_prices(product_count())
    for i in range(len(worthy_products)-1, -1, -1):
        if big_cookie_count() > worthy_products[i]:
            target_product = driver.find_element(By.XPATH, f'//*[@id="product{i}"]')
            target_product.click()


while True:
    big_cookie_clicker(5)
    product_clicker()


