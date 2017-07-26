from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config
import os
class UploadFile:
    is_complete=0
#    global part_list
    def __init__(self,bucket,part_size_MB):
    	self.bucket=bucket
        self.part_size=part_size_MB*1024*1024
        	
    def upload_large_file(self,file_name,file_path):
        output=self.bucket.initiate_multipart_upload(file_name) #initiate multipart upload, create an upload id
        this_upload_id=output['upload_id']
        original_file=open(file_path,"rb")
        part_list=[]                #part_list stores the part number which completes uploading
        part_amount=os.path.getsize(file_path)/self.part_size
        last_part=os.path.getsize(file_path)-self.part_size*part_amount
        if  last_part>0:
             part_amount+=1
        part_num_list=[]       #part_num_list stores the part number which has not yet uploaded
        for i in range(0,part_amount):
             part_num_list+=[i]
        while len(part_num_list):
            part_index=part_num_list[0]
            original_file.seek(self.part_size*part_index,0)		#move the original file pointer to the part_index
    	    cur_read_part=original_file.read(self.part_size)	#read the current part content returned in the cur_read_part
            output=self.bucket.upload_multipart(file_name,upload_id=this_upload_id,part_number=part_index,body=cur_read_part)
            if output.status_code==201:
                part_list+=[{"part_number":part_index}]
                part_num_list.pop(0)        
        if len(part_num_list)==0:
            complete_output=self.bucket.complete_multipart_upload(file_name,this_upload_id,object_parts=part_list) 
            print(complete_output.content)
            return complete_output
        
        
        




