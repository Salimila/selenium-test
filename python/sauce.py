from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class Test_sauce:     
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/v1/index.html")     
        
    def test_invalid_login(self):# kişinin yanlış giriş yaptığı senaryo fonksiyonu
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
        errorMesage=self.driver.find_element(By.__class__,"//*[@id='login_button_container']/div/form/h3")        
        testResult=errorMesage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu : {testResult}")
    
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/v1/index.html")     
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.   ID,"user-name")))
        UsurName=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.   ID,"password")))
        password=self.driver.find_element(By.ID,"password")
        self.driver.execute_script("window.scrollTo(0,500)")
        #Action Chains
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(UsurName,"problem_user")
        actions.send_keys_to_element(password,"secret_sauce")
        actions.perform()
        # UsurName.send_keys("problem_user")
        # password.send_keys("secret_sauce")
        LoginButton=self.driver.find_element(By.ID,"login-button")
        LoginButton.click()
        self.driver.execute_script("window.scrollTo(0, 500);")
    
TestClass=Test_sauce()
TestClass.test_invalid_login()
TestClass.test_valid_login()
