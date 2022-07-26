from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitialzeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownladVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

inputs = {
    'channel_id': CHANNEL_ID,
    'search_word': 'incredible',
    'limit': 20,

}


def main():
    # 將每個class存成一個class list
    steps = [
        Preflight(),
        GetVideoList(),
        InitialzeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownladVideos(),
        EditVideo(),
        Postflight(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
