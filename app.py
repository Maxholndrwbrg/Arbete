from flask import Flask, render_template, request, session, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Byt ut mot en säker nyckel i produktion

# Databasanslutning
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",  # Byt ut mot ditt användarnamn
        password="your_password",  # Byt ut mot ditt lösenord
        database="Inlamning_1"
    )

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html', name=session['name'])
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Anslut till databasen
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Exekvera SQL-fråga
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        # Stäng anslutning
        cursor.close()
        conn.close()
        
        # Kontrollera användarnamn och lösenord
        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['name'] = user['name']
            flash('Inloggning lyckades! Välkommen!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Ogiltigt användarnamn eller lösenord', 'error')
            return render_template('login.html'), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Du har loggats ut', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)