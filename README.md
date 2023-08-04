# OCR for Regional Languages

This OCR Web Application is a powerful tool that combines the capabilities of Optical Character Recognition (OCR) and text translation. Users can upload an image containing text, and the application will automatically extract the text using easyocr. The extracted text can then be translated to English using googletrans, and an audio file for the translated text is generated with gTTS. The application offers a user-friendly interface for easy interaction and immediate results.

## Usage
📸 OCR For Regional Languages takes an input image <br>
💻 Enter the language code <br>
📝 Get the translated text! <br>
🎙️ Select Text-to-Speech to hear the translated text

## Features
* Image Upload: Users can upload images containing text for OCR processing.
* Text Extraction: The application uses easyocr to extract text from the uploaded image.
* Language Code: Users have to select the language code based on the text in the image.
* Text Translation: The extracted text is then trnslated into English.
* Audio Generation: An audio file for the translated text is generated with gTTS.
* Interactive Web Interface: The application provides a user-friendly web interface for easy image upload and text processing.

## Installations
1. Clone the repository to your local machine:
```
git clone https://github.com/melita-celia/ocr-for-regional-languages.git
cd your_folder
```

2. Create a virtual environment and activate it (optional but recommended):
```
python -m venv venv
source venv\Scripts\activate  
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the Django development server:
```
python manage.py runserver
```

5. Open your web browser and navigate to http://127.0.0.1:8000 to access the OCR for Regional Languages.
   
## Technologies Used
* Python
* Django
* easyocr
* googletrans
* gTTS

## Team Members
* Melita Lewis
* Sushree Nadiminty
* Angelica Sebastian
* Shaun Noronha

## Contributing
Contributions to the OCR for Regional Languages project are welcome. If you encounter any issues or have ideas for new features, feel free to open an issue or submit a pull request.
