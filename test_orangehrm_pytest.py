import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_login_blank_username(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    
    # Assert error appears
    assert page.get_by_text("Required").first.is_visible()

def test_login_blank_password(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    
    # Assert error appears
    assert page.get_by_text("Required").first.is_visible()

def test_login_wrong_password(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("wrong")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    
    # Assert error appears
    assert page.get_by_text("Invalid credentials").first.is_visible()

def test_login_success(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    
    # Assert success
    assert page.get_by_role("heading", name="Dashboard").is_visible()