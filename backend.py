from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

@app.route('/process_audio', methods=['POST'])
def process_audio():
    file = request.files['file']
    
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio)
        response_text = "You said: " + text  # Simple echo response
        tts_engine.save_to_file(response_text, 'response.mp3')
        tts_engine.runAndWait()
        
        return jsonify({'text': response_text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand audio'})
    except sr.RequestError:
        return jsonify({'error': 'Error with the speech recognition service'})

if __name__ == '__main__':
    app.run(debug=True)
