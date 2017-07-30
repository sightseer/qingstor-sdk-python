import os
class FileChunk:
    '''file processing,including open file,move file pointer and read file

    Parameter:
        file_path(str):the relative path of the file
        part_size(int): the part size users want to partition of the file in byte

    Attributes:
        file_path(str):the relative path of the file
        part_size(int): the part size users want to partition of the file in byte
        source_file:source_file refers to the uploading file object
        part_wait_list(int): the list of part index which is waiting to upload 
        cur_read_part(str): the string of current part reading from the source file
        part_amount(int): the total part number partitioned of the source file according to the part size

    '''
    def __init__(self,file_path,part_size):
        self.file_path=file_path
        self.part_wait_list=[]       
        self.cur_read_part=""
        self.part_size=part_size

    def part_wait_list_init(self):
        part_amount=self.get_file_part_amount()
        #initialize the list, part index from 0 to part_amount-1
        for i in range(0,part_amount):
            self.part_wait_list+=[i]

    #the method is to calculate the total part number
    def get_file_part_amount(self):
        part_size=self.part_size
        file_path=self.file_path    
        part_amount=os.path.getsize(file_path)/part_size
        last_part=os.path.getsize(file_path)-part_size*part_amount 
        if  last_part>0:
             part_amount+=1
        return part_amount

    def read_file_part(self,part_index):
        part_size=self.part_size
        with open(self.file_path,"rb") as source_file:
            #move the original file pointer to the part_index
            source_file.seek(part_size*part_index,0)
            #read the current part content returned in the cur_read_part		
    	    cur_read_part=source_file.read(part_size)	
        return cur_read_part
    



