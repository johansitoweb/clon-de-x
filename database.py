import sqlite3  

def init_db():  
    conn = sqlite3.connect('messages.db')  
    cursor = conn.cursor()  
    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS messages (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            content TEXT NOT NULL,  
            likes INTEGER DEFAULT 0  
        )  
    ''')  
    conn.commit()  
    conn.close() 


    