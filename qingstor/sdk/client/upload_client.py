import os
import logging

from ..file_chunk import FileChunk
from ..constant import (
    HTTP_OK,
    MAX_PARTS,
    HTTP_CREATED,
    HTTP_BAD_REQUEST,
    DEFAULT_PART_SIZE,
    SMALLEST_PART_SIZE
)
from error import (
    BadRequestError,
    PartTooSmallError,
    MaxPartsExceededError,
    InvalidObjectNameError
)


class UploadClient:
    """file processing,including open file,move file pointer and read file

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    Attributes:
        file_descriptor(object): the source uploading file object
        file_name: the key(usually using file name) of the uploading file
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    """

    def __init__(self, bucket, part_size=DEFAULT_PART_SIZE):
        if (part_size < SMALLEST_PART_SIZE):
            raise PartTooSmallError()
        else:
            self.bucket = bucket
            self.part_size = part_size
            self.logger = logging.getLogger("qingstor-sdk")

    def upload_file(self, file_name, file_descriptor):
        file_chunk = FileChunk(self.part_size, file_descriptor)
        # Check the file size and part amount
        if (file_chunk.file_size < SMALLEST_PART_SIZE):
            self.bucket.put_object(file_name, file_descriptor)
            return
        elif (file_chunk.part_amount > MAX_PARTS):
            raise MaxPartsExceededError()
        # Initiate multipart upload, create an upload id.
        output = self.bucket.initiate_multipart_upload(file_name)
        if output.status_code == HTTP_BAD_REQUEST:
            raise InvalidObjectNameError()
        elif output.status_code != HTTP_OK:
            self.logger.error("Bad Request!")
            return
        this_upload_id = output['upload_id']
        part_uploaded_list = []
        # This for loop is to upload each part iteratively until all parts uploaded.
        for part_index in file_chunk.part_wait_list:
            cur_read_part = file_chunk.read_file_part(part_index)
            output = self.bucket.upload_multipart(
                file_name,
                upload_id=this_upload_id,
                part_number=part_index,
                body=cur_read_part)
            if output.status_code == HTTP_CREATED:
                part_uploaded_list += [{"part_number": part_index}]
            else:
                raise BadRequestError()

        # Check if the number of uploaded part equals to the original part amount, if so, this uploading is completed.
        if len(part_uploaded_list) == file_chunk.part_amount:
            self.bucket.complete_multipart_upload(
                file_name, this_upload_id, object_parts=part_uploaded_list)
            self.logger.info("Multipart Upload Completed!")
        else:
            raise BadRequestError()
        return
