# 🗣️ Voice Notes & Memo System with MongoDB and Calendar Reminders

A Python-based voice assistant app to record notes and set calendar reminders using speech. Notes are stored in MongoDB and reminders are announced at scheduled times.

---

## 🎯 Features

- 🎤 Voice-based note creation
- 🕓 Optional voice-set reminders
- 🧠 Stores notes in MongoDB
- 🔔 Auto-alerts when reminders are due
- 🗂️ Modular code (voice, DB, main loop)
- 🛠️ Background job scheduler

---

## 📁 Project Structure
voice_notes_project/
├── main.py # App entry point
└── utils/
├── voice.py # Voice input/output
└── db.py # MongoDB operations

## 📁Install Requirements
-pip install -r requirements.txt
-pip install SpeechRecognition pyttsx3 pymongo pyaudio apscheduler

## 📁 Set Up MongoDB
1.Install MongoDB from https://www.mongodb.com/try/download/community
2.Start the service:

bash
mongod

## 📁Run the Application
python main.py
-Say:
1."create note" — to start a new voice memo
2."exit" — to quit the app

## 📚 Example Commands
🗣️: create note  
🗣️: Shopping List  
🗣️: Milk, Bread, Eggs  
🗣️: 2025-05-01 14:30

## ✅ Dependencies
1.SpeechRecognition
2.pyttsx3
3.pymongo
4.apscheduler
5.pyaudio

## 🛡 License
This project is licensed under the MIT License.




