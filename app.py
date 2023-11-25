from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Initialize the data list by reading from the existing CSV file
data_list = []

def read_from_csv():
    csv_file_path = 'feedback_data.csv'
    try:
        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data_list.append({'image_name': row['ImageName'], 'feedback': row['Feedback'], 'comments': row['Comments']})
    except FileNotFoundError:
        # Handle the case where the file doesn't exist yet
        pass

# Read data from CSV when the app starts
read_from_csv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_data', methods=['POST'])
def record_data():
    feedback = request.form.get('feedback')
    comments = request.form.get('comments')
    image_name = request.form.get('imageName')

    data_list.append({'image_name': image_name, 'feedback': feedback, 'comments': comments})

    write_to_csv(data_list)

    return render_template('index.html')  # or redirect to another page after recording data

def write_to_csv(data):
    csv_file_path = 'feedback_data.csv'

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ImageName', 'Feedback', 'Comments']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()

        for entry in data:
            csv_writer.writerow({'ImageName': entry['image_name'], 'Feedback': entry['feedback'], 'Comments': entry['comments']})

if __name__ == '__main__':
    app.run(debug=True)
