# Import the speech_recognition library as sr.
import speech_recognition as sr

# Specify the path to the audio file you want to transcribe.
AUDIO_FILE = "audio.wav"  # Replace with the path to your audio file.

# Initialize the recognizer object.
r = sr.Recognizer()

# Open the specified audio file using the AudioFile context manager.
with sr.AudioFile(AUDIO_FILE) as source:
    # Use the recognizer to read the audio file and store it in the 'audio' variable.
    audio = r.record(source)

# Try to recognize speech using the Google Speech Recognition service.
try:
    # Attempt to transcribe the audio using Google Speech Recognition and print the result.
    print("Audio file contains: " + r.recognize_google(audio))
except sr.UnknownValueError:
    # Handle the case where the recognizer couldn't understand the audio.
    print("Google Speech Recognition couldn't understand audio")
except sr.RequestError:
    # Handle the case where there was an issue making a request to the Google Speech Recognition service.
    print("Couldn't get the result from the Google Speech Recognition.")
