import re
from selenium import webdriver

# Getting link from the user 
link = input("Enter link here >>> ")

# initialize our chrome driver
chrome_driver = "/Users/ashwa/Desktop/drivers/chromedriver"
driver = webdriver.Chrome(chrome_driver)
driver.get(link)

# get the page source 
page_source = driver.page_source

# REGEX to find emails 
EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

# An empty list to add all the emails
list_of_emails = []

# finding all the emails 
for re_match in re.finditer(EMAIL_REGEX, page_source):
    list_of_emails.append(re_match.group())

# lists all emails that we manage to scrape 
for i, email in enumerate(list_of_emails):
    print(f"{i+1}: {email}")

# close the driver since we don't need it 
driver.close()

