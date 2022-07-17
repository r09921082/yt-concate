

class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):  # 簡易顯示此物件資訊
        return f"<Found(yt={str(self.yt)}>"

    def __repr__(self):  # 顯示此物件的細節
        content = ' : '.join([
            'yt=' + str(self.yt),
            'caption=' +str(self.caption),
            'time=' + str(self.time)
        ])
        return '<Found(' + content + ')>'