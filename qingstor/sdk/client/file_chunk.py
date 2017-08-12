import os

from ..constant import SEGMENT_SIZE

class FileChunk(object):

    def __init__(self,fd,part_size,callback):
        self.fd=fd
        self.part_size=part_size
        self.callback=callback

    def __iter__(self):
        return self

    def next(self):
        cur_part=b""
        for i in range(SEGMENT_SIZE,self.part_size,SEGMENT_SIZE):
            cur_segment=self.fd.read(SEGMENT_SIZE)
            cur_segment=cur_segment.encode()
            if cur_segment==b"":
                break
            cur_part+=cur_segment
            self.callback()
        if cur_part:
            return cur_part
        else:
            raise StopIteration
