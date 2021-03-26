from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

# def write_to_text(data):
# 	with open('database.txt', mode = 'a') as database:
#  	   email = data['email']
#  	   subject = data['subject']
#  	   message = data["message"]
#  	   file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', newline = '', mode = 'a') as databasecsv:
 	   email = data['email']
 	   subject = data['subject']
 	   message = data["message"]
 	   csv_writer = csv.writer(databasecsv, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
 	   csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		# write_to_text(data)
		write_to_csv(data)
		print(data)
		return redirect('./thankyou.html')
	else:
		return 'Something went wrong. Try again!'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


# @app.route('/project.html')
# def project():
#     return render_template('project.html')

# @app.route('/components.html')
# def component():
#     return render_template('components.html')


# @app.route('/<username>/<int:log_id>')
# def username(username=None, log_id=None):
#     return render_template('index.html', name=username, post_id=log_id)

# @app.route('/blog')
# def blog():
#     return 'This is a blog!'