# -*- coding: utf-8 -*-
import os
import datetime

from django.conf import settings

import googleapiclient.discovery
import googleapiclient.errors
from .models import KeyWordsData, VideoData


def get_video_list():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = settings.YOUTUBE_API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    key_words = KeyWordsData.objects.all()

    for key_word in key_words:
        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            type="video",
            relevanceLanguage='ru',
            q=key_word.key_word,
        )
        print('connection youtube')
        response = request.execute()
        for item in response['items']:
            youtube_id = item['id']['videoId']
            video_data = {'title': item['snippet']['title'], 'key_word_id': key_word.id,
                          'url': 'https://www.youtube.com/watch?v={}'.format(youtube_id),
                          'published_at': datetime.datetime.strptime(item['snippet']['publishedAt'],
                                                                     '%Y-%m-%dT%H:%M:%SZ')}
            item_obj, obj_create = VideoData.objects.get_or_create(key_word__id=key_word.id, youtube_id=youtube_id,
                                                                   defaults=video_data)

