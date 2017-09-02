from __future__ import absolute_import
from celery import shared_task
from .models import Anime
from genres.models import Genre
from categories.models import Categorie
from reviews.models import Review
from episodes.models import Episode
from characters.models import Character
import requests
import json

max_id = 13589
range1 = lambda start, end: range(start, end+1)

@shared_task
def get_animes():
	for id in range1(200, 205):
		url = "https://kitsu.io/api/edge/anime/{0}".format(id)
		response = requests.get(url)
		anime_data = response.json()['data']

		if anime_data:
			if not Anime.objects.filter(original_id=anime_data['id']).exists():
				anime = Anime()
				anime.original_id = anime_data['id']

				if 'attributes' in anime_data:
					anime.slug = anime_data['attributes']['slug']
					anime.synopsis = anime_data['attributes']['synopsis']

					if 'titles' in anime_data['attributes']:
						anime.english_title = anime_data['attributes']['titles']['en']
						anime.original_title = anime_data['attributes']['titles']['en_jp']

					anime.canonical_title = anime_data['attributes']['canonicalTitle']
					anime.start_date = anime_data['attributes']['startDate']
					anime.end_date = anime_data['attributes']['endDate']
					anime.age_rating = anime_data['attributes']['ageRating']
					anime.age_rating_guide = anime_data['attributes']['ageRatingGuide']
					anime.subtype = anime_data['attributes']['subtype']
					anime.status = anime_data['attributes']['status']

					if anime_data['attributes']['posterImage'] and 'medium' in anime_data['attributes'].get('posterImage', {}):
						anime.poster_image_link = anime_data['attributes']['posterImage']['medium']
					if anime_data['attributes']['coverImage'] and 'large' in anime_data['attributes'].get('coverImage', {}):
						anime.cover_image_link = anime_data['attributes']['coverImage']['large']

					anime.episode_count = anime_data['attributes']['episodeCount']
					anime.episode_length = anime_data['attributes']['episodeLength']
					anime.youtube_video_id = anime_data['attributes']['youtubeVideoId']
					anime.show_type = anime_data['attributes']['showType']
					anime.nsfw = anime_data['attributes']['nsfw']
					anime.save()
					print("Getted anime: {}".format(str(anime)))

				if 'genres' in anime_data.get('relationships', {}):
					if 'related' in anime_data['relationships']['genres'].get('links', {}) and \
						anime_data['relationships']['genres']['links']['related']:
						get_genres(anime_data['relationships']['genres']['links']['related'], anime)

				if 'categories' in anime_data.get('relationships', {}):
					if 'related' in anime_data['relationships']['categories'].get('links', {}) and \
						anime_data['relationships']['categories']['links']['related']:
						get_categories(anime_data['relationships']['categories']['links']['related'], anime)

				if 'reviews' in anime_data.get('relationships', {}):
					if 'related' in anime_data['relationships']['reviews'].get('links', {}) and \
						anime_data['relationships']['reviews']['links']['related']:
						get_reviews(anime_data['relationships']['reviews']['links']['related'], anime)

				if 'episodes' in anime_data.get('relationships', {}):
					if 'related' in anime_data['relationships']['episodes'].get('links', {}) and \
						anime_data['relationships']['episodes']['links']['related']:
						get_episodes(anime_data['relationships']['episodes']['links']['related'], anime)

				if 'animeCharacters' in anime_data.get('relationships', {}):
					if 'related' in anime_data['relationships']['animeCharacters'].get('links', {}) and \
						anime_data['relationships']['animeCharacters']['links']['related']:
						get_anim_characters(anime_data['relationships']['animeCharacters']['links']['related'], anime)



def get_genres(url, anime):
	response_genres = requests.get(url)
	genre_values = response_genres.json()
	
	if 'data' in genre_values:
		for data in genre_values['data']:
			genre = Genre.objects.filter(original_id=data['id']).first()

			if not genre:
				genre = Genre()
				genre.original_id = data['id']
				
				if 'attributes' in data:
					genre.name = data['attributes']['name']
					genre.slug = data['attributes']['slug']
					genre.description = data['attributes']['description']
					genre.save()
					print("Getted genre: {}".format(str(genre)))
			
			if not anime.genres.filter(id=genre.id).exists():
				anime.genres.add(genre)
				print("Added genre {} to anime {}".format(str(genre), str(anime)))

	if 'next' in genre_values['links']:
		get_genres(genre_values['links']['next'], anime)


