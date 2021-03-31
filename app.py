from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///submission.db"
db = SQLAlchemy(app)

class Submission(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(200), nullable = False)
	subject = db.Column(db.String(200), nullable = False)
	message = db.Column(db.String(200), nullable = False)

	def __repr__(self):
		return "<Submission %r>" % self.id

@app.route('/') 
def hello_world():
   return render_template("index.html") 

@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)

@app.route("/receive_data", methods=['POST'])
def receive_data():
	if request.method == "POST":
		email = request.form["email"]
		subject = request.form["subject"]
		message = request.form["message"]

		submission = Submission(email = email, subject = subject, message = message)

		try:
			db.session.add(submission)
			db.session.commit()
			return redirect("thankyou.html")
		except:
			return "did not save to database"
	else:
		return "something went wrong"


if __name__ == '__main__':
   app.run()
   
