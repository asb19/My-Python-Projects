from selenium import webdriver
from bs4 import BeautifulSoup as bs
import  xlsxwriter
import json
import  instaloader
import re

# choose hashtag
hashtag='food'
# browser = webdriver.Chrome('c:/webdrivers/chromedriver')
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="c:/webdrivers/chromedriver",chrome_options=chrome_options)
driver.get('https://www.instagram.com/explore/tags/'+hashtag)
links=[]
for i in range(3):
    Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = driver.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
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
