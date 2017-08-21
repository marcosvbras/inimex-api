import requests
import json

max_id = 13589
range1 = lambda start, end: range(start, end+1)

def get_animes():
	for id in range1(200, 200):
		url = "https://kitsu.io/api/edge/anime/{0}".format(id)
		response = requests.get(url.format(max_id))
		anime_data = response.json()['data']

		if anime_data:
			print("Id: {}".format(anime_data['id']))

			if 'attributes' in anime_data:
				print("Slug: {}".format(anime_data['attributes']['slug']))
				print("Synopsis: {}".format(anime_data['attributes']['synopsis']))

				if 'titles' in anime_data['attributes']:
					print("Title: {}".format(anime_data['attributes']['titles']['en']))
					print("Title (JP): {}".format(anime_data['attributes']['titles']['en_jp']))

				print("Canonical Title: {}".format(anime_data['attributes']['canonicalTitle']))
				print("StartDate: {}".format(anime_data['attributes']['startDate']))
				print("EndDate: {}".format(anime_data['attributes']['endDate']))
				print("Age Rating: {}".format(anime_data['attributes']['ageRating']))
				print("Age Rating Guide: {}".format(anime_data['attributes']['ageRatingGuide']))
				print("Subtype: {}".format(anime_data['attributes']['subtype']))
				print("Status: {}".format(anime_data['attributes']['status']))

				if 'posterImage' in anime_data['attributes']:
					print("Poster Image: {}".format(anime_data['attributes']['posterImage']['medium']))
				if 'coverImage' in anime_data['attributes']:
					print("Cover Image: {}".format(anime_data['attributes']['coverImage']['large']))

				print("Episode Count: {}".format(anime_data['attributes']['episodeCount']))
				print("Episode Length: {}".format(anime_data['attributes']['episodeLength']))
				print("YoutubeVideoId: {}".format(anime_data['attributes']['youtubeVideoId']))
				print("Show Type: {}".format(anime_data['attributes']['showType']))
				print("NSFW: {}".format(anime_data['attributes']['nsfw']))

			# if 'genres' in anime_data.get('relationships', {}):
			# 	if 'related' in anime_data['relationships']['genres'].get('links', {}) and \
			# 		anime_data['relationships']['genres']['links']['related']:
			# 		get_genres(anime_data['relationships']['genres']['links']['related'])

			# if 'categories' in anime_data.get('relationships', {}):
			# 	if 'related' in anime_data['relationships']['categories'].get('links', {}) and \
			# 		anime_data['relationships']['categories']['links']['related']:
			# 		get_categories(anime_data['relationships']['categories']['links']['related'])

			# if 'reviews' in anime_data.get('relationships', {}):
			# 	if 'related' in anime_data['relationships']['reviews'].get('links', {}) and \
			# 		anime_data['relationships']['reviews']['links']['related']:
			# 		get_reviews(anime_data['relationships']['reviews']['links']['related'])

			# if 'episodes' in anime_data.get('relationships', {}):
			# 	if 'related' in anime_data['relationships']['episodes'].get('links', {}) and \
			# 		anime_data['relationships']['episodes']['links']['related']:
			# 		get_episodes(anime_data['relationships']['episodes']['links']['related'])

			if 'animeCharacters' in anime_data.get('relationships', {}):
				if 'related' in anime_data['relationships']['animeCharacters'].get('links', {}) and \
					anime_data['relationships']['animeCharacters']['links']['related']:
					get_anim_characters(anime_data['relationships']['animeCharacters']['links']['related'])



def get_genres(url):
	response_genres = requests.get(url)
	genre_values = response_genres.json()

	if 'data' in genre_values:
		for data in genre_values['data']:
			print("Genre Id: {}".format(data['id']))	
			if 'attributes' in data:
				print("Genre Name: {}".format(data['attributes']['name']))
				print("Genre Slug: {}".format(data['attributes']['slug']))
				print("Genre Description: {}".format(data['attributes']['description']))

	if 'next' in genre_values['links']:
		get_genres(genre_values['links']['next'])


def get_categories(url):
	response_categories = requests.get(url)
	categorie_values = response_categories.json()

	if 'data' in categorie_values:
		for data in categorie_values['data']:
			print("Categorie Id: {}".format(data['id']))	
			if 'attributes' in data:
				print("Categorie Title: {}".format(data['attributes']['title']))
				print("Categorie Slug: {}".format(data['attributes']['slug']))
				print("Categorie Description: {}".format(data['attributes']['description']))
				print("Categorie NSFW: {}".format(data['attributes']['nsfw']))

	if 'next' in categorie_values['links']:
		get_categories(categorie_values['links']['next'])


def get_reviews(url):
	response_reviews = requests.get(url)
	review_values = response_reviews.json()

	if 'data' in review_values:
		for data in review_values['data']:
			print("Review Id: {}".format(data['id']))	
			if 'attributes' in data:
				print("Review Content: {}".format(data['attributes']['content']))
				print("Review Content Formatted: {}".format(data['attributes']['contentFormatted']))
				print("Review Likes Count: {}".format(data['attributes']['likesCount']))
				print("Review rating: {}".format(data['attributes']['rating']))
				print("Review source: {}".format(data['attributes']['source']))
				print("Review spoiler: {}".format(data['attributes']['spoiler']))

	if 'next' in review_values['links']:
		get_reviews(review_values['links']['next'])


def get_episodes(url):
	response_episodes = requests.get(url)
	episode_values = response_episodes.json()

	if 'data' in episode_values:
		for data in episode_values['data']:
			print("Episode Id: {}".format(data['id']))	
			if 'attributes' in data:
				if 'en_jp' in data['attributes']['titles']:
					print("Episode Original Title: {}".format(data['attributes']['titles']['en_jp']))
				if 'en' in data['attributes']['titles']:
					print("Episode English Title: {}".format(data['attributes']['titles']['en']))

				print("Episode Canonical Title: {}".format(data['attributes']['canonicalTitle']))
				print("Episode Season Number: {}".format(data['attributes']['seasonNumber']))
				print("Episode number: {}".format(data['attributes']['number']))
				print("Episode synopsis: {}".format(data['attributes']['synopsis']))
				print("Episode Length: {}".format(data['attributes']['length']))

	if 'next' in episode_values['links']:
		get_episodes(episode_values['links']['next'])

def get_anim_characters(url):
	response_anim_charac = requests.get(url)
	anim_charac_values = response_anim_charac.json()
	
	if 'data' in anim_charac_values:
		for anim_charac_data in anim_charac_values['data']:
			if 'character' in anim_charac_data.get('relationships', {}):
				if 'related' in anim_charac_data['relationships']['character'].get('links', {}) and \
					anim_charac_data['relationships']['character']['links']['related']:
					get_characters(anim_charac_data['relationships']['character']['links']['related'])

	if 'next' in anim_charac_values['links']:
		get_anim_characters(anim_charac_values['links']['next'])


def get_characters(url):
	response_characters = requests.get(url)
	result = response_characters.json()
	
	if 'data' in result:
		data = result['data']
		if 'attributes' in data:
			print("Character Slug: {}".format(data['attributes']['slug']))
			print("Character Name: {}".format(data['attributes']['name']))
			print("Character malId: {}".format(data['attributes']['malId']))
			print("Character description: {}".format(data['attributes']['description']))

			if 'original' in data['attributes']['image']:
				print("Character Image Url: {}".format(data['attributes']['image']['original']))


if __name__ == '__main__':
	get_animes()




