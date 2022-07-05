from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

inputs = {
    'channel_id': CHANNEL_ID
}


def main():
    # 將每個class存成一個class list
    steps = [
        GetVideoList(),

        ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
