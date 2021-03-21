import pytest
from selenium import webdriver


# pytest runtime variable - initialization and declaration
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# defining scope as class will let the test methods in this file execute once before the class is initiated
@pytest.fixture(scope="class")
# setup will setup everything before test starts execution
# request is an instance for your fixture
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    # driver will be sent to classes where this fixture is being used
    request.cls.driver = driver
    yield
    driver.close()
