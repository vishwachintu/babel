from translate import Translator
from playsound import playsound 
import speech_recognition as sr 
# from googletrans import Translator 
# from gtts import gTTS 
import os 
import sys
# import keyboard

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation
def takecommand(): 
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		print("listening.....") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing.....") 
		query = r.recognize_google(audio, language='en-in') 
		print(f"Detected Text: {query}\n") 
	except Exception as e: 
		print("say that again please.....") 
		return "None"
	return query 
query=" "
# Example usage
while True:
    query = takecommand() 
    while(query == "None"): 
        query = takecommand() 
    translated_text = translate_text(query, "ar")  # Translate to Arabic
    print("Translated text:", translated_text)
