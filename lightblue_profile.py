#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:20:45 2020

@author: emirimorita
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

USER = "emorita@princeton.edu"
PASS = "tajpEz-tydref-2kimta"
LIGHTBLUE = "https://www.wantedly.com/projects/251266"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.wantedly.com/user/sign_in')

username_box = driver.find_element_by_name("user[email]")
username_box.send_keys(USER)
password_box = driver.find_element_by_name("user[password]")
password_box.send_keys(PASS)
submit_button = driver.find_element_by_name( "commit")
submit_button.submit()

# list of 'p' tag text for each company profile
driver.get(LIGHTBLUE)
data = driver.find_element_by_class_name('js-descriptions')
dataList = data.find_elements_by_tag_name('p') 
temp = ''
for item in dataList: 
    temp += " " + item.text
text_list_lightblue = temp

print(len(text_list_lightblue))