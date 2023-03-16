import requests
import time
import datetime
# global variables
api_key = '5880111a-6c30-41c3-9b5c-dc2e28e87a59'
bot_token = '5444728134:AAFlM4xJe3PM9TPFWJasSa7PGI4l4Udwt3g'
chat_id = '-1001817908220'
threshold = 30
time_interval =  5 * 60 # in seconds
def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=SOL'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    
    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()
# extract the bitcoin price from the json data
    btc_price = response_json['data']['SOL']
    print(btc_price['quote']['USD']['price'])
    return btc_price['quote']['USD']['price']
# fn to send_message through telegram
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
# send the msg
    requests.get(url)
# main fn
def main():
    price_list = []
    now = datetime.datetime.now()
    start_time = datetime.time(8, 0)
    end_time = datetime.time(23, 59)
# infinite loop
    while True:
        print(now.time(), start_time, end_time)
        if start_time <= now.time() <= end_time:
            price = get_btc_price()
            price_list.append(price)
    # if the price falls below threshold, send an immediate msg
            if price < threshold:
                send_message(chat_id=chat_id, msg=f'SOL Price Drop Alert: {price}')
    # send last 6 btc price
            if len(price_list) >= 6:
                send_message(chat_id=chat_id, msg=price_list)
                # empty the price_list
                price_list = []
    # fetch the price for every dash minutes
            time.sleep(time_interval)
# fancy way to activate the main() function
if __name__ == '__main__':
    main()