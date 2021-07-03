from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 600)
# driver.implicitly_wait(5)
driver.get('https://web.whatsapp.com/')

time.sleep(30)

row_count = driver.find_element_by_xpath(
    "//div[@aria-label='Chat list']").get_attribute('aria-rowcount')
row_count = int(row_count)
print(row_count)
for x in range(row_count):
    try:
        x = str(x)
        name = driver.find_element_by_xpath(
            "//div[@aria-label='Chat list']//following-sibling::div[contains(@style,'z-index: " + x + "; transition: none 0s ease 0s;')]").text
        # print(name)
        if str(name).startswith('+91'):
            # +91 98920 339612:48 PMHi
            cropped_name = str(name)[0:15]
            print("New contact found as: " + str(cropped_name))
            driver.find_element_by_xpath(
                "//div[@aria-label='Chat list']//following-sibling::div[contains(@style,'z-index: " + x + "; transition: none 0s ease 0s;')]").click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@id='main']/header").click()
            # driver.find_element_by_xpath(
            #     "//div[@id='main']//span[@title=" + cropped_name + "]").click()
            time.sleep(3)
            profile_name = driver.find_element_by_xpath(
                "//div[@id='app']//section/div[1]/div[2]").text
            print("New contact found: "+cropped_name +
                  " with profile name as: " + str(profile_name))
    except:
        pass


# while True:
#     row_count = driver.find_element_by_xpath("//div[@aria-label='Chat list']").get_attribute('aria-rowcount')

#     print(row_count)
