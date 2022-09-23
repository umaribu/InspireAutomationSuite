import time

import pytest
from selenium.webdriver.common.by import By

from src.Utilities.customLogger import LogGen
from src.Utilities.readProperties import ReadData
from src.pageObjects.postPageObjects import postJournal
from src.pageObjects.signInPageObjects import signInPage


class Test_JournalPost:
    url = ReadData.getURL()
    email = ReadData.getEmail()
    password = ReadData.getPassword()
    logs = LogGen.logs()

    @pytest.mark.regression
    def test_VerifyJournalPost(self, setUp):
        self.driver = setUp
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)
        self.lp = signInPage(self.driver)
        self.lp.clickSigninbutton()
        self.lp.clickSigninLink()
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        time.sleep(3)
        actual_username = self.driver.find_element(By.XPATH, "//h2/a").text
        expected_username = "QA_candidate_1_Umar"
        if actual_username == expected_username:
            self.driver.save_screenshot("./src/Screenshots/Sign_IN_Pass.png")
            self.logs.info("Signed in Successfully with Correct UserName--> Passed")
            assert True
        else:
            self.driver.save_screenshot("./src/Screenshots/Sign_IN_Fail.png")
            self.logs.error("Sign in Failed--> Fail")
            assert False
        self.post = postJournal(self.driver)
        self.post.clickPostIcon()
        self.post.clickJournal()
        self.logs.info("********* Post an Entry in My Journal Tab is opened *********")
        self.post.enterTitle("Allergy symptoms")
        self.post.enterBody("Sneezing.\n"
                            "Itching of the nose, eyes or roof of the mouth.\n"
                            "Runny, stuffy nose. Watery, red or swollen eyes (conjunctivitis)")
        self.post.selectPostMethod("Inspire friends")
        time.sleep(2)
        self.driver.save_screenshot("./src/Screenshots/JournalTab.png")
        self.post.clickPost()
        actual_text = self.driver.find_element(By.XPATH, "//header[@class='header-post']/h1").text
        if "Allergy symptoms" in actual_text:
            self.driver.save_screenshot("./src/Screenshots/Post_Published.png")
            self.logs.info("Post Is Published Successfully--> Passed")
            assert True
        else:
            self.driver.save_screenshot("./src/Screenshots/Post_NotPublished.png")
            self.logs.error("Post is not Published--> Fail")
            assert False
