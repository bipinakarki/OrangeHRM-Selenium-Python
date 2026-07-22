from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class PIMPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.pim_menu=(By.XPATH,"//span[text()='PIM']")
        self.add_button=(By.XPATH,"//button[normalize-space()='Add']")
        self.first_name=(By.NAME,"firstName")
        self.middle_name=(By.NAME,"middleName")
        self.last_name=(By.NAME,"lastName")
        #self.save_button = (By.CSS_SELECTOR,"button[type='submit']")
        self.save_button = (By.XPATH,"//button[@type='submit']")

    
    def click_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()
        time.sleep(2)

    def click_add_button(self):

        self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        ).click()
        time.sleep(3)

    def enter_first_name(self, firstname):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(firstname)
        time.sleep(2)
    def enter_last_name(self, lastname):

        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(lastname)
        time.sleep(2)
    def click_save(self):

        self.wait.until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
        self.wait.until(
        EC.url_contains("viewPersonalDetails")
        )