from qingstor.sdk.error import BadRequestError,InvalidObjectNameError
import os
import mock
import unittest
from qingstor.sdk.client.upload_client import UploadClient
from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import Bucket
from qingstor.sdk.service.qingstor import QingStor

TEST_PART_SIZE=5242880
TEST_FILE_PATH='test_file_100M'
TEST_OBJECT_KEY='test_upload_20170804'
TEST_ACCESS_KEY='This_is_mock_access_key'
TEST_SECRET_ACCESS_KEY='This_is_mock_secret_access_key'

class MockHttpResponse:

    def __init__(self,status_code):
        self.status_code = status_code

    # Mock the upload_id
    def __getitem__(self, key):
        return 000000000000


class AccessConfig:

    def __init__(self):
        self.access_key=TEST_ACCESS_KEY
        self.secret_access_key=TEST_SECRET_ACCESS_KEY

    def set_qingstor(self):
        self.config = Config(self.access_key, self.secret_access_key)
        self.qingstor = QingStor(self.config)
        return self.qingstor


class TestUploadClient(unittest.TestCase):

    def setUp(self):
        os.system("dd if=/dev/zero of=test_file_100M bs=1024 count=102400")

    def tearDown(self):
        os.system("rm -f test_file_100M")

    def test_right_response(self):
        # Mock the output of initiate_multipart_upload
        output1=MockHttpResponse(200)
        http200=mock.Mock(return_value=output1)
        Bucket.initiate_multipart_upload=http200

        # Mock the output of upload_multipart
        output2=MockHttpResponse(201)
        http201=mock.Mock(return_value=output2)
        Bucket.upload_multipart=http201

        # Set the access config
        access_config=AccessConfig()
        qingstor=access_config.set_qingstor()

        # Create bucket instance
        bucket=qingstor.Bucket('test_upload_bucket','pek3a')
        upload_obj = UploadClient(bucket, TEST_PART_SIZE)
        with open(TEST_FILE_PATH, 'rb') as f:
            upload_obj.upload_file('upload_20180803.mp4', f)

    def test_initialize_bad_response(self):
        # Mock the output of initiate_multipart_upload
        output1=MockHttpResponse(400)
        http400=mock.Mock(return_value=output1)
        Bucket.initiate_multipart_upload=http400

        # Set the access config
        access_config = AccessConfig()
        qingstor = access_config.set_qingstor()

        # Create bucket instance
        bucket=qingstor.Bucket('test_upload_bucket','pek3a')
        upload_obj = UploadClient(bucket, TEST_PART_SIZE)
        with open(TEST_FILE_PATH, 'rb') as f:
            self.assertRaises(InvalidObjectNameError,upload_obj.upload_file,TEST_OBJECT_KEY,f)

    def test_upload_bad_response(self):
        # Mock the output of initiate_multipart_upload
        output1=MockHttpResponse(200)
        http200=mock.Mock(return_value=output1)
        Bucket.initiate_multipart_upload=http200

        # Mock the output of upload_multipart
        output2=MockHttpResponse(400)
        http400=mock.Mock(return_value=output2)
        Bucket.upload_multipart=http400

        # Set the access config
        access_config = AccessConfig()
        qingstor = access_config.set_qingstor()

        # Create bucket instance
        bucket=qingstor.Bucket('test_upload_bucket','pek3a')
        upload_obj = UploadClient(bucket, TEST_PART_SIZE)
        with open(TEST_FILE_PATH, 'rb') as f:
            self.assertRaises(BadRequestError,upload_obj.upload_file,TEST_OBJECT_KEY,f)

if __name__=="__main__":
    unittest.main()
