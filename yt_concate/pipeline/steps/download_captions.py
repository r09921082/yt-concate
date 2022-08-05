import concurrent.futures
import requests
import time
import pprint
from yt_concate.pipeline.steps.step import Step, StepException
from pytube import YouTube


class DownloadCaptions(Step):
    # def process(self, data, inputs, utils):
    # start = time.time()
    # for yt in data:
    #     print('Downloading caption for', yt.id)  # 做debug用
    #
    #     if utils.caption_file_exists(yt):  # 如果檔案已存在在資料夾，就不用再下載一次
    #         print("Found existing caption file.")
    #         continue
    #
    #     try:
    #         source = YouTube(yt.url)
    #         en_caption = source.captions.get_by_language_code('a.en')
    #         en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    #
    #     except AttributeError:
    #         print("AttributeError when downloading cation for", yt.url)
    #         continue
    #
    #     except FileNotFoundError:
    #         print("FileNotFoundError when downloading cation for", yt.url)
    #
    #     text_file = open(yt.get_caption_filepath(), "w", encoding='utf-8')
    #     text_file.write(en_caption_convert_to_srt)
    #     text_file.close()
    # end = time.time()
    #
    # print(f"It costs {end-start}")
    # print(data)
    # return data

    '''
    Multi-threading
    '''

    def get_caption(self, yt, utils):
        print('Downloading caption for', yt.id)  # 做debug用

        if utils.caption_file_exists(yt):  # 如果檔案已存在在資料夾，就不用再下載一次
            print("Found existing caption file.")
        try:
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            text_file = open(yt.get_caption_filepath(), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        except AttributeError:
            print("AttributeError when downloading cation for", yt.url)
        except FileNotFoundError:
            print("FileNotFoundError when downloading cation for", yt.url)

        return yt

    def process(self, data, inputs, utils):
        multi_thread_data = []
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            yt = {executor.submit(self.get_caption, yt, utils): yt for yt in data}
            for future in concurrent.futures.as_completed(yt):  # 將multi_thread結果合併
                try:
                    data = future.result()
                    multi_thread_data.append(data)
                except UnboundLocalError:
                    pass

        end = time.time()
        print(f"It costs {end - start}")
        print(data)
        return multi_thread_data
