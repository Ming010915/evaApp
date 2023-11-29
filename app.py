#TODO: The images are repeated after changing users 

from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os

app = Flask(__name__)

# Configuration
app.config['DATABASE'] = 'feedback_data.db'

def get_db_connection():
    return sqlite3.connect(app.config['DATABASE'])

def create_table():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS feedback_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_name TEXT,
                score INTEGER,
                comments TEXT,
                userName TEXT
            )
        ''')

def write_to_sqlite(entry):
    with get_db_connection() as conn:
        conn.execute('''
            INSERT INTO feedback_data (image_name, score, comments, userName)
            VALUES (?, ?, ?, ?)
        ''', (entry['image_name'], entry["score"], entry['comments'], entry['userName']))

def resultNumber(image_name):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM feedback_data WHERE image_name = ?
        ''', (image_name,))
    
# Initialize SQLite Database
create_table()

@app.route('/number_of_images')
def number_of_images():
    # Specify the path to your images folder
    images_folder_path = 'static/images'

    # Get the list of files in the folder
    image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(images_folder_path, f))]
    message = {'length': len(image_files) }

    # Pass the count of images to the template
    return jsonify(message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_data', methods=['POST'])
def record_data():
    comments = request.form.get('comments')
    image_name = request.form.get('imageName')
    userName = request.form.get('userName')
    score = request.form.get('score')

    entry = {'image_name': image_name, 'score': score, 'comments': comments, 'userName': userName}
    write_to_sqlite(entry)  # Write only the latest entry to the database
    resultNumber(image_name)
    # Redirect to the index page after recording data
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)