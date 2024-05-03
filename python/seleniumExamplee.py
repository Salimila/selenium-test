from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
input=driver.find_element(By.NAME,"q")
sleep(5)
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME,"btnK") 
sleep(2)
searchButton.click()
sleep(2)
firsResult=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
firsResult.click()

listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda (len{listOfCourses})kurs var ")

while True:
    continue