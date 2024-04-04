# PROJECT_Nyrio_OCR
PROJECT Nyrio Ned2  avec OCR
This project aims to develop a program for OCR letter detection using an SVM classifier compared with the PyTesseract library for optical character recognition.

Table of Contents
Description
Installation
Usage
Example
Contributing
License
Description
The program uses an SVM model for character classification on preprocessed images. Images are resized and preprocessed before being passed to the SVM model for classification. Detected characters are then compared with the results from PyTesseract to evaluate the model's performance.

Installation
Clone this repository:
bash
Copy code
git clone https://github.com/your_username/project_name.git
Install the required dependencies:
bash
Copy code
pip install numpy tensorflow opencv-python scikit-learn matplotlib pytesseract pillow
Usage
Place your images in the alphabet_resize/ directory.
Run the main.py script.
Check the results in the console output and the generated images.
Example
Here is an example of usage:

bash
Copy code
python main.py
Contributing
Contributions are welcome! To contribute to this project, please submit a pull request describing your changes.

License
This project is licensed under the MIT License. For more information, please see the LICENSE file.