import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

login = "mandar.gite@gmail.com"
password = "Cortex@5326"

driver = webdriver.Chrome()   # instanstiate driver class for webdriver
driver.get('http://www.linkedin.com/');
time.sleep(5) # Let the user actually see something!


# locate login id element 
session_key = driver.find_element('name','session_key' )
# send to webdriver the email id 
session_key.send_keys(login)

# locate password element 
session_password =driver.find_element('name','session_password')
# send password to webdriver 
session_password.send_keys(password)

# locate submit button 
submit = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button')
# click on submit button 
submit.click()

time.sleep(60) # Let the user actually see something!

driver.quit()