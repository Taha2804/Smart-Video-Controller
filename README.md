# 🎮 Smart Video Controller

A multi-modal video player control system that enables hands-free operation through both **voice commands** and **hand gestures**. This project combines computer vision and speech recognition to provide an intuitive, accessible video playback experience.

## 🌟 Features

### Voice Control
- **Play/Pause**: Toggle video playback with voice commands
- **Navigation**: Skip to next or previous video
- **Seeking**: Jump forward or backward by 5 seconds
- **Volume Control**: Increase, decrease, or mute audio
- **Stop Command**: Exit voice control mode

### Hand Gesture Control
- **1 Finger**: Seek forward (right arrow)
- **2 Fingers**: Seek backward (left arrow)
- **3 Fingers**: Volume up
- **4 Fingers**: Volume down
- **5 Fingers**: Play/Pause toggle

### Web-Based Video Player
- Custom-designed dark theme video player interface
- Progress bar with time tracking
- Video upload functionality
- Responsive controls and metadata display
- Smooth animations and hover effects

## 🛠️ Technologies Used

### Backend
- **Python 3.x**
- **OpenCV**: Computer vision for hand gesture detection
- **MediaPipe**: Hand tracking and landmark detection
- **SpeechRecognition**: Voice command processing with Google Speech API
- **PyAutoGUI**: Keyboard automation for control simulation

### Frontend
- **HTML5**: Video player structure
- **CSS3**: Modern, responsive UI styling
- **JavaScript (Vanilla)**: Player controls and event handling

## 📋 Prerequisites

```bash
# Python dependencies
pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install SpeechRecognition
pip install pyaudio
```

**Note**: For microphone input, you may need to install additional system dependencies:
- **Windows**: PyAudio should work out of the box
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **macOS**: `brew install portaudio`

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-video-controller.git
cd smart-video-controller
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up the web player**
   - Open `player.html` in a web browser
   - Or serve it using a local server:
   ```bash
   python -m http.server 8000
   ```

## 💻 Usage

### Voice Control Mode

```bash
python smart_controller_voice.py
```

**Supported Commands**:
- "play" or "pause" - Toggle playback
- "next" - Next video
- "previous" - Previous video
- "forward" - Skip ahead 5 seconds
- "backward" - Skip back 5 seconds
- "increase volume" - Raise volume
- "decrease volume" - Lower volume
- "mute" - Toggle mute
- "stop" - Exit voice control

### Hand Gesture Control Mode

```bash
python Smart_Controller_hand_gesture.py
```

**Gesture Instructions**:
1. Position your hand in front of the webcam
2. Ensure good lighting for optimal detection
3. Hold gestures for 0.2 seconds for activation
4. Press `ESC` to exit

### Web Video Player

1. Open `player.html` in your browser
2. Upload a video using the file input
3. Control playback using the on-screen buttons
4. Or use voice/gesture control for hands-free operation

## 📁 Project Structure

```
smart-video-controller/
│
├── smart_controller_voice.py      # Voice command control script
├── Smart_Controller_hand_gesture.py # Hand gesture recognition script
├── player.html                     # Video player HTML structure
├── style.css                       # Player styling
├── script.js                       # Player functionality
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

## 🎯 How It Works

### Voice Control
1. Microphone captures audio input
2. Google Speech Recognition API converts speech to text
3. Command parser identifies the action
4. PyAutoGUI simulates keyboard shortcuts
5. Video player responds to keyboard input

### Hand Gesture Control
1. Webcam captures video frames
2. MediaPipe detects hand landmarks
3. Custom algorithm counts extended fingers
4. Gesture mapped to specific keyboard action
5. PyAutoGUI executes the command

## 🔧 Configuration

### Adjusting Gesture Sensitivity
In `Smart_Controller_hand_gesture.py`, modify the debounce time:
```python
elif (end_time-start_time) > 0.2:  # Change 0.2 to adjust delay
```

### Customizing Voice Commands
In `smart_controller_voice.py`, add new commands:
```python
elif 'your_command' in command:
    your_function()
```

## 🐛 Troubleshooting

### Voice Control Issues
- Ensure microphone permissions are granted
- Check internet connection for Google Speech API
- Reduce background noise for better recognition

### Gesture Control Issues
- Ensure adequate lighting
- Position hand within webcam frame
- Check if webcam is accessible (not used by another app)
- Adjust `max_num_hands` parameter if needed

### Browser Compatibility
- Use modern browsers (Chrome, Firefox, Edge)
- Enable autoplay policies for video playback
- Check browser console for JavaScript errors

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Multi-hand gesture support
- [ ] Custom wake word for voice activation
- [ ] Gesture customization interface
- [ ] Mobile app integration
- [ ] Playlist management
- [ ] Gesture training mode
- [ ] Offline voice recognition

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- **MediaPipe** team for hand tracking solutions
- **Google** for Speech Recognition API
- **OpenCV** community for computer vision tools
- Inspiration from accessibility-focused HCI research

## 📧 Contact

Your Name - [@yourhandle](https://twitter.com/yourhandle) - your.email@example.com

Project Link: [https://github.com/yourusername/smart-video-controller](https://github.com/yourusername/smart-video-controller)

---

**⭐ If you found this project helpful, please consider giving it a star!**
