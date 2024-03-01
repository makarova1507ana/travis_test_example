import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example(browser):
    browser.get("https://www.wikipedia.org/")
    assert "Wikipedia" in browser.title
