from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(driver,10)

        self.username=(By.NAME,"username")
        self.password=(By.NAME,"password")
        self.login_button=(By.CSS_SELECTOR,"button[type='submit']")
    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        time.sleep(1)
    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        time.sleep(1)
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    