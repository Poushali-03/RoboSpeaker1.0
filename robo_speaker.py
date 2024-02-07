import pyttsx3

def robo_speaker(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Speak the provided text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    # Example usage
    text_to_speak = input("Enter the text you want the Robo Speaker to say: ")
    robo_speaker(text_to_speak)



