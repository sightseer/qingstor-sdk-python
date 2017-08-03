# This class is used to mock the outputs of some methods in Bucket
class MockOutput:
    def __init__(self,status_code):
        self.status_code = status_code

    def __getitem__(self, key):
        return 000000000000

