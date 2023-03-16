# ----- Imports and Librarys ----- #

import requests
import re
import time
import queue
import multiprocessing
from threading import Thread
import sys

# ----- Selenium Library's ----- #

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import chromedriver_autoinstaller

# ----- Fix Email Function ----- #

def fix_email(email):

    endings = ['.com', '.us', '.ca', '.ge', '.uk', '.it'] # For different types of domain endings

    # Loop through endings and fix email 

    for e in endings:
        if e in email and not email.endswith(e):
            return email.split(e)[0] + e

    return email

# ----- Convert String To Number Function ----- #

def cstn(x):

    ''' This function returns stringed numbers into int.
    E.g: 1k == 1000 or 100,000 == 100000
    '''

    total_stars = 0
    num_map = {'K':1000, 'M':1000000, 'B':1000000000}

    if isinstance(x, int):
        total_stars = int(x) 
    elif x.isdigit():
        total_stars = int(x)
    elif ',' in x:
        total_stars = int(x.replace(',',''))
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
    return int(total_stars)



# ----- Scrape Class ----- #


class Scrape:

    def __init__(self,search, link_count=100, view_count=None, sub_count=None):

        self.search = search.replace(' ', '+')
        self.link_count = cstn(link_count)
        self.view_count = cstn(view_count) if view_count else view_count
        self.sub_count = cstn(sub_count)if sub_count else sub_count
        self.url = 'https://www.youtube.com/results?search_query=' + search + '&sp=CAI%253D' # Sets it to most recent videos

        # Declarations

        self.filtered_links = queue.Queue()
        self.links = set()
        self.timeout = False
        self.links_gathered = False
        self.position = 0
        self.manager = multiprocessing.Manager()
        self.return_dict = self.manager.dict()
        self.channels = [] # Used to store viewed channels and their subs

        # Driver Setup and Options

        # chromedriver_autoinstaller.install(cwd=True) # Get latest version of chromedriver // Cwd=True -> Saves driver in directory

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument("--log-level=OFF")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("--headless") # Sets headless mode for no window popup

        self.__FetchVideos() # Fetch URLs

    def __subFinder(self, url):

        ''' This function finds subscriber count of url'''

        r = requests.get(url).text # Get the page

        # Find subscriber count

        try:
            x = re.findall(r'.{1,8} subscribers', r)[-1]
            f = re.findall(r'\d+', x)[0]
            subs = (str(f) + x.split(f)[-1]).strip(' subscribers')
        except:
            subs = '1' # Return 1 if subscriber count is not found or hidden

        self.channels.append({"Channel": url, "Subs": subs}) # Saves channel and sub count
            
        return subs

    def __FetchVideos(self):

        '''This function scrapes self.url for urls with
        views and subs conditions being met.'''

        # Variable Declaration

        s = time.time()
        views = None
        subs = None

        # Open chrome driver

        with webdriver.Chrome(options=self.options, executable_path="/usr/local/bin/chromedriver") as driver:

            driver.get(self.url) # Gets the url

            timer = Thread(target=self.__timeoutFunc) # Starts a timeout if links take too long
            timer.start()

            # ----- Render Page For Links ----- #

            try:

                while len(self.links) <= self.link_count and self.timeout == False: # Loops until all links are found or timeout is set to True

                    for video in WebDriverWait(driver, 0).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.text-wrapper.style-scope.ytd-video-renderer"))):

                        url = video.find_element_by_css_selector('a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title').get_attribute('href')

                        # Only check for sub and view count if function calls it -> saves time

                        if self.view_count: 
                            views = cstn(video.find_element_by_css_selector('span.style-scope.ytd-video-meta-block').text.split(' views')[0])

                        if self.sub_count: 

                            channel = video.find_element_by_css_selector('a.yt-simple-endpoint.style-scope.yt-formatted-string').get_attribute('href')
                            channels = [i["Channel"] for i in self.channels]

                            if channel not in channels: 
                                subs = cstn(self.__subFinder(channel)) # If channel hasn't been seen, get it's sub count
                            else: 
                                # If channel stored, return its sub count -> saves time making this program 3x faster
                                for i in self.channels:
                                    if i['Channel'] == channel:
                                        subs = cstn(i["Subs"])

                        if subs == None: subs = 0
                        if views == None: views = 0

                        if(
                            (self.view_count == None and self.sub_count == None)
                            or (self.view_count == None and self.sub_count >= subs)
                            or (self.view_count == None and self.sub_count >= subs)
                            or (self.sub_count == None and self.view_count >= views)
                            or (elf.sub_count >= subs and views <= self.view_count) 
                        ):
                            self.links.add(url)

                    self.position += 10000
                    driver.execute_script("window.scrollTo(0, {})".format(str(self.position))) # render more links

            except Exception as e:

                # Typically called when youtube returns captcha

                driver.close()
                self.links_gathered = True
                sys.exit()

        # Put links into queue

        for link in self.links:
            self.filtered_links.put(link)

        self.links_gathered = True
    
    # This function is to ensure getting links don't take too long or forever 

    def __timeoutFunc(self):

        count = 60 # one minute

        if self.sub_count: count += 60 # Add another 60 seconds if sub count is needed (fetching sub count takes longer)

        before = time.time()
        timeout_time = count*(self.link_count/50) # Set it to 50 links per minute or two if sub count


        while not self.links_gathered:

            time.sleep(1) # Don't eat up cpu

            if time.time()-before >= timeout_time:
                self.timeout = True # Tell url fetcher to stop
                return



# ----- Worker ----- #

def worker(procnum, url, return_dict, sema):

    '''This worker functions goes through all the pages
    and extracts the emails'''

    sema.acquire() # Lock proccess

    page = requests.get(url).text # Get the url

    emails = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', page) # Finds email

    if emails:
        email = fix_email([i for i in emails if not i.endswith('...')][0]) # Checks for valid email and fixes it if any error
        return_dict[procnum] = email

    sema.release() # Allow more processes by releasing lock

    return

# ----- Handler ----- #

def run(search, link_count=100, view_count=None, sub_count=None, cpus=None):

    ''' This function calls the Scrape class to fetch videos then uses 
    multiprocessing to extract the emails from given url. Returns {'Time': time, 'Emails': emails}'''

    all_processes = [] # Store started processes

    total_time = time.time()

    if cpus.isdigit():
        cpu = int(cpus) # Return cpu count to use
    else:
        cpu = multiprocessing.cpu_count() # Use all cpus
        if cpus.lower() == 'half': cpu /= 2 # Use half of your cpu usage
        cpu = int(cpu)


    print("cpu", cpu) 

    sema = multiprocessing.Semaphore(cpu) # Create process lock

    scrape = Scrape(search=search, link_count=link_count, view_count=view_count, sub_count=sub_count) # Creates scrape object

    for i in range(scrape.filtered_links.qsize()):
        p = multiprocessing.Process(target=worker, args=(i, scrape.filtered_links.get(), scrape.return_dict, sema))
        all_processes.append(p)
        p.start()

    for p in all_processes:
        p.join()

    finished_time= time.time()-total_time

    emails = set(scrape.return_dict.values()) # Remove duplicate emails

    to_return = {"Time": finished_time, "Emails": emails} # Make returnable object

    return to_return # Return {"Time": time, "Emails": set(emails...)}

# ----- Fork ----- #

if __name__ == '__main__':

    x = run(search='minecraft', link_count=20, cpus='all') # For tests
    print(x)
