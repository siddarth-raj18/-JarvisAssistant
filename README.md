# 🎙️ Jarvis Voice Assistant

A simple Python-based voice assistant that listens to voice commands and performs basic tasks on your Windows computer.

Jarvis uses speech recognition to understand spoken commands and text-to-speech to respond to the user. It can open applications, launch websites, and search Google or YouTube using voice commands.

## ✨ Features

- 🎤 Voice command recognition
- 🔊 Voice responses using text-to-speech
- 👋 Wake Jarvis using the voice command "Jarvis"
- 😴 Put Jarvis into standby mode using voice commands
- 🌐 Open Google, YouTube, and ChatGPT
- 🔎 Search Google using voice commands
- ▶️ Search YouTube using voice commands
- 📝 Open Notepad
- 🧮 Open Calculator
- 🛑 Stop the assistant using a voice command

## 🛠️ Technologies Used

- **Python 3.13**
- **SpeechRecognition**: Converts spoken commands into text.
- **PyAudio**: Provides microphone audio input.
- **pyttsx3**: Converts text responses into speech.
- **Webbrowser**: Opens websites in the default browser.
- **Subprocess**: Launches Windows applications.

## 📋 Prerequisites

Before running Jarvis, ensure you have:

- Windows 10 or Windows 11
- Python 3.13 installed
- Git installed
- A working microphone
- An internet connection for Google Speech Recognition and online searches

## 📥 Installation

### 1. Clone the repository

Open PowerShell or the VS Code terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/JarvisAssistant.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd JarvisAssistant
```

### 3. Create a virtual environment

```bash
py -3.13 -m venv .venv
```

### 4. Activate the virtual environment

In PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If microphone or PyAudio installation issues occur, verify that Python 3.13 is being used and that the required audio dependencies are installed.

## ▶️ How to Run

Start the assistant using:

```bash
python jarvis.py
```

Allow microphone access if Windows requests permission.

Say **"Jarvis"** to wake the assistant if it starts in standby mode.

## 🗣️ Voice Commands

| Voice Command | Action |
|---|---|
| "Jarvis" | Wake the assistant |
| "Open Google" | Open Google in your browser |
| "Open YouTube" | Open YouTube |
| "Open ChatGPT" | Open ChatGPT |
| "Search Google for Python tutorials" | Search Google |
| "Search YouTube for Python tutorials" | Search YouTube |
| "Open Notepad" | Launch Notepad |
| "Open Calculator" | Launch Calculator |
| "Go to sleep" | Put Jarvis into standby mode |
| "Stop Jarvis" | Stop the assistant |

*Available commands depend on the command-handling logic implemented in `jarvis.py`.*

## 📁 Project Structure

```text
JarvisAssistant/
│
├── jarvis.py          # Main voice assistant program
├── requirements.txt   # Python dependencies
├── .gitignore         # Files excluded from Git
└── README.md          # Project documentation
```

## 📦 Dependencies

The project dependencies are listed in `requirements.txt`.

Currently, the project uses:

- `SpeechRecognition[audio]`
- `pyttsx3`

## ⚠️ Important Notes

- Google Speech Recognition requires an internet connection.
- Microphone access must be enabled in Windows.
- Application commands are designed for Windows.
- Some commands may need adjustment depending on your system configuration.
- The assistant does not continuously operate as an offline wake-word detector. Its speech recognition depends on the implemented listening logic.

## 🔮 Future Improvements

Potential enhancements include:

- Offline speech recognition
- Improved wake-word detection
- Mobile application integration
- Weather updates
- Time and date announcements
- System volume control
- More application-launching commands
- AI-powered question answering

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit your changes.
5. Submit a pull request.

## 📄 License

This project is currently available for personal learning and experimentation. Add a license file if you want to specify the terms under which others may use, modify, or distribute the code.

---

**Built with Python 🐍**
