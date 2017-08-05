import os
import unittest
from qingstor.sdk.client.file_chunk import FileChunk


# The part size of each reading
TEST_PART_SIZE = 50
TEST_PART_INDEX = 10
# Expected_amount = size(test_small_file.txt)/test_part_size=1024*500/50=10240
EXPECTED_AMOUNT = 10240
TEST_FILE_PATH="test_small_file"

class TestFileChunk(unittest.TestCase):
    def setUp(self):
        os.system("dd if=/dev/zero of=test_small_file bs=1024 count=500")

    def tearDown(self):
        os.system("rm -f test_small_file")

    def test_read_file_part(self):
        with open(TEST_FILE_PATH, "rb") as f:
            f.seek(TEST_PART_SIZE*TEST_PART_INDEX, os.SEEK_SET)
            expected_output=f.read(TEST_PART_SIZE)
            f.seek(0, os.SEEK_SET)
            temp_file_chunk = FileChunk(TEST_PART_SIZE, f)
            test_output = temp_file_chunk.read_file_part(TEST_PART_INDEX)
        self.assertEqual(expected_output,test_output)

    def test_get_part_amount(self):
        with open(TEST_FILE_PATH, "rb") as f:
            temp_file_chunk = FileChunk(TEST_PART_SIZE, f)
            test_amount=temp_file_chunk.get_file_part_amount()
        self.assertEqual(test_amount,EXPECTED_AMOUNT)

if __name__=="__main__":
    unittest.main()

