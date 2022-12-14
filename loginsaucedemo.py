import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class saucedemotesting(unittest.TestCase):

     def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
     def testloginvalid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(5)
    
     def testlogininvalid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("locked_out_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(5)
    
     def testlogincapital(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("STANDARD_USER")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("SECRET_SAUCE")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(5)
    
     def testloginvalid2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("STANDARD_USER")
        time.sleep(1)
        driver.find_element_by_name("user-name").send_keys("problem_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(5)
    
     def testaddcart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("problem_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(10)
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        time.sleep(3)

     def testcheckproducts(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("problem_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(10)
        driver.find_element_by_id("item_4_title_link").click()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,365)","")
        time.sleep(5)
     
     def testcartlistafteraddandcheckout(self):
       driver = self.driver
       driver.get("https://www.saucedemo.com/")
       time.sleep(10)
       driver.find_element_by_name("user-name").send_keys("problem_user")
       time.sleep(1)
       driver.find_element_by_id("password").send_keys("secret_sauce")
       time.sleep(2)
       driver.find_element_by_id("login-button").click()
       time.sleep(10)
       driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
       time.sleep(2)
       driver.find_element_by_id("shopping_cart_container").click()
       time.sleep(6)
       driver.execute_script("window.scrollBy(0,365)","")
       time.sleep(4)
       driver.find_element_by_id("checkout").click()
       time.sleep(5)

     
     def testlogout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(10)
        driver.find_element_by_name("user-name").send_keys("problem_user")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element_by_id("login-button").click()
        time.sleep(10)
        driver.find_element_by_id("react-burger-menu-btn").click()
        time.sleep(4)
        driver.find_element_by_id("logout_sidebar_link").click()
        time.sleep(5)
   
    
     def tearDown(self):
        self.driver.quit()  

     if __name__ == "_main_": 
        unittest.main()  