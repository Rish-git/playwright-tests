class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input= page.get_by_placeholder("Username")
        self.password_input= page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("Button" , name="Login")

    def login (self,username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
