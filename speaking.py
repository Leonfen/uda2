import os
from gtts import gTTS

# The text that you want to convert to audio


def speak(language, text):
    if text is None:
        print('asd')
        speak('it', 'Scusa, non ho capito bene; puoi ripetere?')
    # Language in which you want to convert
    try:
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=text, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("./temp/welcome.mp3")

        # Playing the converted file
        os.system("./temp/welcome.mp3")
        return
    except:
        speak('it', 'Scusa, non ho capito bene; puoi ripetere?')
        return
