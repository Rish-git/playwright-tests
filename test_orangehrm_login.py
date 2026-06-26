from playwright.sync_api import sync_playwright
from datetime import datetime
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    #step 1 - navigate to orangeHRM
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=30000)

    #step 2 - screen shot before filling
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    page.screenshot(path=f"C:/Users/rsingh/Documents/VScodeProject/playwright_test/ss/login_before_{timestamp}.png")

    #step 3 - Fill username using get_by_placeholder
    page.get_by_placeholder("Username").fill("Admin")

    #step 4 - Fill Password using get_by_placeholder
    page.get_by_placeholder("password").fill("admin123")

    #step 5 - click login button using get_by_role
    page.get_by_role("button", name = 'Login' ).click()

    #step 6 wait for  page to load
    page.wait_for_load_state("networkidle")

    error_message = page.get_by_text("Required")
    if error_message.is_visible():
        print("Error message appeared")
    else:
        print("Error not shown")

    #step 7 check if login sucessful - take screenshot
    page.screenshot(path=f"C:/Users/rsingh/Documents/VScodeProject/playwright_test/ss/login_after_{timestamp}.png")

        #step 8 assert login success - check if logout button exists
    #page.get_by_role("dropdown", name = 'manda user' ).click()
    # Get the heading "Dashboard" specifically
    dashboard_heading = page.get_by_role("heading", name="Dashboard")
    if dashboard_heading.is_visible():
        print("✅ Login Successful")
   # if "dashboard" in page.url:
     #   print("Login Successful")
    else:
        print("Logout button NOT visible")
    browser.close()
    

