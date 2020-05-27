#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:47:40 2020

@author: emirimorita
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

USER = "emorita@princeton.edu"
PASS = "tajpEz-tydref-2kimta"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.wantedly.com/user/sign_in')

username_box = driver.find_element_by_name("user[email]")
username_box.send_keys(USER)
password_box = driver.find_element_by_name("user[password]")
password_box.send_keys(PASS)
submit_button = driver.find_element_by_name( "commit")
submit_button.submit()

# list of company profile urls
company_urls = []
for i, g in enumerate(driver.find_elements_by_class_name("project-title")):
    #print("------ " + str(i+1) + " ------")
    r = g.find_element_by_tag_name("a")
    company_urls.append(r.get_attribute("href"))

# list of 'p' tag text for each company profile
text_list = []
for i in range(len(company_urls)):
    driver.get(company_urls[i])
    data = driver.find_element_by_class_name('js-descriptions')
    dataList = data.find_elements_by_tag_name('p') 
    temp = ''
    for item in dataList: 
        temp += " " + item.text
    text_list.append(temp)

# export company info to individual text files
for i in range(len(text_list[7:])):
    text_file = open('text' + str(i+7) + '.txt', "w")
    n = text_file.write(text_list[i+7])
    text_file.close()

