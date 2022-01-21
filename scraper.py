from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import  xlsxwriter
import json
import  instaloader
import re
from time import sleep
from getpass import getpass

def login(driver):
    username = input("enter username: ")  # <username here>
    password = input("enter password: ")  # <password here>

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(3)

    # Login
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    submit = driver.find_element_by_tag_name('form')
    submit.submit()
    driver.implicitly_wait(5)

    # Wait for the user dashboard page to load
    # WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "See All")))
# choose hashtag


# browser = webdriver.Chrome('c:/webdrivers/chromedriver')
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="c:/webdrivers/chromedriver",chrome_options=chrome_options)
login(driver)
sleep(15)

hashtag= input("enter hashtag:")
driver.get('https://www.instagram.com/explore/tags/'+hashtag)
driver.implicitly_wait(3)
links=[]
for i in range(3):
    Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = driver.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    page_json = script.string.split(' = ', 1)[1].rstrip(';')
    data = json.loads(page_json)
    for link in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
        links.append('https://www.instagram.com'+'/p/'+link['node']['shortcode']+'/')

print(len(links))
soup=bs(source,'html.parser')
count=0
# create File
print('Starting scraping.........')
# A xls file will be created according to the name of the hashtag
dataWorkbook=xlsxwriter.Workbook('{}_data.xls'.format(hashtag))
mysheet=dataWorkbook.add_worksheet()
userArray=[]
followersArray=[]
followingArray=[]
emailArray=[]
fullNameArray=[]

L = instaloader.Instaloader()
for link in links:
    driver.get(link)
    Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # links = []
    source = driver.page_source
    data = bs(source, 'html.parser')
    body = data.find('body')
    newlink=body.find('a')
    user=newlink['href']
    # print(user)
    username = user[1:-1]


    # try:


    if username is not None:
        if username not in userArray:
            userArray.append(username)
            try:
                profile = instaloader.Profile.from_username(L.context, username)
            except instaloader.exceptions.ProfileNotExistsException:
                print('faulty')
                userArray.remove(username)

                continue

            print('scraping 😁  {}'.format(username))

            bio=profile.biography
                # print(profile.username)
            followees=profile.followees
            followingArray.append(followees)
                # print(profile.followees)
                # print(profile.followers)
            followers=profile.followers

            followersArray.append(followers)
                # print(profile.full_name)
            fullName=profile.full_name
            fullNameArray.append(fullName)
            email=re.findall('[\w\.-]+@[gmail|hotmail|yahoo]+.com', bio)
            # if len(email)==0:
            #     email='Not Present'
            # if email is None:
            #     email='N'
            if email==[]:
                email='None'

            emailArray.append(email[0])


    # except instaloader.ProfileNotExistsException:
    #     print('profile not found,moving to the next')
    # else:









headers=['USERNAME','EMAIL','FOLLOWERS','FOLLOWING','FULL NAME']
bold=dataWorkbook.add_format({'bold':True})
x=0
for head in headers:
    mysheet.write(0,x,head,bold)
    x+=1

for i in range(1,len(userArray)+1):
    mysheet.write(i,0,userArray[i-1])
    mysheet.write(i,1,emailArray[i-1])
    mysheet.write(i,2,followersArray[i-1])
    mysheet.write(i,3,followingArray[i-1])
    mysheet.write(i,4,fullNameArray[i-1])

print('successfully extracted data')
dataWorkbook.close()
