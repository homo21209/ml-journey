import sqlite3
from dataclasses import dataclass

def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute("""
                 CREATE TABLE IF NOT EXIST users(
                 id INTEGER PRIMARY KEY,
                 NAME STRING NOT NULL,
                 EMAIL STRING NOT NULL
                 )"""
                )
    conn.commit()
    conn.close()

@dataclass
class User:
    id:int
    name:str
    email:str


    def save(self):
        conn = sqlite3.connect('users.db')
        conn.execute("INSERT OR REPLACE INTO user (id,name,email) VALUES (?,?,?)",(self.id,self.name,self.email))
        conn.commit()
        conn.close()
    
    def delete(self):
        conn = sqlite3.connect('users.db')
        conn.execute('DELETE FROM users WHERE id = ?',(self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get(user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.execute('SELECT id,name,email FROM users WHERE id = ?',(user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(*row)
        else:
            return None
    
