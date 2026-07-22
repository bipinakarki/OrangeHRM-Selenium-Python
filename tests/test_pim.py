from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage

def test_pim(driver):
    obj=LoginPage(driver)
    obj.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    obj.enter_username("Admin")
    obj.enter_password("admin123")
    obj.click_login()
    dashboard = DashboardPage(driver)
    assert dashboard.verify_dashboard()
    pim = PIMPage(driver)

    pim.click_pim()
    assert"viewEmployeeList" in driver.current_url
    
    pim.click_add_button()

    pim.enter_first_name("Bipina")

    pim.enter_last_name("Karki")

    pim.click_save()

    assert "viewPersonalDetails" in driver.current_url

    print("Employee added successfully")