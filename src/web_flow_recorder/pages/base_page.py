from __future__ import annotations

from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout_seconds: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout_seconds)

    def visit(self, url: str) -> None:
        self.driver.get(url)
