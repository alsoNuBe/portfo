from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
# print(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
    # return 'Hello, Andrew - fantastic day today!'
    # print(url_for('static', filename='neptune.ico'))
    # return render_template('index.html', name=username, num_id=post_id)



@app.route('/')
def my_site():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    # return 'Hello, Andrew - fantastic day today!'
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        fieldnames=['email', 'subject', 'message']
        writer = csv.DictWriter(database, fieldnames)
        writer.writerow({'email': data['email'], 'subject': data['subject'], 'message': data['message']})


def write_to_csv2(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write_file = csv.writer(database, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csv_write_file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # data = 'Al'
            # print(data)
            # write_to_file(data)
            write_to_csv2(data)
            # return 'form submitted'
            # return redirect('/thankyou.html')
            # return render_template("thankyou.html", messages=json.loads(messages))
            return render_template("thankyou.html", messages=data)
            # return 'form submitted'
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong - try again!'
    # return 'form submitted, hooorrraaaayyy!'