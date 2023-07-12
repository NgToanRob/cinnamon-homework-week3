# CINNAMON HW3 – AI-Venger

Our library is a powerful tool for converting various file formats to images. It provides a convenient and efficient way to transform files such as PNG, HEIC, TIFF, and PDF into PNG images.

## Table of Contents
0. Introduction
1. Installation
2. Contributing
3. License


## I. Introduction 🌟

This repository contains the following files and folders:

- **resources**: Contains test images for validating the library's functionality.
- **sources**: Contains the main code for the file-to-image conversion.
    - **converter.py**: Implements the file-to-image conversion logic.
    - **main.py**: Provides an example usage of the library.
- **test**: Contains unit tests for verifying the correctness of the library.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **LICENSE**: Contains the license information for the library.
- **requirements.txt**: Lists the dependencies required by the library.

## II. Installation 📥

To install this library, follow the steps below:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/NgToanRob/cinnamon-homework-week3.git
```

2. Navigate to the project directory:

```bash
cd cinnamon-homework-week3
```

3. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

4. Execute the script using the following command:

```shell
python src/main.py --i input_file.tiff --o output_file.png
```

- Replace input_file.tiff with the path to your input TIFF file.
- Replace output_file.png with the desired path for the output PNG file.

The script will convert the input TIFF file to a PNG image and save it at the specified output file path.

## III. Contributing 🤝
Contributions to the library are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Open a pull request, providing a detailed description of your changes and the motivation behind them.

## IV. License ⚖️
The library is open source and is licensed under the MIT License. For more information, please see the LICENSE file.
