from playwright.sync_api import sync_playwright
from datetime import datetime
import time

with sync_playwright() as p:
    # Step 1 - Launch browser, headless=False means visible on screen
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 2 - Navigate to Google
    page.goto("https://www.google.com")

    # Step 3 - Wait so you can see it (you suggested this!)
    time.sleep(3)

    # Step 4 - Get the title and print it
    title = page.title()
    print(title)

    # Step 5 - Take screenshot
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"screenshot_{timestamp}.png"
    page.screenshot(path=f"C:/Users/rsingh/Documents/VScodeProject/playwright_test/ss/{filename}")

    #step 6 - close the browser
    browser.close()




