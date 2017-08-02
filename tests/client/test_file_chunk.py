from qingstor.sdk.client.file_chunk import FileChunk
part_size=20
with open('test_fileS.txt','rb') as f:
    output=FileChunk(part_size,f)
    for part_index in range(output.part_amount):
        cur_part_content=output.read_file_part(part_index)
        print cur_part_content
