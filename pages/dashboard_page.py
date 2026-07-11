class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.user_menu = page.get_by_role("Button").first   #user profile button
        self.logout_button = page.get_by_role("menuitem", name = "Logout")

    def is_dashboard_visible(self):
        return self.dashboard_heading.is_visible()

    def logout(self):
        self.user_menu.click() 
        self.logout_button.click()

