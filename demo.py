from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome() # открытие браузера
driver.get('https://kazan.bankturov.ru/search-hotel') #переход по ссылке
button1 = driver.find_element(By.LINK_TEXT, 'Поиск туров') # поиск по уникальному тексту
button1.click() # нажатие на кнопку
sleep(4) # задержка на 4 секунды
button2 = driver.find_element(By.CLASS_NAME, 'logo').click # поиск по уникальному классу
driver.find_element(By.CSS_SELECTOR, 'a[href="/kredit3"]').click()
# поиск по селектору
sleep(3)








