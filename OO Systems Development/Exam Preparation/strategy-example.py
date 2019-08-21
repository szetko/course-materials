from abc import ABC, abstractmethod


class Decompressor(ABC):

    def __init__(self, filename):
        self.filename = filename
        self.suffix = f.split('.')[-1]

    @abstractmethod
    def decompress_file(self):
        pass


class DOCXDecompressor(Decompressor):
    def decompress_file(self):
        detected_msg = 'docx detected'
        return detected_msg


class XLSXDecompressor(Decompressor):
    def decompress_file(self):
        detected_msg = 'xlsx detected'
        return detected_msg


class PPTXDecompressor(Decompressor):
    def decompress_file(self):
        detected_msg = 'pptx detected'
        return detected_msg


def decompressor_factory(filename):
    extension_map = {"docx": DOCXDecompressor,
                     "xlsx": XLSXDecompressor,
                     "pptx": PPTXDecompressor}
    suffix = filename.split('.')[-1]
    return extension_map[suffix](filename)


if __name__ == '__main__':
    files = ['file1.docx', 'file2.xlsx', 'file3.pptx', 'file4.pub']
    for f in files:
        try:
            decompressor = decompressor_factory(f)
            print(decompressor.decompress_file())
        except KeyError as e:
            print(e, 'extension not found')
