import datetime

import pytest_html
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


# Parameterize with fixture ==== 'params=["First Itr", "Second Itr"]'

@pytest.fixture(autouse=True)
def setup(request, browser):
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


def pytest_html_duration_format(duration):
    duration_timedelta = datetime.timedelta(seconds=duration)
    time = datetime.datetime(1, 1, 1) + duration_timedelta
    return time.strftime("%H:%M:%S")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://github.com/goodtogo01/Reports.git"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
