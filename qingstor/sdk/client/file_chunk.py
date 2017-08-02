import os

from ..error import PartTooSmallError
from ..constant import SMALLEST_PART_SIZE


class FileChunk:
    """file processing,including open file,move file pointer and read file

    Parameter:
        part_size(int): the part size users want to partition of the file in byte
        fd(object): the source uploading file object

    Attributes:
        part_size(int): the part size users want to partition of the file in byte
        cur_read_part(str): the string of current part reading from the source file
        part_index: the index of each part

    """

    def __init__(self, part_size, fd):
        if part_size < SMALLEST_PART_SIZE:
            raise PartTooSmallError()
        self.part_size = part_size
        self.fd = fd
        self.part_amount = self.get_file_part_amount()
        self.part_wait_list = []
        # Initialize the part_wait_list according to part_amount.
        for i in range(0, self.part_amount):
            self.part_wait_list += [i]

    # The method is to calculate the total part number.
    def get_file_part_amount(self):
        self.fd.seek(0, os.SEEK_END)
        self.file_size = self.fd.tell()
        part_size = self.part_size
        part_amount = self.file_size // part_size
        last_part = self.file_size - part_size * part_amount
        if last_part > 0:
            assert isinstance(part_amount, object)
            part_amount += 1
        return part_amount

    def read_file_part(self, part_index):
        part_size = self.part_size
        # Move the original file pointer to the part_index.
        self.fd.seek(part_size * part_index, os.SEEK_SET)
        # Read the current part content returned in the cur_read_part.
        cur_read_part = self.fd.read(part_size)
        return cur_read_part
