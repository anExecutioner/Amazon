import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='package')
def browser():
    driver = webdriver.Edge(service=ChromeService(EdgeChromiumDriverManager().install()))
        
    yield driver
    driver.quit()


