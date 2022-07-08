from yt_concate.pipeline.steps.step import Step, StepException
from pytube import YouTube
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('Downloading caption for', url)  # 做debug用

            if utils.caption_file_exists(url):  # 如果檔案已存在在資料夾，就不用再下載一次
                print("Found existing caption file.")
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            except AttributeError:
                print("AttributeError when downloading cation for", url)
                continue
            except FileNotFoundError:
                print("FileNotFoundError when downloading cation for", url)

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
