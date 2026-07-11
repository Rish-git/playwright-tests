import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page = browser.new_page()
        yield browser
        browser.close()
    
def test_login_blank_username(page):
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button" , name="Login").click()
    page.wait_for_load_state("networkidle")

    #assert error appears
    assert page.get_by_text("Required").first.is_visible()

def test_login_blank_password(page):
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("")
    page.get_by_role("button" , name="Login").click()
    page.wait_for_load_state("networkidle")

    #assert error appears
    assert page.get_by_text("Required").first.is_visible()

def test_login_wrong_password(page):
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("wrong")
    page.get_by_role("button" , name="Login").click()
    page.wait_for_load_state("networkidle")

    #assert error appears
    assert page.get_by_text("Invalid Credentials").first.is_visible()

def test_login_success(page):
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button" , name="Login").click()
    page.wait_for_load_state("networkidle")

    #assert error appears
    assert page.get_by_role("Heading", name="Dashboard").is_visible()