def get_categories(url, anime):
	response_categories = requests.get(url)
	categorie_values = response_categories.json()

	if 'data' in categorie_values:
		for data in categorie_values['data']:
			categorie = Categorie.objects.filter(original_id=data['id']).first()

			if not categorie:
				categorie = Categorie()
				categorie.original_id = data['id']
					
				if 'attributes' in data:
					categorie.title = data['attributes']['title']
					categorie.slug = data['attributes']['slug']
					categorie.description = data['attributes']['description']
					categorie.nsfw = data['attributes']['nsfw']
					categorie.save()
					print("Getted categorie: {}".format(str(categorie)))

			if not anime.categories.filter(id=categorie.id).exists():
				anime.categories.add(categorie)
				print("Added categorie {} to anime {}".format(str(categorie), str(anime)))

	if 'next' in categorie_values['links']:
		get_categories(categorie_values['links']['next'], anime)


def get_reviews(url, anime):
	response_reviews = requests.get(url)
	review_values = response_reviews.json()

	if 'data' in review_values:
		for data in review_values['data']:
			review = Review.objects.filter(original_id=data['id'])

			if not review:
				review = Review()
				review.original_id = data['id']

				if 'attributes' in data:
					review.content = data['attributes']['content']
					review.content_formatted = data['attributes']['contentFormatted']
					review.likes_count = data['attributes']['likesCount']
					review.rating = data['attributes']['rating']
					review.source = data['attributes']['source']
					review.anime = anime
					review.spoiler = data['attributes']['spoiler']
					review.save()
					print("Added review '{}' to anime {}".format(str(review), str(anime)))

	if 'next' in review_values['links']:
		get_reviews(review_values['links']['next'], anime)


def get_episodes(url, anime):
	response_episodes = requests.get(url)
	episode_values = response_episodes.json()

	if 'data' in episode_values:
		for data in episode_values['data']:
			episode = Episode.objects.filter(original_id=data['id']).first()

			if not episode:
				episode = Episode()
				episode.original_id = data['id']

				if 'attributes' in data:
					if 'en_jp' in data['attributes']['titles']:
						episode.original_title = data['attributes']['titles']['en_jp']
					if 'en' in data['attributes']['titles']:
						episode.english_title = data['attributes']['titles']['en']

					episode.anime = anime
					episode.canonical_title = data['attributes']['canonicalTitle']
					episode.season_number = data['attributes']['seasonNumber']
					episode.number = data['attributes']['number']
					episode.synopsis = data['attributes']['synopsis']

					if data['attributes']['length']:
						episode.length = data['attributes']['length']

					episode.save()
					print("Added episode '{}' to anime {}".format(str(episode), str(anime)))

	if 'next' in episode_values['links']:
		get_episodes(episode_values['links']['next'], anime)

def get_anim_characters(url, anime):
	response_anim_charac = requests.get(url)
	anim_charac_values = response_anim_charac.json()
	
	if 'data' in anim_charac_values:
		for anim_charac_data in anim_charac_values['data']:
			if 'character' in anim_charac_data.get('relationships', {}):
				if 'related' in anim_charac_data['relationships']['character'].get('links', {}) and \
					anim_charac_data['relationships']['character']['links']['related']:
					get_characters(anim_charac_data['relationships']['character']['links']['related'], anime)

	if 'next' in anim_charac_values['links']:
		get_anim_characters(anim_charac_values['links']['next'], anime)


def get_characters(url, anime):
	response_characters = requests.get(url)
	result = response_characters.json()
	
	if 'data' in result:
		data = result['data']
		character = Character.objects.filter(original_id=data['id'])

		if not character:
			character = Character()
			character.original_id = data['id']

			if 'attributes' in data:
				character.anime = anime
				character.slug = data['attributes']['slug']
				character.name = data['attributes']['name']
				character.mal_id = data['attributes']['malId']
				character.description = data['attributes']['description']

				if data['attributes']['image'] and'original' in data['attributes']['image']:
					character.image_url = data['attributes']['image']['original']

				character.save()
				print("Added character '{}' to anime {}".format(str(character), str(anime)))