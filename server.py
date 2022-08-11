import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def database_csv(data):
    with open('./database.csv', mode='a', newline='') as DATABASE_CSV:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        data_csv = csv.writer(DATABASE_CSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_csv.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        database_csv(data)
        return redirect('contact_after.html')
    else:
        return 'Something Went Wrong'
