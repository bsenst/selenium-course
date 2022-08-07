from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

import math

url = "http://SunInJuly.github.io/execute_script.html"

try:

  browser = webdriver.Chrome("chromedriver",options=options)
  browser.get(url)

  x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
  answer = math.log(abs(12*math.sin(int(x))))
  
  browser.find_element(By.XPATH, "//input").send_keys(answer)

  option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
  browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
  option1.click()

  option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
  browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
  option2.click()

  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(3)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла