from qingstor.sdk.service.qingstor import QingStor
from file_chunk import FileChunk
import os
class UploadClient:
    '''file processing,including open file,move file pointer and read file

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size_MB(int):the part size users want to partition of the file in MB
        file_name: the key(usually using file name) of the uploading file
        file_path(str): the relative path of the file
        

    Attributes:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size_MB(int): the part size users want to partition of the file in MB
        file_name: the key(usually using file name) of the uploading file
        file_path(str): the relative path of the file
        part_size(int): the part size users want to partition of the file in byte
        source_file: source_file refers to the uploading file object (from class FileChunk)
        part_wait_list(int): part_wait_list(int): the list of part index which is waiting to upload
        cur_read_part(str): the string of current part reading from the source file (from class FileChunk)        
        part_amount(int): the total part number partitioned of the source file according to the part size (from class FileChunk)
        this_upload_id: the unique upload id of the uploading file
        file_chunk: the instance of the class FileChunk
        part_index: the index of each part
        part_uploaded_list: the list of part index which completes uploading
        
    
    '''
    #httpstatus code
    status_part_created=201
    status_ok=200
    status_bad_request=400

    def __init__(self,bucket,part_size_MB):
    	self.bucket=bucket
        self.part_size=part_size_MB*1024*1024
        
    def upload_large_file(self,file_name,file_path):
        #initiate multipart upload, create an upload id
        output=self.bucket.initiate_multipart_upload(file_name) 
        if output.status_code==self.status_ok:
            print("Multipart Upload Initialization Done!")
        else:
            print("Invalid Request!") 
        this_upload_id=output['upload_id']
        file_chunk=FileChunk(file_path,self.part_size)
        file_chunk.part_wait_list_init()
        part_uploaded_list=[]
        #this while loop is to upload each part iteratively until all parts uploaded                
        while len(file_chunk.part_wait_list):
            part_index=file_chunk.part_wait_list[0]
            cur_read_part=file_chunk.read_file_part(part_index)
            output=self.bucket.upload_multipart(file_name,upload_id=this_upload_id,part_number=part_index,body=cur_read_part)
            if output.status_code==self.status_part_created:
                part_uploaded_list+=[{"part_number":part_index}]
                file_chunk.part_wait_list.pop(0)
                print("%d Part Uploaded!"%part_index)
            elif output.status_code==self.status_bad_request:
                print("Part Uploading Error!Error Cases:\n\
 [entity_too_small]The part size of the uploading file is smaller than the smallest limitation(4M)\n\
 [max_parts_exceeded]: The number of part exceeds part limitation(1000)\n\
 [upload_not_exists]: Upload id does not exist")
        if len(file_chunk.part_wait_list)==0:
            complete_output=self.bucket.complete_multipart_upload(file_name,this_upload_id,object_parts=part_uploaded_list) 
            print("Multipart Upload Completed!")
            return complete_output 




