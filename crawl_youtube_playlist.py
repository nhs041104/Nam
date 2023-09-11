import pandas as pd
from googleapiclient.discovery import build

# 조회수 단위 설정
def format_view_count(view_count):
    if view_count >= 100000000:
        return f"{view_count // 100000000}억"
    elif view_count >= 10000:
        return f"{view_count // 10000}만"
    else:
        return str(view_count)

# YouTube API 키 설정
API_KEY = input("자신의 Youtube API KEY를 입력하세요: ")

# YouTube API 클라이언트 생성
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 재생목록 코드 입력 받기
playlist_id = input("YouTube 재생목록 코드를 입력하세요: ")

# 재생목록에서 동영상 목록 가져오기
videos = []
next_page_token = None

while True:
    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,  # 변경 가능
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

    # 영상 조회수 가져오기
    video_statistics = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()

    view_count = int(video_statistics['items'][0]['statistics']['viewCount'])

    formatted_view_count = format_view_count(view_count)

    video_data.append([title, video_url, thumbnail_url, formatted_view_count])

# 데이터프레임 생성
df = pd.DataFrame(video_data, columns=['Title', 'Video URL', 'Thumbnail URL', 'View Count'])

# 데이터프레임 출력
df