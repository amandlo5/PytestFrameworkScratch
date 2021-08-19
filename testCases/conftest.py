from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/mumu/PycharmProjects/PytestFrameworkScratch/chromedriver.exe")
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="C:/Users/mumu/PycharmProjects/PytestFrameworkScratch/msedgedriver.exe")
    else:
        driver = webdriver.Chrome(
            executable_path="C:/Users/mumu/PycharmProjects/PytestFrameworkScratch/chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


# Pytest HTML Report
#for adding in html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amol'

#for updating in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
