from .step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips

class EditVideo(Step):
    def process(self, data, inputs, utils):  # 傳入的 data 為 Found 物件
        clips = []
        for found in data:
            start_time, end_time = self.parse_caption_time(found.time)
            video_file_path = found.yt.video_filepath
            if "b9dWgUlMb9o.mp4" in video_file_path:
                continue

            video = VideoFileClip(video_file_path).subclip(start_time, end_time)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

            final_clip = concatenate_videoclips(clips)
            output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
            final_clip.write_videofile(output_filepath)


    def parse_caption_time(self, caption_time):
        start_time, end_time = caption_time.split(" --> ")
        return self.parse_time_str(start_time), self.parse_time_str(end_time)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000
