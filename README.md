# Narrator

---

This Python script converts text from a PDF file into an MP3 audio file. The conversion is achieved by leveraging the PyPDF2 and pyttsx3 libraries along with subprocesses for handling audio file formats.

## Features

- **PDF Text Extraction:** Extracts text from a provided PDF file using PyPDF2.
- **Text-to-Audio Conversion:** Converts the extracted text into an MP3 audio file using pyttsx3.
- **Customizable Rate:** Adjustable rate (words per minute) for the generated audio output.

## Requirements

- Python 3.x
- PyPDF2
- pyttsx3
- FFmpeg (for audio file format conversion)

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SetuBaru/Narrator.git
   cd Narrator
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**

   ```bash
   python main.py
   ```

   Customize the input file path, output file path, and rate (words per minute) within `main.py` as needed.

## Usage Examples

```python
# Customize the input and output file paths in main.py
input_file = os.path.join("Ebooks", [Your Ebook Name].pdf")
output_file = os.path.join("AudioBooks", os.path.basename(input_file).split('.')[0] + ".mp3")

# Extract text and convert to audio
text = extract_text_from_pdf(input_file)
if text:
    text_to_audio(text, output_file, rate=80)
```

## Future Work

I'm hoping to integrate RetreivalBased Voice Conversion to improve the audio qulity of the result using Machine Learning Technology, a sample of the expected results can be found within the sample_results sub folder!
<img width="1600" alt="Screenshot 2023-12-28 at 01 13 52" src="https://github.com/SetuBaru/Narrator/assets/78774159/6d490ac8-291f-441d-b1a1-18d5bc434b60">


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
