from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

driver.find_element(By.CSS_SELECTOR, ".gb_A").click() #нажимаем на иконку все приложения

sleep(10)

driver.quit()


