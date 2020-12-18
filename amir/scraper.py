from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()

def scrape():
    s=requests.session()
    url='https://www.instagram.com/explore/tags/'
    tag='birds'
    url+=tag
    content=s.get(url,verify=False).content
    # print(content)
    soup=BeautifulSoup(content,'html.parser')
    print(soup)
    listings=soup.find_all('div',{'class':'Nnq7C'})
    print(listings[0])
    for i in listings:
        print(i.find_all('a')[0])
    
    return None


scrape()



