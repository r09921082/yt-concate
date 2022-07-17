from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownladVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # 淘汰掉list中重複性的元素
        print('Videos to download=', len(yt_set))
        for yt in yt_set:  # data 為 found 物件
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'Found existing video file for {url}, skipping.')
                continue

            print('Downloading!', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data