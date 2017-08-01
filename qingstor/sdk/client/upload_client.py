import os
import logging

from file_chunk import FileChunk
from qingstor.sdk.service.qingstor import QingStor
from constant import HTTP_CREATED,HTTP_OK,HTTP_BAD_REQUEST
from error import PartTooSmallError,MaxPartsExceededError,InvalidObjectNameError 


class UploadClient:
    '''file processing,including open file,move file pointer and read file

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte
        
    Attributes:
        file_descriptor(object): the source uploading file object
        file_name: the key(usually using file name) of the uploading file
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte
        
    '''

    def __init__(self,bucket,part_size):
    	if(part_size<4*1024*1024):
            raise PartTooSmallError()
        else:
            self.bucket=bucket
            self.part_size=part_size
            self.logger=logging.getLogger("qingstor-sdk")
        
    def upload_large_file(self,file_name,file_descriptor):
        # Initiate multipart upload, create an upload id.
        output=self.bucket.initiate_multipart_upload(file_name) 
        if output.status_code==HTTP_OK:
            self.logger.info("Multipart Upload Initialization Done!")   
        elif output.status_code==HTTP_BAD_REQUEST:
            raise InvalidObjectNameError()
        else:
            self.logger.error("Bad Request!")
            return
        this_upload_id=output['upload_id']
        file_chunk=FileChunk(self.part_size,file_descriptor)
        if(file_chunk.part_amount>1000):
            raise MaxPartsExceededError()    
        part_uploaded_list=[] 
        # This for loop is to upload each part iteratively until all parts uploaded.                
        for part_index in file_chunk.part_wait_list:
            cur_read_part=file_chunk.read_file_part(part_index)
            output=self.bucket.upload_multipart(
            file_name,
            upload_id=this_upload_id,
            part_number=part_index,
            body=cur_read_part
            )
            if output.status_code==HTTP_CREATED:
                part_uploaded_list+=[{"part_number":part_index}] 
                self.logger.info("%d Part Uploaded!"%part_index)
            elif output.status_code==HTTP_BAD_REQUEST:
                self.logger.error("Part Uploading Error!")
        # Check if the number of uploaded part equals to the original part amount, if so, this uploading is completed.
        if len(part_uploaded_list)==file_chunk.part_amount:
            complete_output=self.bucket.complete_multipart_upload(file_name,this_upload_id,object_parts=part_uploaded_list) 
            self.logger.info("Multipart Upload Completed!")
            return complete_output
        else:
            self.logger.error("Multipart Upload Failed!")
        

