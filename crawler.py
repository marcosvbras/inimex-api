import requests
import json
import os

max_id = 13589
range1 = lambda start, end: range(start, end+1)

for id in range1(6050, 6150):
	url = "https://kitsu.io/api/edge/anime/{0}".format(id)
	response = requests.get(url.format(max_id))
	anime = response.json()

	try:
		title = anime['data']['attributes']['titles']['en_jp']
		print("[Success] %s" % title)
	except Exception as exception:
		message = "Error to curl anime with ID: {0}".format(id)
		os.system("echo {0} >> anime_download_log.txt".format(message))
		print("[Error] %s " % message)