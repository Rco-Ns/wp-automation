from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:/Users/SDN SITUGUNTING 3/PycharmProjects/Automation Testing/Drivers/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.ebay.com/")

#Type any search string in the search bar. For example: MacBook.
search_type =driver.find_element_by_id("gh-ac")
search_type.send_keys("MacBook")

#Change the Search category.For example: Computers / Tablets & Networking and click Search.
category = driver.find_element_by_class_name("gh-sb ")
category.click()

select = Select(driver.find_element_by_id("gh-cat"))
select.select_by_value("58058")

search = driver.find_element_by_id("gh-btn")
search.click()