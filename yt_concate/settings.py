import os
from dotenv import load_dotenv
load_dotenv()  # 讀取環境變數

API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'D:\yt-concate\yt_concate\downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUTS_DIR = 'D:\yt-concate\yt_concate\outputs'
