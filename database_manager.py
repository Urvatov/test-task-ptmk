import sqlite3

class DatabaseManager:
    def __init__(self, database : str):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    def __str__(self) -> str:
        return self.database


data = DatabaseManager("database.db")