from qingstor.sdk.service.qingstor import QingStor
from file_chunk import FileChunk
from ..constants import HTTP_CREATED,HTTP_OK,HTTP_BAD_REQUEST
from ..error import PartTooSmallError,MaxPartsExceededError
import logging
import os
class UploadClient:
    '''file processing,including open file,move file pointer and read file

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size_MB(int):the part size users want to partition of the file in MB
        part_size(int): the part size users want to partition of the file in byte
        

    Attributes:
        file_descriptor(object): the source uploading file object
        file_name: the key(usually using file name) of the uploading file
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size_MB(int): the part size users want to partition of the file in MB
        part_size(int): the part size users want to partition of the file in byte
        part_wait_list(int): part_wait_list(int): the list of part index which is waiting to upload
        cur_read_part(str): the string of current part reading from the source file (from class FileChunk)        
        part_amount(int): the total part number partitioned of the source file according to the part size (from class FileChunk)
        this_upload_id: the unique upload id of the uploading file
        file_chunk: the instance of the class FileChunk
        part_index: the index of each part
        part_uploaded_list: the list of part index which completes uploading
        
    
    '''


    def __init__(self,bucket,part_size_MB):
    	if(part_size_MB<4):
            raise PartTooSmallError()
        else:
            self.bucket=bucket
            self.part_size=part_size_MB*1024*1024
            self.logger=self.log_config()
        
    def upload_large_file(self,file_name,file_descriptor):
        #initiate multipart upload, create an upload id
        output=self.bucket.initiate_multipart_upload(file_name) 
        if output.status_code==HTTP_OK:
           self.logger.info("Multipart Upload Initialization Done!")   
        else:
            self.logger.error("Invalid Request!") 
        this_upload_id=output['upload_id']
        file_chunk=FileChunk(self.part_size,file_descriptor)
        if(file_chunk.part_amount>1000):
            raise MaxPartsExceededError()    
        part_uploaded_list=[] 
        #this while loop is to upload each part iteratively until all parts uploaded                
        while len(file_chunk.part_wait_list):
            part_index=file_chunk.part_wait_list[0]
            cur_read_part=file_chunk.read_file_part(part_index)
            output=self.bucket.upload_multipart(file_name,upload_id=this_upload_id,part_number=part_index,body=cur_read_part)
            if output.status_code==HTTP_CREATED:
                part_uploaded_list+=[{"part_number":part_index}]
                file_chunk.part_wait_list.pop(0)
                self.logger.info("%d Part Uploaded!"%part_index)
            elif output.status_code==HTTP_BAD_REQUEST:
                self.logger.error("Part Uploading Error!")
        if len(file_chunk.part_wait_list)==0:
            complete_output=self.bucket.complete_multipart_upload(file_name,this_upload_id,object_parts=part_uploaded_list) 
            self.logger.info("Multipart Upload Completed!")
            return complete_output 


    def log_config(self):
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        fh=logging.StreamHandler()
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
        

