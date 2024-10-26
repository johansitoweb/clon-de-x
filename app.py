from flask import Flask, render_template, request, redirect, url_for  
import sqlite3  
from database import init_db  

app = Flask(__name__)  

# Inicializa la base de datos  
init_db()  

def get_db_connection():  
    conn = sqlite3.connect('messages.db')  
    conn.row_factory = sqlite3.Row  
    return conn  

@app.route('/', methods=['GET', 'POST'])  
def home():  
    if request.method == 'POST':  
        content = request.form['content']  
        conn = get_db_connection()  
        conn.execute('INSERT INTO messages (content) VALUES (?)', (content,))  
        conn.commit()  
        conn.close()  
        return redirect(url_for('home'))  

    conn = get_db_connection()  
    messages = conn.execute('SELECT * FROM messages ORDER BY id DESC').fetchall()  
    conn.close()  
    return render_template('index.html', messages=messages)  

@app.route('/like/<int:message_id>')  
def like(message_id):  
    conn = get_db_connection()  
    conn.execute('UPDATE messages SET likes = likes + 1 WHERE id = ?', (message_id,))  
    conn.commit()  
    conn.close()  
    return redirect(url_for('home'))  

if __name__ == '__main__':  
    app.run(debug=True)



    