import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setUp(browser):
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = "Inspire"
    config._metadata['Module Name'] = "Verify Journal Posting"
    config._metadata['Tester'] = "Umar"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
