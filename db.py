from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.voice_notes
notes_collection = db.notes

def save_note(title, content, reminder_time=None):
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now(),
        "reminder_time": reminder_time
    }
    result = notes_collection.insert_one(note)
    return result.inserted_id

def get_due_notes(current_time):
    return list(notes_collection.find({"reminder_time": {"$lte": current_time}}))
