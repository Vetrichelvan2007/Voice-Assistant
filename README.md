🎙️ Mini Voice Assistant
A Python-based voice assistant that can open apps, play YouTube videos, tell jokes, search Google, answer questions using a local AI model (Mistral via Ollama), and more.

✨ Features
FeatureTrigger WordsOpen browser / Google / Chrome"browser", "google", "chrome"Play a song on YouTube"play [song name]"Open any application"open [app name]"Search on Google"search ... google"Tell a joke"joke"Get current date & time"date", "time"AI-powered Q&A (Mistral)Any other spoken queryGreet"hello", "hi"Exit assistant"exit"

🛠️ Requirements
Python Version
Python 3.8+
Python Libraries
Install all dependencies with:
bashpip install pyttsx3 pywhatkit pyjokes AppOpener requests SpeechRecognition pyaudio
LibraryPurposepyttsx3Text-to-speech enginepywhatkitPlay YouTube videospyjokesFetch random jokesAppOpenerOpen installed applicationsrequestsHTTP calls to local Mistral modelSpeechRecognitionCapture and transcribe voice inputpyaudioMicrophone access (required by SpeechRecognition)
Local AI Model (Ollama + Mistral)
The assistant uses a locally running Mistral model for general Q&A. To set it up:

Install Ollama
Pull the Mistral model:

bash   ollama pull mistral

Start the Ollama server:

bash   ollama serve
The assistant expects the model to be accessible at http://localhost:11434.

🚀 Getting Started

Clone or download this repository.
Install dependencies:

bash   pip install pyttsx3 pywhatkit pyjokes AppOpener requests SpeechRecognition pyaudio

Start Ollama (for AI Q&A support):

bash   ollama serve

Run the assistant:

bash   python assistant.py

💬 Usage Examples
You sayAssistant does"Hello"Greets you"Open Chrome"Opens Chrome browser"Play Believer"Plays Believer on YouTube"Open Notepad"Opens Notepad"Tell me a joke"Tells a random joke"What is the time?"Announces current date & time"What is machine learning?"Queries local Mistral model and speaks the answer"Exit"Shuts down the assistant

🔧 Configuration
You can adjust the assistant's voice and speech rate in the source file:
pythonassistant.setProperty('rate', 170)        # Speech speed (words per minute)
assistant.setProperty('voice', voices[1].id)  # Voice index (0 = male, 1 = female on most systems)

📁 Project Structure
mini-voice-assistant/
│
├── assistant.py       # Main assistant script
└── README.md          # Project documentation

⚠️ Known Limitations

Speech recognition requires a working microphone and an active internet connection (uses Google Speech API).
App opening via AppOpener depends on the app being installed and recognizable by name.
The local Mistral model must be running before launching the assistant for AI Q&A to work.
Long AI responses may take a few seconds to be spoken aloud.


📄 License
This project is open-source and free to use for personal and educational purposes.
