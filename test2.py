from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome() # открытие браузера
driver.get('https://kazan.bankturov.ru/search-online') #переход по ссылке


driver.find_element(By.CSS_SELECTOR, 'a[href="/kredit3"]').click()

sleep(3)