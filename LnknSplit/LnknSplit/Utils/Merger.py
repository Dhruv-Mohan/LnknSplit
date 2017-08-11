import os
from Utils import split_pb2
class Merger(object):
    """Class to merge split files"""

    def __init__ (self, header_file_path=None, output_dir=None):
        self.file_path = header_file_path
        self.input_dir, self.file_name = os.path.split(self.file_path)
        self.output_dir = output_dir
        if self.output_dir is None:
            self.output_dir = self.input_dir


    def merge_file(self):
        header_proto_info = split_pb2.Data_header()
        with open(self.file_path,"rb") as header_reader:
            header_proto_info.ParseFromString(header_reader.read())

        self.final_filename = header_proto_info.Final_file_name
        trunc = open(self.output_dir + '\\' + self.final_filename, "wb")
        trunc.close()
        for part_file_name in header_proto_info.File_name:
            self.deposit_chunk(part_file_name)

    def deposit_chunk(self, part_file_name):
        with open(self.output_dir + '\\' + self.final_filename, "ab") as final_file_writer:
            with open(self.input_dir + '\\' + part_file_name, "rb") as chunk_file_reader:
                chunk_info = split_pb2.Data_chunk()
                chunk_info.ParseFromString(chunk_file_reader.read())
                final_file_writer.write(chunk_info.Chunk)



