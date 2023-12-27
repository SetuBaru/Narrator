import pyttsx3
import os
import PyPDF2
import subprocess


# Extracting Text from the Pdf
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            _text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                _text += page.extract_text() + '\n\n'
                page_num += 1
            print(f'File {file_path} found!\n')
            return _text
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return ''
    except Exception as e:
        print(f"An error occurred while extracting text: {str(e)}")
        return ''


# Converting the Text to Audio
def text_to_audio(_text, _output_file, rate=150):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)

        # Save audio to a temporary file
        temp_file = _output_file + "_temp.wav"
        engine.save_to_file(_text, temp_file)
        engine.runAndWait()

        # Convert the temporary file to MP3 using subprocess
        subprocess.run(['ffmpeg', '-i', temp_file, _output_file])

        # Remove temporary file
        os.remove(temp_file)

        print(f"Audio file '{_output_file}' generated successfully!\n")
    except KeyboardInterrupt:
        print("\nConversion process interrupted.")
    except Exception as e:
        print(f"An error occurred during text-to-audio conversion: {str(e)}")


if __name__ == "__main__":
    # Getting Input File
    input_file = os.path.join("Ebooks", "Hansel-and-Gretel.pdf")  # Replace this with your PDF file path
    print(f'Input File: {input_file}.\n')

    # Setting Output File
    output_file = os.path.join("AudioBooks", os.path.basename(input_file).split('.')[0] + ".mp3")
    print(f'Output File: {output_file}.\n')

    # Extracting Text from Input File
    text = extract_text_from_pdf(input_file)
    if text:
        print('Text Extracted Successfully!\n')
        text_to_audio(text, output_file, rate=80)  # Adjust rate (words per minute) as needed
        print('Completed Successfully!')
    else:
        print("Text extraction failed. Please check the input file path.\n")
