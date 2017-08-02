from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.client.upload_client import UploadClient
part_size=5242880
config=Config('NNVTMYBHVSBCWYDIQQYC','uUYcSlnpwZXuxSXRNpYDVMH7AzuQ699n8NfRvYgc')
qingstor=QingStor(config)
bucket=qingstor.Bucket('test-bucket-pysdk','pek3a')
up_obj = UploadClient(bucket, part_size)
#with open('test_fileL_starwars.mp4', 'rb') as f:
with open('test_fileS.txt', 'rb') as f:
    output = up_obj.upload_file('starwars20180802.mp4', f,)

"""
new_bucket=GetBucket()
bukcet=new_bucket.get_bukcet('NNVTMYBHVSBCWYDIQQYC',
                 'uUYcSlnpwZXuxSXRNpYDVMH7AzuQ699n8NfRvYgc',
                 'test-bucket-pysdk','pek3a')
"""
