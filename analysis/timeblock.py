from base.parts_model import PartsModel
import dill
import time

class TimeBlockModel(PartsModel):
    def __init__(self):
        super().__init__()

    def run_parts(self):
        print("agent : ", self.agent)
        print("ENV : ", self.environment)


if __name__ == "__main__":
    timeblock = TimeBlockModel()
    with open("./partsmodel/timeblock.simx", "wb") as f:
        dill.dump(timeblock, f)
