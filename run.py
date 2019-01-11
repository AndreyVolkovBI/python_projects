from flask import Flask, redirect, render_template, url_for, request
from flask_assets import Bundle, Environment
from json import dump, load
from datetime import datetime
import pytz

app = Flask(__name__)

def getReviews():
	path = './static/db/reviews.json'
	with open(path, 'r', encoding='utf-8') as f:
		return load(f)

@app.route("/")
def home():
	content = request.args.get("name")
	if content:
		addReview(content)
	return render_template('index.html')

@app.route("/answers")
def answers():
	return render_template('answers.html', title="Answers", data=getReviews())

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

def getTime():
    time = str(datetime.now(pytz.timezone("Europe/Moscow"))).split('-')
    date = time[2].split(' ')[0] + '.' + time[1] + '.' + time[0]
    time = time[2].split(' ')[1].split('.')[0]
    return time + ' ' + date

# class Review(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	date = db.Column(db.String(20), unique=False, nullable=False)
# 	content = db.Column(db.String(2000), unique=False, nullable=False)

# 	def __repr__(self):
# 		return f"Review('{self.id}', '{self.date}', '{self.content}')"

data = {}
def addReview(content):
	path = './static/db/reviews.json'
	with open(path, 'r', encoding='utf-8') as f:
		global data
		data = load(f)
	with open('./static/db/reviews.json', 'w', encoding='utf-8') as f:
		data[getTime()] = content
		dump(data, f, ensure_ascii=False)

# def convertToDict(file):
# 	return [item.__dict__ for item in file]

# def getJsonLink():
#     with open('./static/db/reviews.json', 'w', encoding='utf-8') as f:
#         f.write(dumps(getReviews()))
#     return True


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')