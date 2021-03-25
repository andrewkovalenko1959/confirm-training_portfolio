# http://www.mashup-template.com/templates.html
# https://plugins.jetbrains.com/plugin/10037-csv-plugin
# python3 -m venv /path/to/new/virtual/environment

# 1.cd section19
# 2. cd Web_Server2
# 3. python3 -m venv venv  ---> creates venviroment
# 4. to use already created folder as venv :
# 4.1 go back section19
# 4.2 create Web_Server2
# 4.3 python3 -m venv Web_Server2


# set FLASK_APP=265.py set FLASK_APP=development  # debug to on run :
# D:\BLOB\Solutions\Udemy\Complete-Python-Developer-Zero-to-Mastery\Section19\Web_Server\Scripts\acitivate.bat from
# CMD flask run : to run flask

# from flask import Flask
from flask import Flask, render_template, request, redirect
import csv  # for 273

app = Flask(__name__)


# @app.route('/') # here is problem : you can not call home page
# def my_home():
#     return render_template('index.html')

# we are goinf to use variable
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')

@app.route('/')  # here is problem : you can not call home page
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# < span
# id = "typed-strings" >
# < span > I
# 'm Andrey Kovalenko</span>
# < span > Python
# Expert < / span >
# < span > Working as a
# Freelance < / span >
# < / span >
# < span
# id = "typed" > < / span >
#
# for 269

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         # write_to_file(data)  # for 272 video
#         write_to_csv(data)
#         # return 'form has been submitted'
#         return redirect('thankyou.html')
#     else:
#         return 'something went wrong'


# go to contact.html and finf "send"

# < form action = "" class ="reveal-content" > < div  class ="row" > < div class ="col-md-7" >

# < form action = "submit_form" method="post" class ="reveal-content" > < div  class ="row" > < div class ="col-md-7" >


# for 272
def write_to_file(data):  # data is in submit_form()
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


# for 273
def write_to_csv(data):  # data is in submit_form()
    with open('database.csv', newline='', mode='a') as database2:  # with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',')  # , newline='' , quotechar='"', quoting=csv.QUOTE_MINIMAL
        csv_write.writerow([email, subject, message])


# for 275

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


# for 278
# create login

# https://www.pythonanywhere.com/login/?next=/
# create portfo repos. in my github
# copy  https://github.com/andrewkovalenko1959/portfo.git
# run: git clone https://github.com/andrewkovalenko1959/portfo.git
# creates a folder

