from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()

url = "http://suninjuly.github.io/redirect_accept.html"

try:
  browser = webdriver.Chrome("chromedriver",options=options)
  browser.get(url)

  btn = browser.find_element(By.XPATH, "//button")
  btn.click()

  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)

  import math
  x = (browser.find_element(By.XPATH, "//span[@id='input_value']").text)
  ans = str(math.log(abs(12*math.sin(int(x)))))
  print(x, ans)
  field = browser.find_element(By.CSS_SELECTOR, ".form-control")
  field.send_keys(ans)

  browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(3)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла