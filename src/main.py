from converter import Converter


def main():
    input_file = './resources/file_example.tiff'
    output_file = './resources/file_example.png'
    converter = Converter(input_file, output_file)
    converter.convert_pdf_to_png()


if __name__ == "__main__":
    main()
