import smtplib

import speech_recognition as sr
import pyttsx3
import webbrowser
# import openai
import datetime
import pywhatkit
import os
import random
import time
import pyaudio


# pywhatkit.sendwhatmsg("+917900632387", "Class sorry", 22, 10)


import pyttsx3
from wikipedia import wikipedia


def speak(text, gender='female'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 'female':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from shiri"

if __name__ == "__main__":
    speak("Hello boss, I am shiri, your virtual assistant ", gender='female')
    while True:
        print("Listening.....")  
        query = takeCommand()

        if "wikipedia" in query:  # if wikipedia found in the query then this block will be executed
            speak("Searching Wikipedia boss...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # todo : Add zxsmore sites
        sites = [["Youtube", "https://www.Youtube.com"],
          ["Whatsapp","https://web.Whatsapp.com"], ["google","https://www.google.com"],
          ["Ayurvedic", "https://www.netmeds.com/"],
          ["Login page", "http://115.244.87.227/Login"],
          ["chat gpt", "https://chat.openai.com/"],
          ["News", "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"],
          ["Classroom", "https://classroom.com"],
          ["VS Code", "C:\\Users\\user 2\OneDrive\Microsoft VS Code\Code.exe"],
          ["Spotify", "C:\\Users\\user 2\OneDrive\Desktop\Spotify.lnk"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} boss......")
                webbrowser.open(site[1])

        # todo : Add a feature to play a specific song
        if "open music" in query:
            speak(f"Opening music boss......")



        def get_audio_files(directory):
            return [f for f in os.listdir(directory) if f.endswith(('.mp3', '.wav', '.ogg'))]

        def play_random_music(directory):
            audio_files = get_audio_files(directory)
            random.shuffle(audio_files)

            for audio_file in audio_files:
                    file_path = os.path.join(directory, audio_file)
                    os.startfile(file_path)
                    time.sleep(5)  # Wait for 5 seconds between songs


            # Replace 'your_directory_path' with the path to your music directory
            play_random_music('C:\\Users\\user 2\OneDrive\Desktop\music')

            # os.startfile(musicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"boss the time is{strfTime}")

        if "open photos" in query:
            speak(f"Opening photos boss.....")
            os.startfile(f"C:\\Users\\user 2\OneDrive\Desktop\clg")




        # if "spotify" in query:
        #     speak(f"Opening spotify boss.....")
        #     os.system(f"C:\\Users\\user 2\OneDrive\Desktop\Spotify.lnk")


        # speak(query)

        # def sendEmail(to, content):
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.ehlo()
        #     server.starttls()
        #     server.login('monichaudhary2004@gmail.com', 'Vanshika123')
        #     server.sendmail('monichaudhary2004@gmail.com', to, content)
        #     server.close()

        if "open camera" in query:
            speak(f"Opening camera boss.....")
            import cv2

        # Function to capture an image using webcam
            def capture_photo():
                # Open the webcam
                cap = cv2.VideoCapture(0)

                # Check if the webcam is opened successfully
                if not cap.isOpened():
                    print("Error: Unable to open webcam")
                    return

                # Capture a frame from the webcam
                ret, frame = cap.read()

                # Check if the frame is captured successfully
                if not ret:
                    print("Error: Unable to capture frame")
                    return

                # Save the captured frame as an image
                cv2.imwrite('captured_photo.jpg', frame)

                # Release the webcam
                cap.release()

                print("Photo captured successfully!")


            # Main function
            def main():
                # Call the function to capture a photo
                capture_photo()


            if __name__ == "__main__":
                main()
