from utils.voice import speak, get_voice_input
from utils.db import save_note, get_due_notes
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def create_note():
    title = get_voice_input("What is the title of your note?")
    if not title:
        return
    content = get_voice_input("What should I write in the note?")
    if not content:
        return
    reminder_input = get_voice_input("Do you want to set a reminder? Say date and time like '2025-05-01 14:30' or say 'no'.")
    reminder_time = None
    if reminder_input and reminder_input.lower() != "no":
        try:
            reminder_time = datetime.strptime(reminder_input, "%Y-%m-%d %H:%M")
        except ValueError:
            speak("Invalid date format. Skipping reminder.")
    save_note(title, content, reminder_time)
    speak("Note saved successfully.")

def check_reminders():
    now = datetime.now()
    due_notes = get_due_notes(now)
    for note in due_notes:
        speak(f"Reminder: {note['title']} - {note['content']}")

def main():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_reminders, 'interval', seconds=60)
    scheduler.start()
    speak("Voice memo system started. Say 'create note' to begin.")

    try:
        while True:
            command = get_voice_input("Waiting for command...")
            if command and "create" in command.lower():
                create_note()
            elif command and "exit" in command.lower():
                speak("Exiting voice memo system.")
                break
    except KeyboardInterrupt:
        pass
    finally:
        scheduler.shutdown()

if __name__ == "__main__":
    main()
