from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_pom(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    #Navigate to login
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)

    #use loginpage class method
    login_page.login("admin", "admin123")
    assert dashboard_page.is_dashboard_visible()

