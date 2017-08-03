from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.service.qingstor import Bucket
from mock_output import MockOutput
from qingstor.sdk.client.upload_client import UploadClient
import mock
TEST_PART_SIZE=5242880
TEST_FILE_PATH='test_file_12M.mp3'

config=Config('This_is_mock_access_key','This_is_mock_secret_access_key')
qingstor=QingStor(config)
# Mock the output of initiate_multipart_upload
output1=MockOutput(200)
code200=mock.Mock(return_value=output1)
Bucket.initiate_multipart_upload=code200
# Mock the output of upload_multipart
output2=MockOutput(201)
code201=mock.Mock(return_value=output2)
Bucket.upload_multipart=code201
# Create bucket instance
bucket=qingstor.Bucket('test-upload_bucket','pek3a')
upload_obj = UploadClient(bucket, TEST_PART_SIZE)
with open(TEST_FILE_PATH, 'rb') as f:
    output = upload_obj.upload_file('upload_20180803.mp4', f,)


