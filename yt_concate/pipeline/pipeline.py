from yt_concate.pipeline.steps.step import StepException


# 建立一個自動化工廠
class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None

        # 利用for迴圈逐一跑它
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:  # 抓每個step中的錯誤
                print("Exception happened: ", e)
                break
