
from recognition import recognize_speech_from_mic
from speaking import speak
import speech_recognition as sr

if __name__ == "__main__":
    print('pronto a essere conosciuto')
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    response = recognize_speech_from_mic(recognizer, mic)
    print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}'
          .format(response['success'],
                  response['error'],
                  '-'*17,
                  response['transcription']))
    speak('it', response['transcription'])
