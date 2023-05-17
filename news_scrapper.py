# Required imports 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import datetime
from selenium.webdriver.chrome.options import Options
import os 
import sys


script_path = os.path.dirname(sys.executable)

options = Options()
options.headless = True

website = "https://www.aljazeera.com/news/"
path = "C:\\Users\\mabde\\Downloads\\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="gc__content"]')

titles = []
descriptions = []
links = []

output = {
    'Headline': titles,
    "Description": descriptions,
    "Links": links
}

for container in containers:
    title = container.find_element(by="xpath", value='./div/h3/a').text.encode('ascii', 'ignore').decode()
    description = container.find_element(by="xpath", value='./div/h3/a/span').text.encode('ascii', 'ignore').decode()

    link = container.find_element(by="xpath", value='./div/h3/a').get_attribute("href")
    titles.append(title)
    descriptions.append(description)
    links.append(link)

now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')

df = pd.DataFrame(output)
filename = f'news_{date_str}.csv'
final_path = os.path.join(script_path, filename)

df.to_csv(filename, index=False)

driver.quit()
