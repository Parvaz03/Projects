# Project
🔧 Requirements
1. Python Libraries
Install these using PyCharm terminal or pip:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 pymongo pyaudio datetime apscheduler
If pyaudio fails to install, try:
On Windows: download .whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
On Mac: brew install portaudio then pip install pyaudio

2. MongoDB Setup
Install MongoDB (Community Edition): https://www.mongodb.com/try/download/community

Start MongoDB server (default runs at mongodb://localhost:27017)

Create a database: voice_notes, collection: notes

📁 Project Structure
css
Copy
Edit
voice_notes_project/
├── main.py
└── utils/
    └── voice.py
    └── db.py
🧠 Code
utils/voice.py – Voice Input/Output
python

main.py – Main App
python

🛠️ Setup in PyCharm
Open PyCharm → Create New Project

Ensure interpreter uses Python 3.8+

Install all dependencies (in terminal or via PyCharm GUI)

Create project files as shown above

Run main.py

⏰ Features
Voice command for creating notes

Optional voice-input reminder time

Stores notes in MongoDB

Uses background scheduler to check and read reminders every minute
