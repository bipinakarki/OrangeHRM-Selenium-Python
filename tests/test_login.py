from selenium import webdriver
from pages.login_page import LoginPage

def test_login(driver):
    obj=LoginPage(driver)
    obj.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    obj.enter_username("Admin")
    obj.enter_password("admin123")
    obj.click_login()
    assert "dashboard" in driver.current_url

    print("Successful login")