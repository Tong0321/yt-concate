import json
import ssl
import urllib.request
import os
from yt_concate.settings import API_KEY
print(API_KEY)
api_key = os.getenv('API_KEY')
def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen('https://google.com')
    print(r.status)
    print(r)


if __name__ == '__main__':
    main()

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyBbP5AV-2jTu9G9vX3kzcdT6YlCLnkvNug'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
