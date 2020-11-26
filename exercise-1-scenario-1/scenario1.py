from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.ebay.com/")

#Navigate to Search by category > Electronics > Cell Phones & accessories
shop_category = driver.find_element_by_id("gh-shop-ei")
shop_category.click()

phones_accessories = driver.find_element_by_xpath("//a[text()='Cell phones & accessories']")
phones_accessories.click()

#After the page loads, click Cell Phones & Smartphones in the left hand side navigation section.
phones_smartphones = driver.find_element_by_xpath("//a[text()='Cell Phones & Smartphones']")
phones_smartphones.click()
time.sleep(2)

#Now,click - More refinements (appears on the left at the end of all filters).
more = driver.find_element_by_id("s0-29-13-0-1[1]-0-6-0-0[0]-2[7]_1-3")
more.click()
time.sleep(2)

#Add 3 filters - screen size, Price and Item location appearing in the pop-up and click apply
screen = driver.find_element_by_xpath("/html/body/div[11]/div[2]/div/form/div[1]/div[2]/div[1]/div/fieldset/div[2]/div[1]/label/input")
screen.click()
time.sleep(2)

price = driver.find_element_by_id("c3-mainPanel-price")
price.click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='c3-subPanel-_x-price-textrange']/div/div[1]/div/input").send_keys("3000000")
driver.find_element_by_xpath("//*[@id='c3-subPanel-_x-price-textrange']/div/div[2]/div/input").send_keys("5000000")

location = driver.find_element_by_id("c3-mainPanel-location")
location.click()
asia = driver.find_element_by_xpath("//*[@id='c3-subPanel-location_Asia']/label/input")
asia.click()
time.sleep(1)

apply = driver.find_element_by_xpath("//*[@id='c3-footerId']/div[2]/button")
apply.click()

driver.quit()
print("Test Completed")


