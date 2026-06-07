# Friday AI Voice Assistant

## Overview

Friday AI Voice Assistant is a Python-based desktop voice assistant developed as a learning project to explore speech recognition, text-to-speech conversion, and desktop automation on macOS.

The assistant can understand voice commands and perform tasks such as searching Wikipedia, opening websites, launching macOS applications, playing music, taking notes, and providing useful information to the user.

Supported macOS applications include FaceTime, Photos, WhatsApp, Apple Music, Safari, and Google Chrome.

---

## Features

### Voice Assistant Features

- Voice command recognition
- Text-to-speech responses
- Tell current date and time
- Search information using Wikipedia
- Search queries on Google
- Tell jokes
- Play music
- Take and save notes
- Open websites through voice commands

### macOS Application Control

The assistant can launch commonly used macOS applications using voice commands, including:

- FaceTime
- Photos
- WhatsApp
- Apple Music
- Safari
- Google Chrome

Example voice commands:

- "Open FaceTime"
- "Open WhatsApp"
- "Open Chrome"
- "Open Safari"
- "Open Photos"
- "Open Music"

### Desktop Automation

- Launch applications using voice commands
- Open websites automatically
- Execute basic desktop tasks
- Improve productivity through hands-free interaction

---

## Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- Wikipedia API
- PyAutoGUI
- pyjokes

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/friday-ai-voice-assistant.git
cd friday-ai-voice-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Project

```bash
python friday.py
```

---

## Sample Commands

- Open FaceTime
- Open WhatsApp
- Open Chrome
- Open Safari
- Open Photos
- Open Music
- Search Wikipedia
- Tell a joke
- Tell the current time
- Take a note

---

## What I Learned

- Speech recognition using Python
- Text-to-speech implementation
- Desktop automation on macOS
- Working with external Python libraries
- Handling voice-based user interactions
- Managing Python project dependencies

---

## Future Improvements

- Add weather information
- Integrate AI-powered conversations
- Add email functionality
- Improve command recognition accuracy
- Create a graphical user interface (GUI)
- Support additional automation features

---

## Requirements

- Python 3.8 or higher
- Microphone access
- Required packages listed in requirements.txt

---

## License

This project is distributed under the MIT License.

---

## Disclaimer

This project was developed as a personal learning project to understand voice assistants, speech processing, desktop automation, and Python application development.
