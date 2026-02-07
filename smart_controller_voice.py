import speech_recognition as sr
import pyautogui
 

# Function to play/pause the video
def play_pause_video():
    try:
        pyautogui.press('space')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to play the next video
def play_next_video():
    try:
        pyautogui.keyDown('shift')
        pyautogui.press('n')
        pyautogui.keyUp('shift')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to play the previous video
def play_previous_video():
    try:
        pyautogui.keyDown('shift')
        pyautogui.press('p')
        pyautogui.keyUp('shift')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to skip forward 5 seconds
def skip_forward():
    try:
        pyautogui.press('right')  # Simulates pressing the right arrow key
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to skip backward 5 seconds
def skip_backward():
    try:
        pyautogui.press('left')  # Simulates pressing the left arrow key
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to increase the volume
def increase_volume():
    try:
        pyautogui.press('volumeup')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to decrease the volume
def decrease_volume():
    try:
        pyautogui.press('volumedown')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")

# Function to mute the volume
def mute_volume():
    try:
        pyautogui.press('volumemute')
    except pyautogui.FailSafeException:
        print("PyAutoGUI failed to simulate keyboard input")
 
# Function to listen for voice commands and execute corresponding actions
def listen_and_execute(r, source):
    print("Listening...")
    r.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-US').lower()  # Convert to lowercase for easier matching
        print(f"You said: {command}")

        if 'play' in command or 'pause' in command:
            play_pause_video()
        elif 'next' in command:
            play_next_video()
        elif 'previous' in command:
            play_previous_video()
        elif 'forward' in command:
            skip_forward()
        elif 'backward' in command:
            skip_backward()
        elif 'increase volume' in command:
            increase_volume()
        elif 'decrease volume' in command:
            decrease_volume()
        elif 'mute' in command:
            mute_volume()
        elif 'stop' in command:
            print("Stopping voice control...")
            return False  # Return False to stop the loop
        else:
            print("Invalid command")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return True  # Continue listening

# Main function to run the command loop
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        keep_listening = True
        while keep_listening:  # Run until 'stop' command is detected
            try:
                keep_listening = listen_and_execute(r, source)
            except Exception as e:
                print(f"An error occurred in the loop: {e}")

if __name__ == "__main__":
    main()
