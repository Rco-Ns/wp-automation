from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# User Stories
# As a user, I want to create a public gist.
# As a user, I want to edit an existing gist.
# As a user, I want to delete an existing gist.
# As a user, I want to see my list of gists.

username = "your-github-username"
pwd = "your-github-password"
myGistsURL = "https://gist.github.com/your-gists-url"
gitHubURL = "https://github.com/login"

class CreateModule():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def loginGithub(self):
        self.driver.get(gitHubURL)
        self.driver.find_element_by_id("login_field").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(pwd)
        self.driver.find_element(By.NAME, "commit").click()

    def moveToGist(self):
        self.driver.get(myGistsURL)

    def cickAdd(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "Header-link").click()

    def addPublic(self):
        self.driver.find_element_by_name("gist[description]").clear()
        self.driver.find_element_by_name("gist[description]").send_keys("Gist2")
        self.driver.find_element_by_name("gist[contents][][name]").clear()
        self.driver.find_element_by_name("gist[contents][][name]").send_keys("gist")
        self.driver.execute_script(
            'document.querySelector("textarea.file-editor-textarea").innerText = "text description"')

        submit = self.driver.find_element_by_class_name("BtnGroup")
        submit.find_element(By.TAG_NAME, "button").click()

    def findMyGistList(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[7]/details").click()
        self.driver.find_element(By.XPATH, "//details/details-menu")
        self.driver.find_element(By.LINK_TEXT, "Your gists").click()

    def deleteGists(self):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Rco-Ns'])[3]/following::strong[1]").click()
        delete = self.driver.find_element(By.CLASS_NAME, "application-main")
        delete.find_element(By.CLASS_NAME, "gisthead")
        delete.find_element(By.TAG_NAME, "button").click();
        self.driver.switch_to.alert.accept()
