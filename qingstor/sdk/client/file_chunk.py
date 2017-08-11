import os
from io import BytesIO

from ..constant import SEGMENT_SIZE

class FileChunk(object):

    def __init__(self,fd,part_size,callback):
        self.fd=fd
        self.part_size=part_size
        self._callback=callback

    def __iter__(self):
        return self

    def next(self):
        cur_part=""
        for i in range(SEGMENT_SIZE,self.part_size,SEGMENT_SIZE):
            cur_segment=self.fd.read(SEGMENT_SIZE)
            if cur_segment=="":
                break
            cur_part+=cur_segment
            self._callback()
        if cur_part:
            return cur_part
        else:
            raise StopIteration
