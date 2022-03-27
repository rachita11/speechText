import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

print("Choose your language and provide the code:")
print("1 - English   2 - Hindi   3 - Bengali   4 - Kannada   5 - Malayalam")
n = int(input())
# listening to the microphone

with sr.Microphone() as source:
    try:
            # using google speech recognition
        if(n==1):
            while(True):
                print("Talk")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text)

                print(text)
        elif(n==2):
            while(True):
                print("Talk")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text,language = "hi-IN")

                print(text)
        elif(n==3):
            while(True):
                print("Talk")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text,language = "bn-IN")
                print(text)
            
        elif(n==4):
            while(True):
                print("Talk")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text,language = "kn-IN")
                print(text)
        elif(n==5):
            while(True):
                print("Talk")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text,language = "ml-IN")
                print(text)
    #handeling keyboard interrupt
    except(KeyboardInterrupt):
        print("Listening stopped.")
    except:
        print("I couldn't hear anything...sorry")
        #recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
