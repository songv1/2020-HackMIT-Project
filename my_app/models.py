from my_app import db

class Fact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	value = db.Column(db.String(100))

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	
	#According to Reedsy, flash fiction has an upper limit of 1500 words.
	description = db.Column(db.String(1500))