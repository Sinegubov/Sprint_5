import pytest
from selenium import webdriver


# Определение нестандартного маркера для передачи url фикстуре
def pytest_configure(config):
    config.addinivalue_line("markers", "url(link): mark test with a specific URL")


@pytest.fixture(scope='function')
def run_webdriver(request):
    base_url = request.node.get_closest_marker("url").args[0]

    def driver_teardown():
        driver.quit()

    driver = webdriver.Chrome()
    driver.get(base_url)

    request.addfinalizer(driver_teardown)

    return driver
