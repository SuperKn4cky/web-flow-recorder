from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from web_flow_recorder.data_factory import SignupData
from web_flow_recorder.pages.base_page import BasePage


class SignupPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm_password")
    ACCEPT_TERMS = (By.NAME, "accept_terms")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_BANNER = (By.CSS_SELECTOR, "[data-testid='signup-success']")

    def fill_form(self, data: SignupData) -> None:
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(data.email)
        self.driver.find_element(*self.PASSWORD).send_keys(data.password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(data.confirm_password)

        if data.accepted_terms:
            checkbox = self.driver.find_element(*self.ACCEPT_TERMS)
            if not checkbox.is_selected():
                checkbox.click()

    def submit(self) -> None:
        self.driver.find_element(*self.SUBMIT).click()

    def wait_success(self) -> None:
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_BANNER))
