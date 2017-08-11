import os
from Utils import split_pb2
class Splitter(object):
    """Class to split an object into user defined proto chunks"""

    def __init__(self, file_path=None, output_dir=None, chunk_size=512*1024):
        self.chunk_size = chunk_size
        self.file_path = file_path
        self.input_dir, self.file_name = os.path.split(file_path)
        self.output_dir = output_dir
        if self.output_dir is None:
            self.output_dir = self.input_dir
        self.file_prefix, _ = os.path.splitext(self.file_name)
        self.file_index = 0

    def split_file(self):
        ''' engine funciton of the class, reads the input file and calls the supporting functions'''
        with open(self.file_path,"rb") as original_file: #read chunks till end
            with open(self.output_dir + '\\' + self.file_prefix + '_Header.head',"wb") as header_proto_writer:
                header_proto_info = split_pb2.Data_header()
                header_proto_info.Final_file_name = self.file_name
                while True:
                    chunk = original_file.read(self.chunk_size)
                    if len(chunk) is 0:
                        header_proto_writer.write(header_proto_info.SerializeToString())
                        break
                    self.update_chunk_filename()
                    header_proto_info.File_name.extend([self.chunk_filename])
                    self.write_chunk(chunk)

    def write_chunk(self, chunk):
        ''' Writes chunks of data into chunk proto files '''
        chunk_info = split_pb2.Data_chunk()
        with open(self.output_dir + '\\' + self.chunk_filename, "wb") as chunk_writer:
            chunk_info.Chunk = chunk
            chunk_writer.write(chunk_info.SerializeToString())


    def update_chunk_filename(self):
        '''Updates internal chunk_filename after chunk is written '''
        self.chunk_filename = self.file_prefix + '_Chunk_' + str(self.file_index) + '.part'
        self.file_index = self.file_index + 1