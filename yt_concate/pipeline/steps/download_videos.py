import time
import concurrent.futures
from .step import Step
from pytube import YouTube, exceptions
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    # def process(self, data, inputs, utils):
    # yt_set = set([found.yt for found in data])  # 淘汰掉list中重複性的元素
    # print(yt_set)
    # print('Videos to download=', len(yt_set))
    # for yt in yt_set:  # data 為 found 物件
    #     url = yt.url
    #     if utils.video_file_exists(yt):
    #         print(f'Found existing video file for {url}, skipping.')
    #         continue
    #
    #     print('Downloading!', url)
    #     YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=f"{yt.id}.mp4")
    #
    # return data

    def get_video(self, found, utils):
        url = found.yt.url
        if utils.video_file_exists(found.yt):
            print(f'Found existing video file for {url}, skipping.')
        else:
            print('Downloading!', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=f"{found.yt.id}.mp4")

        return found

    def process(self, data, inputs, utils):
        multi_thread_data = []
        start = time.time()
        found_set = set([found for found in data])  # 淘汰掉list中重複性的元素
        print('Videos to download=', len(found_set))
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            found = {executor.submit(self.get_video, found, utils): found for found in found_set}
            for future in concurrent.futures.as_completed(found):
                try:
                    data = future.result()
                    multi_thread_data.append(data)
                except UnboundLocalError:
                    pass

        end = time.time()
        print(f"It costs {end - start}")
        return multi_thread_data
