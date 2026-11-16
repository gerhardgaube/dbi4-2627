from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure

# ------------------------------------------------------------
# MongoDB Atlas Connection String (ANPASSEN!)
# ------------------------------------------------------------
MONGODB_URI = "mongodb+srv://:@testgerhard.0rechap.mongodb.net/"

DB_NAME = "sample_mflix"


def main():
    try:
        # Verbindung herstellen
        client = MongoClient(MONGODB_URI)

        # Verbindung testen
        client.admin.command("ping")
        print("Verbindung zu MongoDB Atlas erfolgreich.\n")

        db = client[DB_NAME]

        # Collections anzeigen
        print("Collections:")
        print(db.list_collection_names())
        print()

        # ------------------------------------------------------------
        # 1) Einige Filme
        # ------------------------------------------------------------
        print("=== Filme (Beispiel) ===")
        for doc in db.movies.find(
            {},
            {
                "_id": 0,
                "title": 1,
                "year": 1,
                "imdb.rating": 1,
            },
        ).limit(5):
            pprint(doc)
        print()

        # ------------------------------------------------------------
        # 2) Filter: gute Filme
        # ------------------------------------------------------------
        print("=== Gute Filme (IMDb >= 7.5) ===")
        for doc in db.movies.find(
            {"imdb.rating": {"$gte": 7.5}},
            {
                "_id": 0,
                "title": 1,
                "year": 1,
                "imdb.rating": 1,
            },
        ).sort("imdb.rating", -1).limit(10):
            pprint(doc)
        print()

        # ------------------------------------------------------------
        # 3) Aggregation: Kommentare zählen
        # ------------------------------------------------------------
        print("=== Top Filme nach Kommentaren ===")
        pipeline = [
            {"$group": {"_id": "$movie_id", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 5},
        ]

        for doc in db.comments.aggregate(pipeline):
            pprint(doc)
        print()

        # ------------------------------------------------------------
        # 4) $lookup (Join)
        # ------------------------------------------------------------
        print("=== Kommentare + Filmtitel ===")
        pipeline_lookup = [
            {"$group": {"_id": "$movie_id", "count": {"$sum": 1}}},
            {
                "$lookup": {
                    "from": "movies",
                    "localField": "_id",
                    "foreignField": "_id",
                    "as": "movie",
                }
            },
            {"$unwind": "$movie"},
            {
                "$project": {
                    "_id": 0,
                    "title": "$movie.title",
                    "count": 1,
                }
            },
            {"$sort": {"count": -1}},
            {"$limit": 5},
        ]

        for doc in db.comments.aggregate(pipeline_lookup):
            pprint(doc)
        print()

    except ConfigurationError as e:
        print(f"Fehler im Connection String: {e}")
    except ConnectionFailure as e:
        print(f"Verbindung fehlgeschlagen: {e}")
    except OperationFailure as e:
        print(f"MongoDB Fehler: {e}")
    except Exception as e:
        print(f"Allgemeiner Fehler: {e}")
    finally:
        try:
            client.close()
        except:
            pass


if __name__ == "__main__":
    main()
