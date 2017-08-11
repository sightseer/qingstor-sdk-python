import os


class ReadFile(object):

    def __init__(self,fd,part_size):
        self.fd=fd
        self.part_size=part_size

    def __iter__(self):
        return self

    def next(self):
        cur_part = self.fd.read(self.part_size)
        if cur_part:
            return cur_part
        else:
            raise StopIteration
