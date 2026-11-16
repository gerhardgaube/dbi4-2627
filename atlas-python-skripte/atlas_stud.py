from pymongo import MongoClient

# Verbindungszeichenfolge für MongoDB Atlas (ersetzen Sie diese mit Ihrer eigenen)
mongo_uri = "mongodb+srv://:@testgerhard.0rechap.mongodb.net/"

# Verbindung zur Datenbank herstellen
client = MongoClient(mongo_uri)

# Datenbank und Sammlung auswählen
database = client["InformatikG2"]
collection = database["StudentenG2"]

# Beispiel-Daten einfügen
student_data = [
    {"Vorname": "Max", "Nachname": "Mustermann", "Matrikelnummer": 12345},
    {"Vorname": "Anna", "Nachname": "Musterfrau", "Matrikelnummer": 67890},
    {"Vorname": "Donald", "Nachname": "Musterfrau", "Matrikelnummer": 222222}
]

# Daten einfügen
collection.insert_many(student_data)

# Alle Studenten anzeigen
print("Alle Studenten:")
for student in collection.find():
    print(student)

# Ein Studenten-Dokument aktualisieren
update_criteria = {"Matrikelnummer": 12345}
update_data = {"$set": {"Nachname": "NeuerNachname"}}
collection.update_one(update_criteria, update_data)

# Alle Studenten nach dem Update anzeigen
print("\nAlle Studenten nach dem Update:")
for student in collection.find():
    print(student)

# Ein Studenten-Dokument löschen
#delete_criteria = {"Matrikelnummer": 67890}
#collection.delete_one(delete_criteria)

# Alle Studenten nach dem Löschen anzeigen
print("\nAlle Studenten nach dem Löschen:")
for student in collection.find():
    print(student)

# Verbindung schließen
client.close()
