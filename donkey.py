from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from time import sleep

path_service = Service(executable_path="/home/pneumothorax/Documents/pythonScripts/chromedriver")

driver = webdriver.Chrome(service=path_service)

link = input("Enter the link of the Google Form: ")
driver.get(link)
#https://forms.gle/XSFUAVykDFXK1MAq6   

# First button
button_submit = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span")))
#button_submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span")
button_submit .click()

# Email input
email_input = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "identifierId"))).send_keys("luigi.mamani.r@uni.pe")
#email_input = driver.find_element(By.ID, "identifierId").send_keys("luigi.mamani.r@uni.pe")

# Next button
next_button = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button")
next_button.click()

# Password input 

password_input = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys("paolavesala123")
#password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("paolavesala123")

# Next button
next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()

# AUTENTICATION COMPLETE!

# Name input
name_input = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys("Luigi Mamani")

# Last name input

# Phone input

# Students code input
sleep(50)
driver.quit()