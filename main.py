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

if __name__ == "__main__":
    test_example()  # Вызов функции run_test() для запуска тестов
