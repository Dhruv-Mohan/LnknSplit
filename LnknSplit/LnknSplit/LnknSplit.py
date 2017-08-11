from Utils import split_pb2
from Utils.Splitter import Splitter
from Utils.Merger import Merger





split_object = Splitter(file_path='E:\\test.epub', chunk_size=100*1024, output_dir = 'E:\\LnknSplit')
split_object.split_file()

#Spliter objects create a inputfilename_Header.head file. Merger objects use this file to reconstruct the file split. 
merge_object = Merger(header_file_path='E:\\LnknSplit\\test_Header.head', output_dir='E:\\LnknSplit\\Testout')
merge_object.merge_file()


