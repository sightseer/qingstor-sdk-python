#This module is used to print the expected output of part file reading
import os

PART_SIZE=50

def read_file_part(part_index,fd):
    # Move the original file pointer to the part_index.
    fd.seek(PART_SIZE * part_index, os.SEEK_SET)
    # Read the current part content returned in the cur_read_part.
    cur_read_part = fd.read(PART_SIZE)
    return cur_read_part
