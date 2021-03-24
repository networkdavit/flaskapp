# flaskapp.py
# This is a "hello world" app sample for flask app. You may have a different file.
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/') 
def hello_world():
   return render_template("index.html") 

@app.route('/<page_name>')
def page(page_name):
    return render_template(f"{page_name}")

@app.route("/receive_data", methods=['POST'])
def receive_data():
	if request.method == "POST":
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]
		data = f"Email: {email} \nSubject: {subject} \nMessage: {message}\n    "
		f = open("message.txt", "a")
		f.write(data)
		f.close()
		return redirect("index.html")


if __name__ == '__main__':
   app.run()
   