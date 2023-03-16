import json
import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs


# init session
session = HTMLSession()

def get_video_info(url):
    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result = {}

    response.html.render(sleep=1, timeout=60)

    # Additional video and channel information (with help from: https://stackoverflow.com/a/68262735)
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']
    # number of likes

        # channel details
    channel_tag = soup.find("meta", itemprop="channelId")['content']
    # channel name
    channel_name = soup.find("span", itemprop="author").next.next['content']
    # channel URL
    # channel_url = soup.find("span", itemprop="author").next['href']
    channel_url = f"https://www.youtube.com/{channel_tag}"
    # number of subscribers as str
    channel_subscribers = videoSecondaryInfoRenderer['owner']['videoOwnerRenderer']['subscriberCountText']['accessibility']['accessibilityData']['label']
    # channel details (old way)
    # channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")
    # # channel name (old way)
    # channel_name = channel_tag.text
    # # channel URL (old way)
    # channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str (old way)
    # channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="YouTube Video Data Extractor")
    # parser.add_argument("url", help="https://www.youtube.com/watch?v=SqH74p8cykw")
    # args = parser.parse_args()
    # url = args.url
    # get the data
    data = get_video_info("https://www.youtube.com/watch?v=DTFzmkO96Wo")
    # print in nice format
    # print(f"Title: {data['title']}")
    # print(f"Views: {data['views']}")
    # print(f"Published at: {data['date_published']}")
    # print(f"Video Duration: {data['duration']}")
    # print(f"Video tags: {data['tags']}")
    # print(f"Likes: {data['likes']}")
    # print(f"Dislikes: {data['dislikes']}")
    # print(f"\nDescription: {data['description']}\n")
    print(f"\nChannel Name: {data['channel']['name']}")
    print(f"Channel URL: {data['channel']['url']}")
    print(f"Channel Subscribers: {data['channel']['subscribers']}")