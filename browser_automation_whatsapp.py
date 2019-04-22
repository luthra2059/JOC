# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:08:27 2019

@author: om8007
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path=r'Z:\python\driver\geckodriver.exe')  #local path to your firefox driver

driver.get("https:/web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target = '"+91 75649 72281"'           #Enter the target name within double quotes
msg = "Message sent using Python"      #The message you want to send
x_arg = '//span[contains(@title,'+ target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = driver.find_element_by_class_name('_2S1VP')
for i in range(3):               #Run the loop as many times you want to send the msg
    input_box.send_keys(msg+Keys.ENTER)
    
