from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) #Here we use the flask class to instantiate an app
print(__name__)

#Frameworks give us a higher level of abstraction - meaning t
#-hat we don't need to know what the code is doing underneigh
#We just need to know that the parts give us extra features
#The decorators below are called end points

@app.route('/') #We pass what is received here, into the hello world name param below
def my_home():
    return render_template('index.html') 
    #Putting the above alone will not work as flask auto tries to find a folder called templates
    #So, we must first create a folder called templates

@app.route('/<string:page_name>') #This works the same as having the below
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt', mode='a') as database: #Mode=a appends to the file
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2: 
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'somthing went wrong. Try again!'


#Rather than using the below, we have created a dynamic version above
# @app.route('/work.html') #This is a decorator 
# def work():
#     return render_template('work.html') 

# @app.route('/about.html') #This is a decorator 
# def about():
#     return render_template('about.html') 

# @app.route('/index.html') #This is a decorator 
# def index():
#     return render_template('index.html')

# @app.route('/works.html') #This is a decorator 
# def works():
#     return render_template('works.html') 

# @app.route('/contact.html') 
# def contact():
#     return render_template('contact.html')

#In order to use HTML, CSS and JS files rather than just passing text into strings
#-we use render template
