from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest


#prefix=> ön ek test_
#postfix=>

class Test_DemoClass:
    def setup_method(self):#her testen önce çağrılır
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.get("https://www.saucedemo.com/v1/index.html") 

    
    #setup=> demoFUNC => TEARDOWN=>
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))      #en fazla 5 saniye olacak şekilde usur-name id'li elemetin görümesini bekle
        UsurName=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        password=self.driver.find_element(By.ID,"password")
        UsurName.send_keys("arık böke")
        password.send_keys("PASSWORD")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"login-button")))
        LoginButton=self.driver.find_element(By.ID,"login-button")     
        sleep(1)
        LoginButton.click()
        # errorMesage=self.driver.find_element(By.__class__,"//*[@id='login_button_container']/div/form/h3")        
        # testResult=errorMesage.text=="Epic sadface: Username and password do not match any user in this service"
        # print(f"Test sonucu : {testResult}")
    
    #3A act arrnage Assert    
    def teardown_method(self):#her testen sonra çağrılır
        self.driver.quit()
    
    
  
TestClass=Test_DemoClass()
TestClass.setup_method()
TestClass.test_invalid_login()
TestClass.teardown_method()

