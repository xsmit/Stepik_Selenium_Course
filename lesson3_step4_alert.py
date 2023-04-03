from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12*math.sin(int(x))), math.e)


chrome_service_executable_path = "C:\\Users\\yury.ageev\\AppData\\Local\\Programs\\ChromeDriver\\chromedriver.exe"
chrome_service = Service(executable_path=chrome_service_executable_path)
browser = webdriver.Chrome(service=chrome_service)

initial_url = "http://suninjuly.github.io/alert_accept.html"
browser.get(initial_url)

btn_journey = browser.find_element(By.TAG_NAME, "button")
btn_journey.click()

alert = browser.switch_to.alert
alert.accept()

x_val = browser.find_element(By.ID, "input_value").text
y_val = calc(x_val)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(y_val))

btn_submit = browser.find_element(By.TAG_NAME, "button")
btn_submit.click()

time.sleep(30)
browser.quit()
