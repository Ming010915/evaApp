from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Initialize an empty list to store data
data_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_data', methods=['POST'])
def record_data():
    # Get the feedback, comments, and image name from the request
    feedback = request.form.get('feedback')
    comments = request.form.get('comments')
    image_name = request.form.get('imageName')

    # Add the feedback, comments, and image name to the data list
    data_list.append({'image_name': image_name, 'feedback': feedback, 'comments': comments})

    # Write the data to a CSV file
    write_to_csv(data_list)

    # Return a response (this can be customized based on your needs)
    return "Feedback recorded successfully!"

def write_to_csv(data):
    # Define the CSV file path
    csv_file_path = 'feedback_data.csv'

    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ImageName', 'Feedback', 'Comments']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        csv_writer.writeheader()

        # Write data
        for entry in data:
            csv_writer.writerow({'ImageName': entry['image_name'], 'Feedback': entry['feedback'], 'Comments': entry['comments']})

if __name__ == '__main__':
    app.run(debug=True)
