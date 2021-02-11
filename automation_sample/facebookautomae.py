import random
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path='c:/webdrivers/chromedriver')

email_phone = input("Enter your email or phone:  ")
pwd = input("Enter your password: ")

driver.get('https://www.facebook.com/login')

driver.find_element_by_id("email").click()
driver.find_element_by_id("email").send_keys(email_phone)
driver.implicitly_wait(1)
driver.find_element_by_id("pass").click()
driver.find_element_by_id("pass").send_keys(pwd)
driver.implicitly_wait(1)
driver.find_element_by_id("loginbutton").click()
driver.implicitly_wait(10)

inp = input("What do you want to do next?")

def comment_on_post(com):
    try:
        home = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a")
        home.click()
        driver.implicitly_wait(3)
        profile = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/a")
        profile.click()
        driver.implicitly_wait(3)
        cururl = driver.current_url
        driver.get(cururl+"&sk=friends")
        driver.implicitly_wait(4)
        n = random.randint(1,6)
        driver.implicitly_wait(10)
        f = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[%s]/div[1]/a"%n)
        driver.implicitly_wait(1)
        print(f.is_displayed())
        f.click()

        driver.implicitly_wait(3)
        driver.implicitly_wait(2)


        driver.implicitly_wait(5)
        cm  = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div")

        driver.implicitly_wait(1)
        cm.click()
        driver.implicitly_wait(5)
        cm.send_keys(com,Keys.ENTER)
        driver.implicitly_wait(3)
        return 0
    except NoSuchElementException:
        comment_on_post(com)

def updateStatus(st):
    try:
        home = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a")
        driver.implicitly_wait(6)
        home.click()
        driver.implicitly_wait(3)
        g =driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]")
        driver.implicitly_wait(4)
        g.click()
        driver.implicitly_wait(3)
        status = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div")
        print(status.is_displayed())
        status.click()
        driver.implicitly_wait(3)
        # textbox = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div").click()

        driver.implicitly_wait(4)
        status.send_keys(st)
        driver.implicitly_wait(3)
        button = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div").click()
        return 0
    except NoSuchElementException:
        updateStatus(st)

if inp == "comment":
    com = input("your comment")
    comment_on_post(com)
elif inp == "update":
    st = input("your status")
    updateStatus(st)