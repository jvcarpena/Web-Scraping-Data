import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Load env file
load_dotenv()

#===================================== USING BEAUTIFUL SOUP =====================================#
# Create request to get the html from the zillow website.
URL_ZILLOW = os.getenv("URL_ZILLOW")
response = requests.get(url=URL_ZILLOW)
response.raise_for_status()
zillow_html = response.text
# print(zillow_html)

# Create a soup using Beautiful Soup and the zillow html.
soup = BeautifulSoup(zillow_html, "html.parser")

# Create a list of links.
list_of_links = [link.get("href") for link in soup.select(".StyledPropertyCardDataArea-anchor")]
# print(list_of_links)

# Create a list of prices.
list_of_price = [price.text.split()[0].replace("+", "").replace("/", "").
                 replace("mo", "") for price in soup.select(".PropertyCardWrapper__StyledPriceLine")]
# print(list_of_price)

# Create a list of addresses
list_of_addresses = [address.text.strip() for address in soup.select(".StyledPropertyCardDataArea-anchor")]
# print(list_of_addresses)

#===================================== USING SELENIUM =====================================#
# Create chrome option
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_experimental_option("detach", True)

# Create driver
URL_GOOGLE_FORMS = os.getenv("URL_GOOGLE_FORMS")
driver = webdriver.Chrome(options=chrome_option)

for i in range(len(list_of_addresses)):
    driver.get(url=URL_GOOGLE_FORMS)
    time.sleep(4)

    address_input = driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i1"]')
    address_input.send_keys(list_of_addresses[i])
    time.sleep(2)

    price_input = driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i5"]')
    price_input.send_keys(list_of_price[i])
    time.sleep(2)

    link_input = driver.find_element(By.CSS_SELECTOR, value='input[aria-labelledby="i9"]')
    link_input.send_keys(list_of_links[i])
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div['
                                                        '1]/div/span')
    submit_button.click()
    time.sleep(2)


