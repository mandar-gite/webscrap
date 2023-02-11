import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
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
submit = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
# click on submit button 
submit.click()

time.sleep(60)  # Let the user actually see something!

driver.quit()
'''

def identify_urls():
    search_results = driver.find_elements(By.CLASS_NAME, "yuRUbf")
    return search_results


def extract_urls(search_results):
    # iterate the search_results to extact the linked-in profile urls
    for result in search_results:
        lnkdin_url = result.find_element(By.CSS_SELECTOR, 'a[href]').get_attribute('href')
        lnkdin_urls.append(lnkdin_url)
    return lnkdin_urls


def click_next():
    next_bttn = driver.find_element(By.XPATH, xpath_next)
    next_bttn.click()
    time.sleep(5)


def google_safe():
    return random(300, 1500)
