from .step import Step
from yt_concate.model.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions

            if not captions:  # 跳過沒有字幕的影片
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)  # 使用一個helper class去儲存資料
                    found.append(f)  # found清單中裝found物件

        return found
