# 🎙️ Voice Command Assistant

A Python-based voice assistant that listens to your commands and performs actions like searching on Wikipedia, opening websites, telling the time, or noting tasks. It includes a basic authentication step and uses speech for both input and output.

---

## 📌 Features

- 🗣️ **Voice Activation**: Begins execution when the assistant name ("jarvis") is spoken.
- 🔐 **Password Security**: Asks for a voice-confirmed password before allowing tasks.
- 📚 **Wikipedia Search**: Answers questions starting with "tell me about..."
- 🌐 **Open Websites**: Supports opening YouTube and Google via voice commands.
- ⏰ **Tells Time**: Speaks the current time on request.
- 📝 **Task Reminder**: Takes a task from your voice and stores it temporarily.
- 🛑 **Shutdown**: Ends the assistant gracefully on command.

---

## 🧰 Technologies Used

- Python 3.12  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)  
- [PyAudio](https://pypi.org/project/PyAudio/)  
- [pyttsx3](https://pypi.org/project/pyttsx3/)  
- [Wikipedia API](https://pypi.org/project/wikipedia/)  
- Webbrowser, OS, and datetime modules

---

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/voice-command-assistant.git
   cd voice-command-assistant
