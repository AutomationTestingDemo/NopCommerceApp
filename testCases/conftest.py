from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver= webdriver.Chrome(ChromeDriverManager().install())
    elif browser=="firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):     #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to the setup
    return request.config.getoption("--browser")

############Pytest html report##############
#it is a hook to add environment info to the html report
def pytest_configure(config):
    config._metadata['Project Name']='NopCommerceApp'
    config._metadata['Module Name'] = 'Commerce'
    config._metadata['Tester'] = 'Kalyan'

#This is hook to delete/modify the env info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)