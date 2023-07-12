from converter import Converter
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file",
                        help="The path to the input TIFF file.")
    parser.add_argument("-o", "--output_file",
                        help="The path to the output PNG file.")
    args = parser.parse_args()

    converter = Converter(args.input_file, args.output_file)
    converter.convert_tiff_to_png()


if __name__ == "__main__":
    main()
