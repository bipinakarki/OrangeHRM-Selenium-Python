from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.dashboard_header=(By.XPATH,"//h6[text()='Dashboard']")
    def verify_dashboard(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_header)).is_displayed()
    