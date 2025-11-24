# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        driver.get("https://www.saucedemo.com/cart.html")
        driver.find_element_by_link_text("2").click()
        driver.get("https://www.saucedemo.com/checkout-step-one.html")
        driver.find_element_by_id("first-name").click()
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("Liz")
        driver.find_element_by_id("last-name").click()
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("San")
        driver.find_element_by_id("postal-code").click()
        driver.find_element_by_id("postal-code").clear()
        driver.find_element_by_id("postal-code").send_keys("12345")
        driver.get("https://www.saucedemo.com/checkout-step-two.html")
        driver.find_element_by_id("finish").click()
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.find_element_by_id("back-to-products").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
