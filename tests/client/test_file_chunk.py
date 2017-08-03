import unittest
from read_file_part import *
from qingstor.sdk.client.file_chunk import FileChunk


# The part size of each reading
PART_SIZE = 50
PART_INDEX = 18
FILE_PATH="test_file_12M.mp3"

class TestFileChunk(unittest.TestCase):
    def test_read_file_part(self):
        expected_output=""
        with open(FILE_PATH, "rb") as f:
            expected_output=read_file_part(PART_INDEX,f)
        test_output=""
        with open(FILE_PATH, "rb") as f:
            temp_file_chunk = FileChunk(PART_SIZE, f)
            test_output = temp_file_chunk.read_file_part(PART_INDEX)
        self.assertEqual(expected_output,test_output)

if __name__=="__main__":
    unittest.main()
