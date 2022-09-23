from selenium.webdriver.common.by import By


class signInPage():
    signin_button_id = "logIn"
    signin_hyperlink_xpath = "//a[text()='Sign in']"
    email_id = "email"
    password_id = "pw"
    login_button_id = "login_submit"

    def __init__(self, driver):
        self.driver = driver

    def clickSigninbutton(self):
        self.driver.find_element(By.ID, self.signin_button_id).click()

    def clickSigninLink(self):
        self.driver.find_element(By.XPATH, self.signin_hyperlink_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.login_button_id).click()


