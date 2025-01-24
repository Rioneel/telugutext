import yt_dlp
import speech_recognition as sr
import os

# Function to download and convert YouTube videos to WAV
def download_and_convert(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Save as the video title.wav
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])  # Download and convert to WAV
        if result == 0:
            print(f"Successfully downloaded and converted: {url}")
        else:
            print(f"Failed to download: {url}")
        return result

# Function to transcribe audio using speech recognition
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    # Load the audio file using the recognizer
    with sr.AudioFile(file_path) as source:
        print(f"Listening to the audio file: {file_path}")
        audio = recognizer.record(source)
    
    # Convert audio to text using Google Web Speech API with Telugu language support
    try:
        text = recognizer.recognize_google(audio, language="te-IN")
        print("Transcription in Telugu: ", text)
        
        # Save the Telugu transcription to a text file
        transcription_file = file_path.replace(".wav", "_transcription.txt")
        with open(transcription_file, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Transcription saved to: {transcription_file}")
    
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    except sr.UnknownValueError:
        print("Audio could not be understood")

# Main function to process YouTube URLs and transcribe
def main():
    # Example: Replace this with the actual reading of URLs from your Excel or other input
    urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]  # Sample URL, replace with real ones
    
    for url in urls:
        print(f"Processing: {url}")
        download_result = download_and_convert(url)
        
        # Assuming the WAV file is saved with the title as its name
        wav_file = None
        for file in os.listdir():
            if file.endswith(".wav"):
                wav_file = file
                break
        
        # If a WAV file was created, transcribe it
        if wav_file:
            transcribe_audio(wav_file)
        else:
            print("No WAV file found for transcription")

# Run the main function
if __name__ == "__main__":
    main()
