from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chrome_driver= webdriver.Edge()
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)

chrome_driver.find_element(By.NAME,"name").send_keys("MyUser")
chrome_driver.find_element(By.NAME,"email").send_keys("MyUser@gmail.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("hellopwd")
chrome_driver.find_element(By.ID,"exampleCheck1").click()
myselect= Select(chrome_driver.find_element(By.ID, "exampleFormControlSelect1"))
myselect.select_by_visible_text("Female")
chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
chrome_driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=chrome_driver.find_element(By.CLASS_NAME,"alert-success").text
time.sleep(2)

print(message)
assert "Success" in message
print("Page Title :", chrome_driver.title)
print("Page URL : ", chrome_driver.current_url)
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")

#chrome_driver.quit()