from flask import Flask, render_template, request, redirect, url_for
import csv
import sqlite3

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
                feedback TEXT,
                comments TEXT,
                user TEXT
            )
        ''')

def read_from_csv():
    csv_file_path = 'feedback_data.csv'
    data = []
    try:
        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append({
                    'image_name': row['ImageName'],
                    'feedback': row['Feedback'],
                    'comments': row['Comments'],
                    'user': row['User']
                })
    except FileNotFoundError:
        pass
    return data

def write_to_sqlite(data):
    with get_db_connection() as conn:
        for entry in data:
            conn.execute('''
                INSERT INTO feedback_data (image_name, feedback, comments, user)
                VALUES (?, ?, ?, ?)
            ''', (entry['image_name'], entry['feedback'], entry['comments'], entry['user']))

# Initialize SQLite Database
create_table()

# Read data from CSV when the app starts
data_list = read_from_csv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_data', methods=['POST'])
def record_data():
    feedback = request.form.get('feedback')
    comments = request.form.get('comments')
    image_name = request.form.get('imageName')
    user = request.form.get('user')

    # Validate data if needed

    data_list.append({'image_name': image_name, 'feedback': feedback, 'comments': comments, 'user': user})
    write_to_sqlite(data_list)

    # Redirect to the index page after recording data
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)