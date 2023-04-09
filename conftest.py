import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose site language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        # вариант для моего компа
        # from selenium.webdriver.firefox.service import Service as FirefoxService
        # import os
        #
        # install_dir = "/snap/firefox/current/usr/lib/firefox"
        # driver_loc = os.path.join(install_dir, "geckodriver")
        # binary_loc = os.path.join(install_dir, "firefox")
        #
        # service = FirefoxService(driver_loc)
        # opts = webdriver.FirefoxOptions()
        # opts.binary_location = binary_loc
        # opts.set_preference("intl.accept_languages", user_language)
        # browser = webdriver.Firefox(service=service, options=opts)

        # общий вариант
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
