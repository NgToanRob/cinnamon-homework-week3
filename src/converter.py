from pdf2image import convert_from_path
from PIL import Image


class Converter():
    '''
    {Dokument here bro}
    '''

    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file

    def convert_tiff_to_png(self):
        '''
        And here!!!!!!!!
        '''
        im = Image.open(self.input_file)
        im.save(self.output_file)
