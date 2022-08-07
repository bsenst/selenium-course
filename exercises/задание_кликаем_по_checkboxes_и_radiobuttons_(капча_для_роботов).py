from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/math.html"

try:

  browser = webdriver.Chrome("chromedriver",options=options)
  browser.get(url)

  x_element = browser.find_element(By.XPATH, value="//span[@id='input_value']")
  x = x_element.text
  y = calc(x)
  answer_element = browser.find_element(By.XPATH, value="//input[@id='answer']")
  answer_element.send_keys(y)

  option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
  option1.click()

  option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
  option2.click()

  submit = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
  submit.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(3)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла