from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class postJournal():
    post_xpath = "//a[@title='Start a Post (Discussion or Journal)']"
    journal_xpath = "//a[text()='Journal Entry']"
    title_id = "title"
    body_xpath = "//textarea[@class='posttextarea']"
    post_button_id = "post-submit"
    body_text_id = "post-inner-content"

    def __init__(self, driver):
        self.driver = driver

    def clickPostIcon(self):
        self.driver.find_element(By.XPATH, self.post_xpath).click()

    def clickJournal(self):
        self.driver.find_element(By.XPATH, self.journal_xpath).click()

    def enterTitle(self, title):
        self.driver.find_element(By.ID, self.title_id).send_keys(title)

    def enterBody(self, body):
        self.driver.find_element(By.XPATH, self.body_xpath).send_keys(body)

    def selectPostMethod(self, value):
        select = Select(self.driver.find_element(By.ID, "privacy"))
        select.select_by_value(value)
    def clickPost(self):
        self.driver.find_element(By.ID, self.post_button_id).click()






