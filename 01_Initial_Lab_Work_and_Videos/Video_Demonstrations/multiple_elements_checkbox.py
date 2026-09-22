# Arpan Mukherjee
# Enrollment - 12023002029022

#identify multiple elements of the same type and use Selenium to find and work with the list of elements

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @id]")

print("Total Checkboxes:", len(checkboxes))
for checkbox in checkboxes:
    print("Checkbox ID:", checkbox.get_attribute("id"))


for chechbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()


time.sleep(5)
driver.quit()
