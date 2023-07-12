from pdf2image import convert_from_path
from PIL import Image


class Converter():
    '''
    The converter class is responsible for converting files to PNG images.
    '''

    def __init__(self, input_file: str, output_file: str) -> None:
        '''
        Initializes a Converter instance with the input and output file paths.

        Args:
            input_file (str): The path of the input file to be converted.
            output_file (str): The path to save the converted PNG image.
        '''
        self.input_file = input_file
        self.output_file = output_file

    def convert_tiff_to_png(self):
        '''
        Converts a TIFF file to a PNG image.

        This method uses the PIL library to open the TIFF file and save it as a PNG image.

        Note:
            This method assumes that the input file is a TIFF image and the output file has a '.png' extension.

        Raises:
            IOError: If there is an error opening or saving the image.

        '''
        
        im = Image.open(self.input_file)
        im.save(self.output_file)
