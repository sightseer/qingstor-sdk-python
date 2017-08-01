import os
from ..error import PartTooSmallError
class FileChunk:
    '''file processing,including open file,move file pointer and read file

    Parameter:
        part_size(int): the part size users want to partition of the file in byte
        part_wait_list(int): the list of part index which is waiting to upload 
        cur_read_part(str): the string of current part reading from the source file
        file_descriptor(object): the source uploading file object
        part_amount(int): the total part number partitioned of the source file according to the part size

    Attributes:
        part_size(int): the part size users want to partition of the file in byte
        part_wait_list(int): the list of part index which is waiting to upload 
        cur_read_part(str): the string of current part reading from the source file
        part_amount(int): the total part number partitioned of the source file according to the part size
        part_index: the index of each part

    '''
    def __init__(self,part_size,file_descriptor):
        if part_size<4:
            raise PartTooSmallError()
        self.part_wait_list=[]     
        self.cur_read_part=""
        self.part_size=part_size
        self.file_descriptor=file_descriptor
        self.part_amount=self.get_file_part_amount()
        #initialize the part_wait_list according to part_amount
        for i in range(0,self.part_amount):
            self.part_wait_list+=[i]

    #the method is to calculate the total part number
    def get_file_part_amount(self):
        self.file_descriptor.seek(0,2)
        file_size=self.file_descriptor.tell()
        part_size=self.part_size
        part_amount=file_size/part_size
        last_part=file_size-part_size*part_amount 
        if  last_part>0:
             part_amount+=1
        return part_amount

    def read_file_part(self,part_index):
        part_size=self.part_size
        #move the original file pointer to the part_index
        self.file_descriptor.seek(part_size*part_index,0)
        #read the current part content returned in the cur_read_part		
    	cur_read_part=self.file_descriptor.read(part_size)	
        return cur_read_part




