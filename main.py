from gtts import gTTS
import PyPDF2

def pdf_to_text(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    print("Audio saved as output.mp3")

def main():
    pdf_file = '12 Rules for Life Jordan Peterson.pdf'  # Replace with your PDF file path
    print("Extracting text from the PDF...")
    text = pdf_to_text(pdf_file)

    if text:
        print("Text extracted successfully! Converting to speech...")
        text_to_speech(text)
    else:
        print("No text found in the PDF.")

if __name__ == "__main__":
    main()
