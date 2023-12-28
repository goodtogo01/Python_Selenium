from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


@pytest.fixture(autouse=True)
def setup(browser):
    if browser == "chrome":
        print("\nLaunching chrome browser............................")
        driver = webdriver.Chrome()
    elif browser == "id":
        print("\nLaunching Internet Explore browser............................")
        driver = webdriver.Ie()
    elif browser == "safari":
        print("\nLaunching safari browser............................")
        driver = webdriver.Safari()
    else:
        print("\nLaunching firefox browser............................")
        driver = webdriver.Firefox()

    driver.delete_all_cookies()
    driver.maximize_window()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI / Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Project Name"] = "Commerce App"
    session.config.stash[metadata_key]["Module Name"] = "User Operation"
    session.config.stash[metadata_key]["Author Name"] = "Khosruz zaman"


# Hooks for delete or modify environment info
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)


def pytest_html_report_title(report):
    report.title = "Commerce Application"
