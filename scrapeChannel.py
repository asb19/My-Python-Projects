from re import sub
from selenium import webdriver
import json, time
from selenium.webdriver.common.by import By
import requests
import re
import time


def get_video_results():
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.get('https://www.youtube.com/results?search_query=SSC hindi')

    youtube_data = []

    # scrolling to the end of the page
    # https://stackoverflow.com/a/57076690/15164646
    i=0
    while True:
        if i==10:
            break
        # end_result = "No more results" string at the bottom of the page
        # this will be used to break out of the while loop
        end_result = driver.find_element(By.CSS_SELECTOR,'#message').is_displayed()
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        # time.sleep(1) # could be removed
        print(end_result)
        i+=1

        # once element is located, break out of the loop
        if end_result == True:
            break

    print('Extracting results. It might take a while...')

    for result in driver.find_elements(By.CSS_SELECTOR,'.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element(By.CSS_SELECTOR,'.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element(By.CSS_SELECTOR,'.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element(By.CSS_SELECTOR,'.long-byline').text
        channel_link = result.find_element(By.CSS_SELECTOR,'#text > a').get_attribute('href')
        print(channel_link)

        subs = __subFinder(channel_link)
        views = result.find_element(By.CSS_SELECTOR,'.style-scope ytd-video-meta-block').text.split('\n')[0]
        # subs = driver.find_element(By.CSS_SELECTOR,'#subscribers').text

        try:
            time_published = result.find_element(By.CSS_SELECTOR,'.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element(By.CSS_SELECTOR,'.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element(By.CSS_SELECTOR,'#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element(By.CSS_SELECTOR,'#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None
        print(verified_badge)

        youtube_data.append({
            'title': title,
            'link': link,
            'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            'subs': subs,
            'views': views,
            'time_published': time_published,
            'snippet': snippet,
            'verified_badge': verified_badge,
            'extensions': extensions,
        })

    print(json.dumps(youtube_data, indent=2, ensure_ascii=False))

    driver.quit()



def __subFinder(url):

        ''' This function finds subscriber count of url'''

        r = requests.get(url).text # Get the page

        # Find subscriber count

        try:
            x = re.findall(r'.{1,8} subscribers', r)[-1]
            f = re.findall(r'\d+', x)[0]
            subs = (str(f) + x.split(f)[-1]).strip(' subscribers')
        except:
            subs = '1' # Return 1 if subscriber count is not found or hidden

        # self.channels.append({"Channel": url, "Subs": subs}) # Saves channel and sub count
            
        return subs

get_video_results()
