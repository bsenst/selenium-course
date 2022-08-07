from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

url = "http://suninjuly.github.io/find_xpath_form"
try:
  browser = webdriver.Chrome("chromedriver",options=options)
  browser.get(url)

  input1 = browser.find_element(by="name", value="first_name")
  input1.send_keys("Ivan")
  input2 = browser.find_element(by="name", value="last_name")
  input2.send_keys("Petrov")
  input3 = browser.find_element(by="name", value="firstname")
  input3.send_keys("Smolensk"),
  input4 = browser.find_element(by="id", value="country")
  input4.send_keys("Russia")

  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(3)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла