from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Aostaeg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_aostaeg(self):
        driver = self.driver
        driver.get("https://aostage.athenasowl.tv/auth/login")
        driver.maximize_window()
        driver.find_element_by_id("mat-input-0").click()
        driver.find_element_by_id("mat-input-0").clear()
        driver.find_element_by_id("mat-input-0").send_keys("ruturaj.sharbidre@athenasowl.tv")
        driver.find_element_by_id("mat-input-1").clear()
        driver.find_element_by_id("mat-input-1").send_keys("\"Ruturaj@123\"")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//mat-list-option/div/div[2]").click()
        driver.find_element_by_xpath("//span").click()
        driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div/span/mat-select-trigger/div").click()
        driver.find_element_by_xpath("//mat-option[@id='mat-option-3']/span").click()
        driver.implicitly_wait(10)
        time.sleep(10)
        print("opening")
        driver.find_element_by_xpath("(//img[contains(@src,'https://storage.googleapis.com/ao-parameters-kubernetes-dev/ao-platform-ui/assets/cluster_qc.svg')])[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.implicitly_wait(10)
        time.sleep(10)
        driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-0']/app-prompt-dialog/mat-dialog-actions/button[3]/span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//mat-card/div/div/div[2]/div[3]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//mat-card/div/div/div[2]/div[3]").click()
        driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-13']/label/div").click()
        driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-14']/label/div").click()
        driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-15']/label/div").click()
        driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-16']/label/div").click()
        driver.find_element_by_xpath("//button[5]/span").click()
        driver.find_element_by_id("mat-input-1").clear()
        driver.find_element_by_id("mat-input-1").send_keys("hello")
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
