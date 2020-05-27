import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


# set de url
url = 'http://www.camargoemartins.com.br'

# get options function
option = Options()

# if you want the webdriver run in background you have do declare it
# option.headless = True
# and then pass this into de driver
# driver = webdriver.Chrome(options=option)

# start de driver
driver = webdriver.Chrome()

# get the url
driver.get(url)

# set a timer in seconds to whait all page load
time.sleep(5)

# now you have to put what you want from website
# example
# //div[@class="container-services"]
get_element = driver.find_element_by_xpath('here you put what you want to get from the website')
# get all html content for what you want
html_content = get_element.get_attribute('outerHTML')

# turn this readable
soup = BeautifulSoup(html_content, 'html-parser')

# get the specific content you want
# example
# table
what_i_want_get = soup.find(name='table')

# get this data and set a limit for it, if you don't want all
# just put the amount you want in .head 
# we use str to transform what we got from html content
data = pd.read_html(str(what_i_want_get))[0].head(2)

# with that data you can get what you want from
# like name, points or whatever have in html
s_data = data[['pass here what you want', 'like name', 'points']]

# organize that into columns
s_data.columns = ['wanted', 'name', 'points']

# now create the object
obj = {}
obj['name of you want here'] = s_data.to_dict('records')

# close the webdriver
driver.quit()

# after close lets create a json object with what we got
js = json.dumps(obj)

# open a file or create
file_open = open('records', 'w')
# write inside that file
file_open.write(js)
# close the file
file_open.close()

# we are done :D