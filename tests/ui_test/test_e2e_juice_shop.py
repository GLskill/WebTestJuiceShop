import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True if you don't need a GUI
        yield browser
        browser.close()


def test_click_element(browser):
    page = browser.new_page()
    base_url = "http://localhost:3000"
    page.goto(base_url)
    time.sleep(20)
    page.close()

