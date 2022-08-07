from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

url = "http://suninjuly.github.io/explicit_wait2.html"

try:

  browser = webdriver.Chrome("chromedriver",options=options)
  browser.get(url)
  
  btn = browser.find_element(By.XPATH, "//button")

  while True:
    price = browser.find_element(By.XPATH, "//h5[@id='price']").text[1:]
    if price != "" and int(price) == 100:
      break

  btn.click()

  import math
  x = (browser.find_element(By.XPATH, "//span[@id='input_value']").text)
  ans = str(math.log(abs(12*math.sin(int(x)))))
  print(x, ans)
  field = browser.find_element(By.CSS_SELECTOR, ".form-control")
  field.send_keys(ans)

  browser.find_element(By.XPATH, "//button[@id='solve']").click()


finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(3)
  
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла