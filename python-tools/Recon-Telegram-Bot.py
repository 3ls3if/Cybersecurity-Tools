#!/usr/bin/python3

import requests
import json

api_key="<your api key>"
URL = "https://api.telegram.org/bot{0}/".format(api_key)

def get_url(url):
	res = requests.get(url)
	content = res.content.decode("utf-8")
	return content

def getUpdates(offset=None):
	url = URL + "getUpdates?timeout=100" 
	if offset:
		url = url + "&offset={}".format(offset+1)
	updates= get_url(url)
	upd = json.loads(updates)
	return upd

def main():
	update_id = None
	while True:
		data = getUpdates(offset=update_id)
		results = data['result']
		if results:
			for i in data['result']:
				update_id = i['update_id']
				chatid=i['message']['from']['id']
				usr=i['message']['from']['username']
				message = "Hello,"+usr
				url = URL+ "sendMessage?chat_id={0}&text={1}".format(chatid,message)
				get_url(url)
				print("message sent!")

main()
