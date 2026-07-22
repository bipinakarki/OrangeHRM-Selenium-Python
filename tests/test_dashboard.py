from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard(driver):
     login = LoginPage(driver)

     login.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

     login.enter_username("Admin")
     login.enter_password("admin123")
     login.click_login()


     dashboard = DashboardPage(driver)

     assert dashboard.verify_dashboard()
 
     print("Dashboard displayed successfully")