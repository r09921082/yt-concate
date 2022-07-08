from abc import ABC  # abstract base class
from abc import abstractmethod


# Base class(Abstract class)
class Step(ABC):

    def __init__(self):
        pass

    @abstractmethod  # decorator, 子類別一定要寫這個method
    # 設計介面
    # inputs 為一個 dict
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass
