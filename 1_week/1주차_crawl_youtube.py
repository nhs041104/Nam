import pandas as pd
import requests
from googleapiclient.discovery import build

# YouTube API 키 설정
API_KEY = 'Your API Key'

# YouTube API 클라이언트 생성
youtube = build('youtube', 'v3', developerKey=API_KEY)

# YouTube 인기 음악 재생목록 ID
playlist_id = 'playlist_code'

# 재생목록에서 동영상 목록 가져오기
videos = []
next_page_token = None

while True:
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    videos.extend(playlist_items['items'])
    next_page_token = playlist_items.get('nextPageToken')

    if not next_page_token:
        break

# 데이터 추출
video_data = []
for video in videos:
    video_id = video['snippet']['resourceId']['videoId']
    title = video['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    thumbnail_url = video['snippet']['thumbnails']['default']['url']
    video_data.append([title, video_url, thumbnail_url])

# 데이터프레임 생성, 추출
df = pd.DataFrame(video_data, columns=['Title', 'Video URL', 'Thumbnail URL'])
df
